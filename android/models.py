from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    balance = models.IntegerField(default=0)

class Categories(models.Model):
    title = models.CharField(max_length=40)
    images = models.CharField(max_length=40)

# class Limitations(models.Model):
#     money = models.DecimalField(max_digits=10, decimal_places=2)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
#
# class AddExpenditure(models.Model):
#     money = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(default=datetime.now)
#     description = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
#
# class AddIncome(models.Model):
#     money = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(default=datetime.now)
#     description = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Planing(models.Model):
    zdor = models.IntegerField(default=0)
    home = models.IntegerField(default=0)
    cafe = models.IntegerField(default=0)
    dosug = models.IntegerField(default=0)
    obraz = models.IntegerField(default=0)
    podar = models.IntegerField(default=0)
    product = models.IntegerField(default=0)
    tochki = models.IntegerField(default=0)
    plan_balance = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CategExp(models.Model):
    zdor = models.IntegerField(default=0)
    home = models.IntegerField(default=0)
    cafe = models.IntegerField(default=0)
    dosug = models.IntegerField(default=0)
    obraz = models.IntegerField(default=0)
    podar = models.IntegerField(default=0)
    product = models.IntegerField(default=0)
    tochki = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ExpInc(models.Model):
    money = models.IntegerField(null=True)
    date = models.DateField(null=True)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    categori = models.CharField(max_length=40, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)