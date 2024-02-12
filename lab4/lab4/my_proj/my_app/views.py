from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def title_name(the_name: str):
    return the_name.lower()

def title_name(names:list):
    new_names = [x.title() for x in names]
    return new_names

class HomePageView(View):
    def get(self, request):

        my_name="RYAN"

        new_names = my_functions.title_name(my_name)

        theNames = ['RYAN','DONNA', 'HARVEY']

        otherNames = theNames
        theNames.append('HOWARD')

        new_names = [x.title() for x in theNames]

        car1 = my_objects.car('Toyota','Supra','2007','grey', 'honk wheeze')
        car2 = my_objects.car('KIA','Telluride','2024','pink', 'beep boop')
        motorcycle = my_objects.motorcycle('Indian','FTR','2015','Purple','VROOOOOOOOOOOOOM')

        context = {'hi':'HELLO PYTHON AND DJANGO!',
                   'name':new_names,
                    'namesList': new_names,
                    'car1':car1,
                    'car2':car2,
                    'motorcycle':motorcycle}

        return render(request, 'my_app/index.html', context)