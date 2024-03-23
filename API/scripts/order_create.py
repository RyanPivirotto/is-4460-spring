import requests
import json

api_url = 'http://localhost:8000/api/orders/'

customer_id = 4

order_data = {
    "customer" : customer_id,
    "total_price": "255.90"
}

response = requests.post(api_url, data=json.dumps(order_data),headers={'Content-Type':'application/json'})    

if response.status_code == 201:
    print('Order created succesfully')
else:
    print(f'Error creating Order.')
