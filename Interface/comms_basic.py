import serial
from threading import Thread
import time

command = "C" # Initial Reset
# Setting up serial communication
ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600

##########################################
# some examples for python dictionaries
#gyroscope =[{ 'x-axis': 100, 'y-axis': 200, 'z-axis': 2000, 'timestamp': 'somestuffhere'}, { 'x-axis': 100, 'y-axis': 200, 'z-axis': 2000, 'timestamp': 'somestuffhere'}]
#gyroscope.append({ 'x-axis': 100, 'y-axis': 200, 'z-axis': 2000, 'timestamp': 'somestuffhere'})
#gyrscope[0]['x-axis'] # display 100
def format_data():
    pass
    
def update_database():
    pass

###########################################
def get_data():
    ser.write(b'A')
    try:
        while True:# Getting the data part 
            time.sleep(1)
            print(ser.readline())
    except KeyboardInterrupt:
        print('Stop reading the buffer')
        stop_data()
        
def stop_data():
    ser.write(b'B')
    
def reset():
    ser.write(b'C')
    
def configure_sensors():
    ser.write(b'D')

if __name__ == "__main__":
    while True:
        command = raw_input("Insert the command (A, B, C or D)\n")
        if command == "A": get_data()
        if command == "B": stop_data()
        if command == "C": reset()
        if command == "D": configure_sensors()
        else: command = "C"
        print(ser.readline())
        
