from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hero(models.Model):

    name = models.CharField(max_length=100)
    secret_identity = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    abilities = models.CharField(max_length=200)
    affiliations = models.TextField(max_length=500)
    villains = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Villain(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    abilities = models.CharField(max_length=200)
    affiliations = models.TextField(max_length=500)
    nemesis = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='hero')

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']


class HeroTeam(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default='https://cdn.europosters.eu/image/1300/posters/dc-comics-rebirth-i80856.jpg')
    heroes = models.ManyToManyField(Hero)

    def __str__(self):
        return self.name

class VillainTeam(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default='https://cdn.europosters.eu/image/1300/posters/dc-comics-rebirth-i80856.jpg')
    villains = models.ManyToManyField(Villain)

    def __str__(self):
        return self.name
