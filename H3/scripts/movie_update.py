import requests
import json

id = 8

api_url = f'http://localhost:8000/movie/create_api/{id}/'

movie_data = {
    "title" : "Title 8",
    "description" : "A movie about a lost boy in the wilderness",
    "director" : "Martin Scorsese",
    "release_year" : "1988",
    "budget" : "$950,000",
    "runtime" : "130 minutes",
    "rating" : "9.5",
    "genre" : "Thriller",
}

response = requests.put(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code==200:
    print('Movie Updated Success')
else:
    print('error updating')