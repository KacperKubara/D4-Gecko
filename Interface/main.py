import threading
import time
from JQueue import JQueue


class ArduinoSerial:
    def __init__(self):
        self.ser = 'thf'
        self.command_queue = JQueue()
        self.get_toggle = False
        self.run = True
        threading.Thread(target=self.main_thread).start()
        threading.Thread(target=self.output_thread).start()

    def main_thread(self):
        print('thread 1')
        while self.run:
            command = input() #raw_input on pi
            self.command_queue.add(str(command))
            if command == 'A':
                self.get_toggle = True
            elif command == 'quit':
                self.run = False
            else:
                self.get_toggle = False

    def output_thread(self):
        print('thread 2')
        while self.run:
            if self.get_toggle:
                self.do_something()
            time.sleep(5)

    def do_something(self):
        print('out')


if __name__ == "__main__":
    one = ArduinoSerial()

