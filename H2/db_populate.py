# db_populate.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'H2.settings')
django.setup()

from movies.models import Movie, User

# Empty all existing rows from the tables
Movie.objects.all().delete()
User.objects.all().delete()

# Add 10 movie rows
for i in range(10):
    movie = Movie.objects.create(
        title=f"Movie {i+1}",
        description=f"Description for Movie {i+1}",
        director=f"Director {i+1}",
        release_year=f"202{i}",
        budget=f"Budget {i+1}",
        runtime=f"Runtime {i+1}",
        rating=f"Rating {i+1}",
        genre=f"Genre {i+1}"
    )

# Add 3 user rows
for i in range(3):
    user = User.objects.create(
        username=f"user{i+1}",
        password=f"password{i+1}",
        first_name=f"First Name {i+1}",
        last_name=f"Last Name {i+1}",
        email=f"user{i+1}@example.com"
    )

# Write Django QuerySet statements for Movie
all_movies = Movie.objects.all()

# Filter movies starting with "Movie"
movies_starting_with_text = Movie.objects.filter(title__startswith='Movie')
one_movie = Movie.objects.first() 
if one_movie:
    # Update one movie
    one_movie.title = "New Title"
    one_movie.save()

# Write Django model statements for User model
def get_user_data(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None
