#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-21 15:57:51
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-21 15:57:51
@Description:
"""
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, FormView, DetailView
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm
from .models import UserProfile

# Create your views here.

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = "/"
        kwargs['redirect_to'] = redirect_to

        return super(LoginView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)

        if form.is_valid():
            auth.login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        else:
            return self.render_to_response({'form': form})

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=[self.request.get_host()]):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(RedirectView):
    url = "/login/"

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(False)
            if UserProfile.objects.filter(email=user.email):
                form._errors['email_exists'] = '* 该邮件地址已被使用'
                return self.render_to_response({'form': form})
            user.save(True)
            url = reverse('users:login')
            return HttpResponseRedirect(url)
        else:
            return self.render_to_response({'form': form})

    
class MyPasswordChangeView(PasswordChangeView):
    pass


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'users/userprofile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class MyPasswordResetView(PasswordResetView):
    pass