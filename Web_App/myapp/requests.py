import requests

grip_url          = http://localhost:3000/grip
accelerometer_url = http://localhost:3000//accelerometer
gyroscope_url     = http://localhost:3000/gyroscope

def post(json_data, url):   
    requests.post(url, json = json_data)
