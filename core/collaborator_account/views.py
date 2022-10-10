from importlib.resources import path
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from account.models import Profile
from account.forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os

# list collaborators (HTML index_collaborator)

@login_required
def index_collaborator(request):
    
    collaborator = Profile.objects.order_by('-id_collaborator')
    number_collaborator = collaborator.count()

    context = {
        'collaborators': collaborator,
        'collaborator_number': number_collaborator
    }

    return render(request, 'collaborator_account/index_collaborator.html', context)

# Personal data per employee (HTML data_collaborator)

@login_required
def data_collaborator(request, id):

    try:
        collaborator = Profile.objects.get(id_collaborator = id)
    
        id_collaborator = collaborator.id_collaborator
        firstname = collaborator.firstname
        lastname = collaborator.lastname
        email = collaborator.email
        username = collaborator.username
        street = collaborator.street
        number_street = collaborator.number_street
        zip_code = collaborator.zip_code
        town = collaborator.town
        country = collaborator.country
        prefix_gsm = str(collaborator.prefix_gsm)
        number_gsm = str(collaborator.gsm)
        gsm = prefix_gsm + number_gsm
        image = collaborator.image

        context = {
            "id_collaborator": id_collaborator,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "username": username,
            "street": street,
            "number_street": number_street,
            "zip_code": zip_code,
            "town": town,
            "country": country,
            "gsm": gsm,
            "image": image
        }

    except:
        return render(request, 'collaborator_account/index_collaborator.html', context)

    return render(request, 'collaborator_account/data_collaborator.html', context)

# Update collaborator

@login_required
def update_collaborator(request, id):

    profile_form = ProfileForm(request.POST or None)

    profile_form = Profile.objects.get(id_collaborator = id)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(profile_form.image) > 0:
                os.remove(profile_form.image.path)
                profile_form.image = request.FILES

        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_form)

        profile = profile_form.save(commit=False)
        profile.save()
        messages.success(request, 'Updated successfully')
        return redirect('index-collaborator')

    else:
        profile_form = ProfileForm(instance=profile_form)

    return render(request, "collaborator_account/update_collaborator.html", {'profile_form': profile_form})
    

# delete collaborator

@login_required
def delete_collaborator(request, id):
    
    collaborator = Profile.objects.get(id_collaborator = id)
    username = collaborator.username
    image = collaborator.image
    user_table = User.objects.all()    

    if username in user_table:
        image.delete()
        username.delete()
        return redirect('index-collaborator')

    else:
        return redirect('data-collaborator')

    return render(request, "collaborator_account/delete_collaborator.html", {'delete_username': delete_username})

# # Change password

# def password_change(request, id):

#     collaborator = Profile.objects.get(id_collaborator = id) 
#     collaborator.set_password('new password')
#     collaborator.save()

#     return render(request, "collaborator_account/index_collaborator.html")