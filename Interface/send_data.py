import requests
import json
import time
import random

# Mock data
grip_data          = {'front_grip': 250, 'rear_grip': 100, 'bottom_grip': 300}
accelerometer_data = {'x_axis': 100, 'y_axis': 2033, 'z_axis': 300}
gyroscope_data     = {'x_axis': 150, 'y_axis': 203, 'z_axis': 400}

# Routes for POST requests
grip_url          = "http://localhost:3000/grip"
accelerometer_url = "http://localhost:3000/accelerometer"
gyroscope_url     = "http://localhost:3000/gyroscope"

def unit_test():
    # Testing is_dict():
    print('Testing is_dict() function...')
    print('Passing dict...')
    print(is_dict(grip_data))
    print('Passing not a dict...')
    print(is_dict(10))
    
    # Testing post():
    print('\nTesting send_data()...')
    # Send accelerometer_data
    print('Accelerometer')
    send_data(accelerometer_url, random_data(accelerometer_data))

    # Send grip_data
    print('Grip')
    send_data(grip_url, random_data(grip_data))
    
    # Send gyroscope_data
    print('Gyroscope')
    send_data(gyroscope_url, random_data(gyroscope_data))
    print('Success!')    

# Sends the data
def send_data(url, dict_data):
    if is_dict(dict_data) is True:
        try:
            requests.post(url, dict_data)
        except ValueError:
            print('Error during post request!')
    else: print('Data is not a dict!')

# Check if the data is of the dict type
def is_dict(dict_data):
    if type(dict_data) == dict:
        return True
    return False 

# Randomizes the data
def random_data(dict_data):
    if type(dict_data) is dict:
        for key in dict_data:
            dict_data[key] = dict_data[key] + random.randint(0,100) - 50
        return dict_data
    else: 
        print('Data is not a dict')
        return 1

if __name__ == '__main__':
    unit_test()


