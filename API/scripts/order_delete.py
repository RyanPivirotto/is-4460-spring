import requests

id = 2

api_url = f'http://localhost:8000/api/orders/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print('Order Deleted Success')
else:
    print('Error deleting Order')