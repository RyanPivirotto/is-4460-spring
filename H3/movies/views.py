from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Movie, Role, User
from .forms import MovieForm, UserForm, RoleForm

# Create your views here.
class MovieList(View):
    def get(self,request):
        Movies = Movie.objects.all()
        return render(request= request,template_name = 'movies/move_list.html',context={'movies':Movies})
