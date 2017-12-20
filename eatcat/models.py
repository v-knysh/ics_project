from django.db import models

# Create your models here.

class Cat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"Cat {self.name}"

    def __repr__(self):
        return f"Cat {self.name}"