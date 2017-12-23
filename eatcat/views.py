import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.template import loader


from eatcat.models.pet import Pet


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def pets_list(request):
    pets = list(Pet.objects.all())
    return HttpResponse(json.dumps(pets, default=lambda o: o.__dict__, sort_keys=True, indent=4))


def pet_info(request, pet_id):
    pet = Pet.objects.filter(id__exact=pet_id).first()
    return HttpResponse(json.dumps(pet, default=lambda o: o.__dict__, sort_keys=True, indent=4))


def users_list(request):
    users = list(User.objects.all())
    return HttpResponse(json.dumps(users , default=lambda o: o.__dict__, sort_keys=True, indent=4))


def user_info(request, pet_id):
    user = User.objects.filter(id__exact=pet_id).first()
    return HttpResponse(json.dumps(user, default=lambda o: o.__dict__, sort_keys=True, indent=4))



def auth(request):
    print(request.method)
    pass
    if request.method == 'POST':
        post_data = {}
        user = authenticate(username=post_data['username'], password=post_data['password'])
        if user is not None:
            pass
    else:
        return HttpResponse(json.dumps())
