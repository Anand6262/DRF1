import requests
URL="http://127.0.0.1:8000/stuinfo/8"
x=requests.get(url=URL) #We can write anything in the place of x
data=x.json()
print(data)