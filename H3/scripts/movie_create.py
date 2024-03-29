import requests
import json

api_url = 'http://localhost:8000/movie/create_api/'

movie_data = {
    "title" : "Title IX",
    "description" : "A movie about a lost boy in the wilderness",
    "director" : "Martin Scorsese",
    "release_year" : "1985",
    "budget" : "$750,000",
    "runtime" : "120 minutes",
    "rating" : "9",
    "genre" : "Thriller",
}

response = requests.post(url= api_url, data=json.dumps(movie_data),headers={'Content-Type':'application/json'})    

if response.status_code == 201:
    print('Customer created succesfully')
else:
    print(f'Error creating customer.')
    
