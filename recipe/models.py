from django.db import models

# Create your models here.
class Burgers(models.Model):
    name = models.CharField(max_length= 100)
    price = models.FloatField(max_length=1000)
    details = models.CharField(max_length=1000)

class Pizzas(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=1000)
    details = models.CharField(max_length=1000)

class Toasts(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=1000)
    details = models.CharField(max_length=1000)

class Desserts(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=1000)
    details = models.CharField(max_length=1000)

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=1000)
    details = models.CharField(max_length=1000)

class Messages(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()

class Subscribers(models.Model):
     email = models.EmailField(null=True)