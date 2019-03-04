"""1650 27/02/2019 this works"""

import threading
import serial #pip install pyserial
from d4_conversion_classes import Decoder

class ArduinoSerial:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyACM0",9600)
        self.ser.baudrate = 9600
        self.ser = serial.Serial("/dev/ttyACM0", self.ser.baudrate)
        self.decoder = Decoder()
        
        self.receive_toggle = False

    def get_data(self):
        print('Get data thread open')
        while self.receive_toggle:
            try:
                self.decoder.data_manipulation(self.ser.readline())
            except Exception as e:
                self.receive_toggle = False
                print('Try again!!')

    #socket command
    def stop_serial(self):
        self.ser.write(b'B')
        self.receive_toggle = False
        print('Serial communications end')

    #call from socket        
    def start_serial(self):
        print('Starting serial communications')
        if self.receive_toggle == False:
            self.receive_toggle = True
            self.ser.write(b'A')
            #might need to add self here
            receieve_thread = threading.Thread(target=self.get_data)
            receieve_thread.start()
        else:
            print('Already reading')
        
    #call from socket    
    def restart_serial(self):
        print('Restart Begin')
        if self.receive_toggle == True:
            self.stop_serial()
            self.start_serial()
        elif self.receive_toggle == False:
            self.start_serial()

