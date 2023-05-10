import requests

domain = 'gits.bj'
api_url = 'http://127.0.0.1:8000/api/twist?domain_name={}'.format(domain)
response = requests.get(api_url, headers={'X-Api-Key': 'MWrUl8kr.8YJlIZe8ZBuCkfJVXRI66ey2dPFsjFpY'}).json()
print(response)