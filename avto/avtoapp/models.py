from django.db import models

# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Mesto(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Avto(models.Model):
    price = models.PositiveIntegerField()
    vladeltsev = models.TextField()
    year = models.PositiveIntegerField()
    doors = models.PositiveIntegerField()
    complectation = models.TextField()
    box = models.TextField()
    model = models.TextField()
    modification = models.TextField()
    pokolenie = models.TextField()
    privod = models.TextField()
    probeg = models.PositiveIntegerField()
    rull = models.TextField()
    sostoyanie = models.TextField()
    type_engine = models.TextField()
    type_kyzov = models.TextField()
    color = models.TextField()
    cat_marka = models.ForeignKey(Marks, on_delete=models.CASCADE)
    cat_mesto = models.ForeignKey(Mesto, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.model


