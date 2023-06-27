import requests
import json

#GET запрос
status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status=available", headers={'accept': 'application/json'})
print(res.status_code, 'GET запрос')
print(res.json())

#POST запрос
new_pet = {
  "id": 9223372036854572002,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_p = requests.post(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(new_pet))
print(res_p.status_code, 'POST запрос')
print(res_p.json())

#DELETE запрос
res_d = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854572002', headers = {'accept': 'application/json'})
print(res_d.status_code, 'DELETE запрос')
print(res_d.json())

#PUT запрос
data = {
  "id": 9223372036854765198,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_put = requests.put(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(data))
print(res_put.status_code, 'PUT запрос')
print(res_put.json())

#Если в curl формат json, тогда надо прописать data = json.dumps()
#Другой вариант: json = {'id': 9223372036854765198, 'name': 'new_name', 'tags': []})
