from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.CharField(max_length=50, blank=True, null=True)
    budget = models.CharField(max_length=50, blank=True, null=True)
    runtime = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=50, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
