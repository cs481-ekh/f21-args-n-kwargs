from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import UserPasswordResetForm, UserPasswordConfirmForm


urlpatterns = [
    # path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>',
         views.user_verification, name='activate'),

    # Password Reset Paths as_view() take a template as an argument to customized view
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html', form_class=UserPasswordResetForm),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', form_class=UserPasswordConfirmForm),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name="password_reset_complete"),
]
