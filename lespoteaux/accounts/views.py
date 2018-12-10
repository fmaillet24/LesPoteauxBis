from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage


from .forms import LoginForm, RegisterForm
from .tokens import account_activation_token

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm()

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
            else:
                messages.error(request, "Erreur")
                return redirect('pronostics:dashboard')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_n = form.cleaned_data['first_name']
            last_n = form.cleaned_data['last_name']
            password = form.cleaned_data['confirm']

            if User.objects.filter(username=username).exists():
                messages.error(request, "L'utilisateur existe deja.")
                return redirect('accounts:login')
            else:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=first_n,
                    last_name=last_n
                )
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = "Active ton compte."
                message = render_to_string('accounts/active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                send_email = EmailMessage(
                    mail_subject, message, to=[email]
                )
                send_email.send()
                messages.error(request,
                               "Ca y est... Tu es presque un poteau, \
                               il ne te reste plus qu'a confirmer ton email \
                               avec le lien que nous t'avons transmis.")
        else:
            return redirect('accounts:register')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def active(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        user.is_active = True
        user.save()
        messages.error(request, "Merci, Vous pouvez maintenant vous connecter")
        return redirect('accounts:login')
    else:
        return HttpResponse('Activation link is invalid!')
