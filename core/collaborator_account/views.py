from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Index_collaborator, Join_table
from .forms import IndexCollaboratorForm
from django.contrib.auth.decorators import login_required #Permet de bloquer les pages inaccessible sans login

# Create your views here.

#  login collaborator 

@login_required
def login_collaborator(request):
        return render(request, "collaborator_account/login_collaborator.html")

# Personal data per employee (HTML data_collaborator)

@login_required
def data_collaborator(request, id):

    try:
        collaborator = Join_table.objects.get(id_collaborator = id)
        profile = collaborator.id_collaborator

        context = {
            "id_collaborator" : profile.id_collaborator,
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
        return render(request, 'collaborator_account/index_collaborator.html', context)

    return render(request, 'collaborator_account/data_collaborator.html', context)

# list collaborators (HTML index_collaborator)

@login_required
def index_collaborator(request):
        
    collaborator = Index_collaborator.objects.all()
    collaborator_number = collaborator.count()

    context = {
        'index_collaborators': collaborator,
        'collaborator_number': collaborator_number
    }

    return render(request, 'collaborator_account/index_collaborator.html', context)

# register collaborator

@login_required
def register_collaborator(request):

    if request.method == 'POST':
        form = IndexCollaboratorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-collaborator')

    else:
        form = IndexCollaboratorForm()

    return render(request, 'collaborator_account/register_collaborator.html', {'form': form})

# Update collaborator

@login_required
def update_collaborator(request, id):

    id_collaborator = Index_collaborator.objects.get(id_collaborator = id)

    if request.method == 'POST':
        form = IndexCollaboratorForm(request.POST, instance=id_collaborator)
        if form.is_valid():
            form.save()
            return redirect('index-collaborator')

    else:
        form = IndexCollaboratorForm(instance=id_collaborator)

    return render(request, "collaborator_account/update_collaborator.html", {'form': form})

# delete collaborator

@login_required
def delete_collaborator(request, id):
    
    collaborator = Index_collaborator.objects.get(id_collaborator = id)
    index = Index_collaborator.objects.all()

    if collaborator in index:
        collaborator.delete()
        return redirect('index-collaborator')

    else:
        return redirect('login-collaborator')

    return render(request, "collaborator_account/delete_collaborator.html", {'collaborator': collaborator})