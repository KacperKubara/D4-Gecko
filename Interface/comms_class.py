import threading
import time
import serial #pip install pyserial
from JQueue import JQueue #jacob made this


class ArduinoSerial:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyACM0",9600)
        self.ser.baudrate = 9600
        self.get_toggle = False
        self.stop_toggle = False
        self.run = True
        threading.Thread(target=self.main_thread).start()
        
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
            elif command == 'quit':
                self.run = False
            elif command == 'C'
                pass
            elif command == 'D'
                pass
            elif command == 'E'
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
            print(self.ser.readline())
            #time.sleep(3)
        self.stop_data()
	
    def stop_data(self):
            self.ser.write(b'B')
            print('Serial communications end')
            
      
    def toggle_all_false(self, *argv):
        for arg in argv:
            arg = False			


if __name__ == "__main__":
    one = ArduinoSerial()

