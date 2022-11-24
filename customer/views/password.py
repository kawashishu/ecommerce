
from multiprocessing import context
from django.shortcuts import redirect, render
from django.views import View
from ..models import Customer
from ..form import RegistrationForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class PasswordView(View):
    model = Customer

    def post(self, request):
        try:
            email = request.POST['email']
            user = Customer.object.get(email__exact=email)
            current_site = get_current_site(request=request)
            mail_subject = 'Reset your blog account.'
            message = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            send_email = EmailMessage(mail_subject, message, to=[email])
            send_email.send()
            messages.success(
                request=request,
                message="Please check your email to reset your password"
            )
        except:
            messages.error(request=request, message="Email does not exist")
            return redirect('register')
        finally:
            form = RegistrationForm()
            context = {
                'form': form,
                'email': email.split('@')[0] if 'email' in locals() else '',
            }
            return render(request, 'forgot_password.html', context)

def forgotPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            user = Customer.objects.get(email__exact=email)
            
            current_site = get_current_site(request=request)

            mail_subject = 'Reset your password'
            message = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            send_email = EmailMessage(mail_subject, message, to=[email])
            
            send_email.send()
            
            messages.success(
                request=request, message="Password reset email has been sent to your email address")

    except Exception:
        messages.error(request=request, message="Account does not exist!")
    finally:
        form = RegistrationForm()
        context = {
            'form': form,
            'email': email.split('@')[0] if 'email' in locals() else '',
        }
        return render(request, "forgot_password.html", context=context)




def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Customer.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request=request, message='Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request=request, message="This link has been expired!")
        return redirect('register')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Customer.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, message="Password reset successful!")
            return redirect('register')
        else:
            messages.error(request, message="Password do not match!") 
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'reset_password.html', context)

