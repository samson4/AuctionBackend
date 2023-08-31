from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import geocoder

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    # location = models.TextField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.username