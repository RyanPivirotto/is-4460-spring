import requests

api_url = 'http://localhost:8000/api/customers/'

#test token success : a02ab0c405f569aac9bbfd46f91cb713894cf083
#test token fail: tapdifhasdofnaogih
token = 'tapdifhasdofnaogih'

headers = {
    'Authorization': f'Token {token}',
}

response = requests.get(api_url, headers=headers)

print(response.status_code)

if response.status_code==200:
    print(f'Customer retrieval successful.{response.text}')
else:
    print(f'Customer retrieval failed. {response.text}')