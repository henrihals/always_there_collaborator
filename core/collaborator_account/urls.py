from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index_collaborator, name='index-collaborator'),
    #path('register/', views.register_collaborator, name='register-collaborator'),
    #path('login/', views.login_collaborator, name='login-collaborator'),
    path('data/<int:id>/', views.data_collaborator, name='data-collaborator'),
    path('update/<int:id>/', views.update_collaborator, name='update-collaborator'),
    path('delete/<int:id>/', views.delete_collaborator, name='delete-collaborator')
]