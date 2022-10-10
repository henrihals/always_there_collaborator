from django.urls import path, include

from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    path('register/collaborator', views.register_account_collaborator, name='register-account-collaborator'),
    path('login/', auth_view.LoginView.as_view(template_name='account/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='account/logout.html', next_page='login'), name='logout')
]