from django.db import models
from django.contrib.auth.models import User


class Turf(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __str__(self):
        return f'{self.turf.name} - {self.user.username}'

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

