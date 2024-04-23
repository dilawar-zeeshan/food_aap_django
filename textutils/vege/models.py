from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recipe(models.Model):
    User = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    rname = models.CharField(max_length=100)
    rdesc = models.TextField()
    rimg = models.ImageField(upload_to="recipe")
    rv_count = models.IntegerField(default=1)


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    st_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.st_id
