from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import auth
from django.conf import settings
from authapp.models import User
from authapp.forms import UserLoginForm, UserEditForm, UserRegisterForm


def authentication(request):
    title = 'Вход'
    login_form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))


def profile(request):
    title = 'Профиль'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('mainapp:main'))

    edit_form = UserEditForm(instance=request.user)
    content = {
        'title': title, 'edit_form': edit_form, 'media_url': settings.MEDIA_URL
    }
    return render(request, 'authapp/edit_profile.html', content)


def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)
