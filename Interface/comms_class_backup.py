"""1650 27/02/2019 this works"""

import threading
import requests
import time
import serial #pip install pyserial
from JQueue import JQueue #jacob made this
from d4_conversion_classes import decode_data


class ArduinoSerial:
    def __init__(self):
        self.grip_url          = "http://138.68.140.17/grip"
        self.accelerometer_url = "http://138.68.140.17/accelerometer"
        self.gyroscope_url     = "http://138.68.140.17/gyroscope"
        self.ser = serial.Serial("/dev/ttyACM0",9600)
        self.ser.baudrate = 9600
        self.get_toggle = False
        self.stop_toggle = False
        self.run = True
        threading.Thread(target=self.main_thread).start()
        self.data = JQueue()
        self.decoder = decode_data()
        
#thread holds for an input and does accordingly
    def main_thread(self):
        print('Main process begun')
        while self.run:
            command = raw_input("Insert the command (A, B, C or D)\n")
            self.get_toggle = False #need a better way of doing this otherwise duplicate commands will lead to a toggle of the toggles
            self.stop_toggle = False
            #self.toggle_all_false(self.get_toggle, self.stop_toggle) #assuming unique command every time
            if command == 'A':
                self.get_toggle = True
            elif command == 'B':
                self.stop_toggle = True
                #print(self.data.elements())
            elif command == 'quit':
                self.run = False
            elif command == 'C':
                pass
            elif command == 'D':
                pass
            elif command == 'E':
                pass
            else:
                print('Invalid command!')
            threading.Thread(target=self.process_thread).start()
      

    def process_thread(self):
        if self.get_toggle:
            self.ser.write(b'A')
            threading.Thread(target=self.get_data).start()
        elif self.stop_toggle:
            pass
        else:
            pass

    def get_data(self):
        while self.get_toggle:
            #print(self.ser.readline())
            (self.decoder).data_manipulation(self.ser.readline())
            print((self.decoder).interrupt)
            print((self.decoder).force_1)
            print((self.decoder).force_2)
            print((self.decoder).force_3)
            print((self.decoder).timestamp)
            #time.sleep(3)
            #data.add(self.ser.readline())
        self.stop_data()
	
    def send_data(self):
        # Code below will send the data if
        # self.queue is a list of dicitonaries
        #in the correct format
        #for data in self.queue:
        #   requests.post(self.accelerometer_url, data)
        pass

    def stop_data(self):
            self.ser.write(b'B')
            print('Serial communications end')
            
      
    def toggle_all_false(self, *argv):
        for arg in argv:
            arg = False			


if __name__ == "__main__":
    one = ArduinoSerial()

