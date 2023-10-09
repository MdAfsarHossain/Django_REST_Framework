import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

# data = {    
#     'name': 'Afsar',
#     'roll': 101,
#     'city': 'CTG'
#     }
data = {    
    'name': 'Tarek',
    'roll': 102,
    'city': 'DHK'
    }
    
json_data = json.dumps(data)  # Convert python to json
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)

