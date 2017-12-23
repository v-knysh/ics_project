import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render

from eatcat.models.pet import Pet




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

