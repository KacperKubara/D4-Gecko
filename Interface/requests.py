import requests
import json

grip_data          = {'front_grip': 250, 'rear_grip': 100, 'bottom_grip': 300}
accelerometer_data = {'x_axis': 100, 'y_axis': 2033, 'z_axis': 300}
gyroscope_data     = {'x_axis': 150, 'y_axis': 203, 'z_axis': 400}
# Routes for POST requests
grip_url          = "http://localhost:3000/grip"
accelerometer_url = "http://localhost:3000/accelerometer"
gyroscope_url     = "http://localhost:3000/gyroscope"

def post(json_data, url):   
    requests.post(url, json = json_data)

def jsonify(data):
    if type(data) == dict:
        return json.dumps(data)
    return "Error, argument is not a dictionary!"

if __name__ == '__main__':
    while True:
        print('Data')

