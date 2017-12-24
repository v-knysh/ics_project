from django.db import models
# from eatcat.models import User
from django.contrib.auth.models import User


# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    weight = models.FloatField()
    age = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # def __init__(self, name, weight, age, owner=None, *args, **kwargs):
    #     super(Pet, self).__init__(*args, *kwargs)
    #     self.name = name
    #     self.weight = weight
    #     self.age = age
    #     self.owner = owner


    # def __str__(self):
    #     return f"Pet {self.name}"
    #
    # def __repr__(self):
    #     return f"Pet {self.name}"