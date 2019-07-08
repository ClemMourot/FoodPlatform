from django.db import models
from django.forms import ModelForm

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'email', 'password']
        labels = {
            'username': 'Pseudo', 'name': 'Prénom', 'surname': 'Nom', 'password': 'Mot de passe',
        }




class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    tag = models.CharField(max_length=150, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.CharField(max_length=1)
    category = models.ManyToManyField(Category)
    image = models.ImageField(max_length=300)
    calories = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()
    proteins = models.FloatField()
    salt = models.FloatField()
    url = models.URLField(max_length=300)


class Substitute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.CharField(max_length=1)
    category = models.ManyToManyField(Category)
    user_id = models.ManyToManyField(User)




