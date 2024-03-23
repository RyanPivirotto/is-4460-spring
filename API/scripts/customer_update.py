import requests
import json

id = 3

api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data = {
    "name" : "Ryan Pivirotto",
    "email" : "rpivirotto@example.com",
    "phone_number" : "8015556666"
}

response = requests.put(api_url, data=json.dumps(customer_data), headers={'Content-Type': 'application/json'})

if response.status_code==200:
    print('Customer Updated Success')
else:
    print('error updating')