from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BlogUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not Profile.objects.filter(user = self).exists():
            Profile.objects.create(user = self)


class Profile(models.Model):
    info = models.TextField(blank=True)
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)

