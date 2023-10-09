import requests

URL = "http://127.0.0.1:8000/stuinfo/1"

r = requests.get(url = URL)
data = r.json()

print(data)


#AfsarHossain@DESKTOP-72CVEAH MINGW64 /d/.bew/Django/Geeky Shows/Django REST Framework (DRF)/gs1     
#$ py myapp.py