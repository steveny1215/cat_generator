import requests
import urllib.request
import os

response = requests.get('https://aws.random.cat/meow')

#print(response.status_code) #Response<200> -> Working
#print(response.json()) #returns a new dictionary
cat = response.json()
print(cat["file"]) #generate link to a random cat image
link = cat["file"]
savein='cat.jpg'
#save randomly generated cat picture into cat.jpg

try:
    urllib.request.urlretrieve(cat["file"],savein) 
except:
    print('Network Issue')