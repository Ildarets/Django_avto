from django.db import models
from django.contrib.auth.models import User
from usersapp.models import BlogUser



# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=16, unique=True)
    # user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mesto(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Avto(models.Model):
    price = models.PositiveIntegerField()
    vladeltsev = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    doors = models.PositiveIntegerField()
    complectation = models.CharField(max_length=50)
    box = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    modification = models.CharField(max_length=50)
    pokolenie = models.CharField(max_length=50)
    privod = models.CharField(max_length=50)
    probeg = models.PositiveIntegerField()
    rull = models.CharField(max_length=50)
    sostoyanie = models.CharField(max_length=50)
    type_engine = models.CharField(max_length=50)
    type_kyzov = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    cat_marka = models.ForeignKey(Marks, on_delete=models.CASCADE)
    cat_mesto = models.ForeignKey(Mesto, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='posts', null=True, blank=True)
    text = models.TextField()
    href = models.CharField(max_length=100)
    image_href_0 = models.CharField(max_length=50)
    image_href_1 = models.CharField(max_length=50)
    image_href_2 = models.CharField(max_length=50)

    def __str__(self):
        return self.model

    def has_image(self):
        return bool(self.image_href_0)


