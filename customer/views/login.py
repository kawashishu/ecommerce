
from django.views import View

from store.models import Order
from ..models import Customer
from ..form import RegistrationForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')

            user = Customer.objects.create_user(
                name=name, email=email, password=password, phone=phone)
            user.save()

            current_site = get_current_site(request=request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            send_email = EmailMessage(mail_subject, message, to=[email])
            try:
                send_email.send()
                messages.success(
                    request=request,
                    message="Please confirm your email \
                    address to complete the registration"
                )
                return redirect('signup')
            except Exception:
                messages.error(
                    request=request,
                    message="Email not sent"
                )
                return redirect('signup')
        else:
            messages.error(request=request, message="Register failed!")
        context = {
            'form_signup': form,
        }
        return render(request, 'signup.html', context)


class LoginView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'signin.html', {'form_signin': form})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request=request, user=user)
            messages.success(request=request, message="Login successful!")
            return redirect('index')
        else:
            messages.error(request=request, message="Login failed!")
            return redirect('signup')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Customer.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request=request, user=user,
                   backend='django.contrib.auth.backends.ModelBackend')
        messages.success(
            request=request,
            message="Your account is activated, please login!")
        return render(request, 'index.html')
    else:
        messages.error(request=request, message="Activation link is invalid!")
        return redirect('/')


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    messages.success(request=request, message="You are logged out!")
    return redirect('index')


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        order = Order.objects.filter(customer=request.user)
        order_arrived = order.filter(state='Arrived')
        orders_count = order.count()
        context = {
            'order': order,
            'orders_count': orders_count,
            'order_arrived': order_arrived,

        }
        return render(request, 'dashboard.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request=request, user=user)
            messages.success(request=request, message="Login successful!")
        else:
            messages.error(request=request, message="Login failed!")
    context = {
        'email': email if 'email' in locals() else '',
        'password': password if 'password' in locals() else '',
    }
    return render(request, 'index.html', context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = UpdateProfileForm
    template_name = 'dash-edit-profile.html'
    success_url = reverse_lazy('dash-edit-profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.request.user.order_set.all()
        context['orders_count'] = context['orders'].count()
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        messages.success(self.request,
                         'Your profile has been updated successfully!')
        return super().form_valid(form)

    def get_object(self):
        return self.request.user
