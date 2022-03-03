from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import uuid



class CustomUser(AbstractUser):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    def get_obsolute_url(self):
        pass