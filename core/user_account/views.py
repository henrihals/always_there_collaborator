from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Index_user, Join_table_user
from .forms import IndexUserForm
from django.contrib.auth.decorators import login_required #Permet de bloquer les pages inaccessible sans login

# Create your views here.

# data user

@login_required
def data_user(request, id):

    try:
        user = Join_table_user.objects.get(id_user = id)
        profile = user.id_user

        context = {
            "id_user": profile.id_user,
            "creation_date" : profile.creation_date,
            "firstname" : profile.firstname,
            "lastname" : profile.lastname,
            #"password" : profile.password,
            "email" : profile.email,
            "street" : profile.street,
            "number_street" : profile.number_street,
            "zip_code" : profile.zip_code,
            "town" : profile.town,
            "country" : profile.country,
            "gsm" : str(profile.prefix_gsm) + str(profile.gsm),
        }

    except:
        return render(request, 'user_account/index_user.html', context)

    return render(request, 'user_account/data_user.html', context)

# list collaborators (HTML index_collaborator)

@login_required
def index_user(request):

    user = Index_user.objects.order_by('-id_user')
    user_number = user.count()

    context = {
        'index_users': user,
        'user_number': user_number
    }

    return render(request, 'user_account/index_user.html', context)

# register user

@login_required
def register_user(request):

    if request.method == 'POST':
        form = IndexUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-user')

    else:
        form = IndexUserForm()

    return render(request, 'user_account/register_user.html', {'form': form})

# Update user

@login_required
def update_user(request, id):

    id_user = Index_user.objects.get(id_user = id)

    if request.method == 'POST':
        form = IndexUserForm(request.POST, instance=id_user)
        if form.is_valid():
            form.save()
            return redirect('index-user')

    else:
        form = IndexUserForm(instance=id_user)

    return render(request, "user_account/update_user.html", {'form': form})

# delete user

@login_required
def delete_user(request, id):

    user = Index_user.objects.get(id_user = id)
    index = Index_user.objects.all()

    if user in index:
        user.delete()
        return redirect('index-user')

    else:
        return redirect('login-user')

    return render(request, "user_account/delete_user.html", {'user': user})