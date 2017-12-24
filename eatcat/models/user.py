from django.contrib.auth.models import AbstractUser
from django.db import models

from .pet import Pet


class User(AbstractUser):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, *kwargs)
