from django.shortcuts import render
from django.http import HttpResponse
import json

from eatcat.models import Cat
# Create your views here.

def cats_list(request):
    cats = [Cat(f"Cat{i}", 5+i/2)for i in range(10)]
    return HttpResponse(json.dumps(cats, default=lambda o: o.__dict__, sort_keys=True, indent=4))

def cat_info(request, cat_id):
    cat = Cat(f"Cat{cat_id}", 5+cat_id/2)
    return HttpResponse(json.dumps(cat, default=lambda o: o.__dict__, sort_keys=True, indent=4))