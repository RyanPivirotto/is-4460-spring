from django import forms
from .models import Movie, Role, User

class MovieForm(forms.modelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class UserForm(forms.modelForm):
    class Meta:
        model = User
        fields = '__all__'

class RoleForm(forms.modelForm):
    class Meta:
        model = Role
        fields = '__all__'