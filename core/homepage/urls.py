from django.urls import path, include
import sys
from . import views

sys.path.append(r'C:\Users\Utilisateur\Documents\Henri\L4D\always_there\test\core\blog_user')
sys.path.append(r'C:\Users\Utilisateur\Documents\Henri\L4D\always_there\test\core\collaborator_account')
sys.path.append(r'C:\Users\Utilisateur\Documents\Henri\L4D\always_there\test\core\user_account')
sys.path.append(r'C:\Users\Utilisateur\Documents\Henri\L4D\always_there\test\core\account')

import collaborator_account
import user_account
import blog_user.urls
import account.urls

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pageinconstruction/', views.in_construction, name='construction'),
    path('collaborator/', include('collaborator_account.urls')),
    path('user/', include('user_account.urls')),
    path('blog/', include('blog_user.urls')),
    path('account/', include('account.urls'))
]