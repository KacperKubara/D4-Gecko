import requests
import json
import time 
grip_data          = {'front_grip': 250, 'rear_grip': 100, 'bottom_grip': 300}
accelerometer_data = {'x_axis': 100, 'y_axis': 2033, 'z_axis': 300}
gyroscope_data     = {'x_axis': 150, 'y_axis': 203, 'z_axis': 400}
# Routes for POST requests
grip_url          = "http://localhost:3000/grip"
accelerometer_url = "http://localhost:3000/accelerometer"
gyroscope_url     = "http://localhost:3000/gyroscope"

def post(data, url):
    if is_dict(data) == True:
        json_data = jsonify(data)   
        requests.post(url, data = json_data)
    else: print('Error, data not a dictionary!')    
    
def is_dict(data):
    if type(data) == dict:
        return True
    return False 

def jsonify(data):
    return json.dumps(data)
 
if __name__ == '__main__':
    for i in range (0, 3):
        # Send accelerometer mock data
        time.sleep(1)
        post(accelerometer_data, accelerometer_url)

        # Send grip mock data
        time.sleep(1)
        post(grip_data, grip_url)

        # Send gyroscope mock data
        time.sleep(1)
        post(gyroscope_data, gyroscope_url)



