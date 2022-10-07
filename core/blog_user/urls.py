from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.index_blog, name='index-blog-user'),
    path('newpost/', views.new_post_blog, name='new-post-user'),
    path('article/<int:id>/', views.data_article_blog, name='data-article-user'),
    path('update/<int:id>/', views.update_article_blog, name='update-article-user'),
    path('delete/<int:id>/', views.delete_article_blog, name='delete-article-user')
    #path('<int:id>/', views.data_user, name='data-user'),
    #path('<int:id_user>/', include ('mail.urls'))
]