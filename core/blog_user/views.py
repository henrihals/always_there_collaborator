from multiprocessing import context
from django.shortcuts import render, redirect

from .forms import IndexBlogUserForm
from .models import Index_blog_user

from django.contrib.auth.decorators import login_required #Permet de bloquer les pages inaccessible sans login

# Create your views here.

# list article blog

@login_required
def index_blog(request):

    list_article_blog = Index_blog_user.objects.all()
    number_article_blog = list_article_blog.count()

    count_article = f'{number_article_blog} articles.'

    if number_article_blog == 1:
        count_article = f'{number_article_blog} article.'

    context = {
        'list_article_blogs': list_article_blog,
        'count_article': count_article
    }

    return render(request, "blog_user/index_blog.html", context)

# add new article

@login_required
def new_post_blog(request):
    
    if request.method == 'POST':
        form = IndexBlogUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-blog-user')

    else:
        form = IndexBlogUserForm()

    return render(request, "blog_user/new_post_blog.html", {'form': form})

# Get data article blog

@login_required
def data_article_blog(request, id):

    try:
        article = Index_blog_user.objects.get(id_blog = id)
        id_blog = article.id_blog
        creation_date = article.creation_date
        title = article.title
        content_blog = article.content_blog

        context = {
            "id_blog": id_blog,
            "creation_date": creation_date,
            "title": title,
            "content_blog": content_blog
            }

    except:
        return render(request, 'blog_user/index_blog.html', context)

    return render(request, "blog_user/data_article_blog.html", context)

@login_required
# Update article blog

def update_article_blog(request, id):

    id_blog = Index_blog_user.objects.get(id_blog = id)

    if request.method == 'POST':
        form = IndexBlogUserForm(request.POST, instance=id_blog)
        if form.is_valid():
            form.save()
            return redirect('index-blog-user')

    else:
        form = IndexBlogUserForm(instance=id_blog)

    return render(request, "blog_user/update_article_blog.html", {'form': form})

# Delete article blog

@login_required
def delete_article_blog(request, id):
    
    article = Index_blog_user.objects.get(id_blog = id)
    index = Index_blog_user.objects.all()

    if article in index:
        article.delete()
        return redirect('index-blog-user')

    else:
        return redirect('login-collaborator')

    return render(request, "blog_user/delete_article_blog.html", {'article': article})