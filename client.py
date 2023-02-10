import requests

# GET
response = requests.get('http://localhost:5050/api/v1/advs/').json()
print(response)

# POST
response = requests.post('http://localhost:5050/api/v1/advs/',
                         json={"author": "Test_author",
                               "title": "testtitle",
                               "description": "testdescription"})
print(response)

# GET по id
resp = requests.get('http://localhost:5050/api/v1/adv/1').json()
print(response)

# PUT по id
response = requests.put('http://localhost:5050/api/v1/adv/1',
                        json={"title": "testtitle", "description": "testdescription"})
print(response)

# DELETE по id
response = requests.delete('http://localhost:5050/api/v1/adv/3')
print(response)
