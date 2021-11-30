import requests


# GET
api_url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(api_url)

for x,y in enumerate(response.headers):
    print(x,'.',y,':', response.headers[y])

# POST
print('\n\nPOST')
api_url = 'https://jsonplaceholder.typicode.com/todos'
todo = {"userid":1, "title":"Buy milk", "completed":False}

response = requests.post(api_url, json=todo)
print(response.json(),'\n\n')
