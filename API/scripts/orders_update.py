import requests
import json

id = 2


api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {
    "customer" : 4,
    'total_price': '500.50'
    
}

response = requests.put(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code==200:
    print('Order Updated Success')
else:
    print('error updating')
    print(response.content)