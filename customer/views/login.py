
from django.dispatch import receiver
from django.views import View
from ..models import Customer
from ..form import RegistrationForm, UpdateProfileForm
from store.models import Notification
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View, UpdateView
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
                    message="Please confirm your email address to complete the registration"
                )
                return redirect('signup')
            except:
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


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Customer.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(
            request=request, message="Your account is activated, please login!")
        return render(request, 'index.html')
    else:
        messages.error(request=request, message="Activation link is invalid!")
        return redirect('/')


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    messages.success(request=request, message="You are logged out!")
    return redirect('index')

@login_required(login_url="signin")
class ProfileView(UpdateView):
    form_class = UpdateProfileForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user

