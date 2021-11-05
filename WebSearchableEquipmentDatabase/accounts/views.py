from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import Account

from .utils import account_activation_token
from .forms import AccountCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


def register(request):
    form = AccountCreationForm()
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = Account.objects.create(email=request.POST['email'])
            user.set_password(request.POST['password1'])
            user.is_active = False
            user.save()
            user_email = form.cleaned_data.get('email')
            current_site = get_current_site(request)
            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }

            link = reverse('activate', kwargs={'uidb64': email_body['uid'], 'token': email_body['token']})
            email_subject = 'Activate your account'
            activate_url = 'http://' + current_site.domain + link

            email = EmailMessage(
                email_subject,
                'Hello ' + user.email + ', Please the link below to activate your account \n' + activate_url,
                'noreply@semycolon.com',
                [user_email],
            )
            email.send(fail_silently=False)
            messages.success(
                request,
                'An email was sent to ' + str(user_email) + ' with instructions on how to activate your account.'
            )
            return redirect('login')

    content = {'form': form}
    return render(request, 'accounts/register.html', content)


def user_verification(request, uidb64, token):
    try:
        id = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=id)
        if user.is_active:
            return redirect('login')
        elif account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            email = user.email.split('@')[1]
            if email == 'u.boisestate.edu':
                group = Group.objects.get(name='student')
            elif email == 'boisestate.edu':
                group = Group.objects.get(name='faculty')
            else:
                group = Group.objects.get(name='guest')
            user.groups.add(group)
            messages.success(request, 'Account activated successfully')
            return redirect('login')
    except Exception as ex:
        pass
    return redirect('home')


def logout(request):
    django_logout(request)
    return redirect('home')
