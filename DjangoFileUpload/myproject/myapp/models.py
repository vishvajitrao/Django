from django.db import models
from django.db.models import Manager
from django.urls import reverse

# Create your models here.


class ProfileUpload(models.Model):
    Profile = models.ImageField(upload_to='media')

class Document(models.Model):
    Doc = models.FileField(upload_to='docs/pdf/')

class Cars(models.Model):
    name = models.CharField(max_length=20)
    cars = models.FileField(upload_to='cars',null=True,blank=True)


class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Age = 21)




class MyDetails(models.Model):
    First_name = models.CharField("Enter first name: ", max_length=20)
    Last_name = models.CharField("Enter last name: ", max_length=20)
    Age = models.IntegerField("Enter your age",default=0)
    Phone_number = models.IntegerField("Enter your phone number here")
    obj = MyManager()
    objects = Manager()

    def __str__(self):
        return self.First_name



class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('Registration')


    
    
