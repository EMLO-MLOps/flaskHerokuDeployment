import requests

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('doggo.jpeg', 'rb')})

print(resp.text)
