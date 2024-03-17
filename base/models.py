from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator



class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to='provider_profile_photos/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone_number = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, )
    categories = models.ManyToManyField('Category', blank=True)
    description_small = models.TextField(null=True, blank=True)
    description_big = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name



class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(
        upload_to='category_icons/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(Provider, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
