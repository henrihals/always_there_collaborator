from django.urls import path, include
import sys
from . import views

#sys.path.append(r'C:\Users\Utilisateur\Documents\Henri\L4D\always_there\always_there_collaborator\core\blog_user')

#import blog_user.urls

urlpatterns = [
    path('index/', views.index_user, name='index-user'),
    path('register/', views.register_user, name='register-user'),
    path('data/<int:id>/', views.data_user, name='data-user'),
    path('update/<int:id>/', views.update_user, name='update-user'),
    path('delete/<int:id>/', views.delete_user, name='delete-user'),
    #path('blog/', include ('blog_user.urls'))
]