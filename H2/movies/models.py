from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.CharField(max_length=50, blank=True, null=True)
    budget = models.CharField(max_length=50, blank=True, null=True)
    runtime = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=50, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} - {self.role}"
