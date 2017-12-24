import json

from django.http import HttpResponse,JsonResponse
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
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            return JsonResponse({'pk':user.pk, 'username':user.username})
        else:
            return JsonResponse({'msg':'Такого користувача не існує'}, status=500)
    else:
        return JsonResponse({'msg':'Problem'}, status=500)

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.all().values_list('username', flat=True)
        if username in user:
            return JsonResponse({'msg':'Такий користувач вже існує'}, status=500)
        else:
            User.objects.create_user(username=username, password=password)
            return JsonResponse({'ok':'ok'})

def dashboard(request):
    # user = User.objects.get(pk=)
    return JsonResponse({'ok':'ok'})