import random
from django.contrib.auth.models import AbstractUser
from django.db import models


def random_int():
    return random.randint(1, 100)


class MiloUser(AbstractUser):
    birthday = models.DateField(null=True)
    random = models.IntegerField(editable=False, default=random_int)
