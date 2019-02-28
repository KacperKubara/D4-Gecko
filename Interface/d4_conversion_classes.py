import time
import threading
import requests

class Decoder():
    def __init__(self):
        self.grip_url          = "http://138.68.140.17/grip"
        self.accelerometer_url = "http://138.68.140.17/accelerometer"
        self.gyroscope_url     = "http://138.68.140.17/gyroscope"
        self.interrupt = 0
        self.force_1 = 0
        self.force_2 = 0
        self.force_3 = 0
        self.timestamp = 0
        self.queue = []
        threading.Thread(target=self.queue_length).start()

    def data_manipulation(self, data):
        self.decode_data(data)
        boolean = self.interrupt
        self.queue_data()
    
    def decode_data(self, data):
        array = data.split(',')
        self.interrupt = int(array[0])
        self.force_1   = int(array[1])
        self.force_2   = int(array[2])
        self.force_3   = int(array[3])
        self.timestamp = time.time()

    def queue_data(self):
        dictionary = {'front_grip': self.force_1, 'rear_grip': self.force_2,
                      'bottom_grip': self.force_3, 'timestamp': self.timestamp}
        (self.queue).append(dictionary)
        #print(dictionary)

    def dequeue_data(self):
        popped = (self.queue).pop(0)
        return popped

    def is_empty(self):
        if (self.queue):
            return False
        else:
            return True
            
    def send_data(self):
        formatted_data = {}
        for data in self.queue:
            formatted_data['front_grip']  = data['front_grip']
            formatted_data['rear_grip']   = data['rear_grip']
            formatted_data['bottom_grip'] = data['bottom_grip']
            requests.post(self.grip_url, formatted_data)
        
    def queue_length(self):
        while True:
            # print('queue_length(): '+ str(self.interrupt))
            while self.interrupt == 0:
                print('interrupt == 0')
                time.sleep(0.2)
                if len(self.queue) >= 2:
                    length = len(self.queue)
                    front_time = (self.queue[length-1])['timestamp']
                    back_time = (self.queue[0])['timestamp']
                    time_difference = (front_time - back_time)
                    print('time difference: ' + str(time_difference))
                    if (time_difference > 2.5):
                        self.dequeue_data()
            while self.interrupt == 1:
               if len(self.queue) >= 2: 
                    time.sleep(0.2)               
                    print('interrupt == 1')
                    length = len(self.queue)
                    front_time = (self.queue[length-1])['timestamp']
                    back_time = (self.queue[0])['timestamp']
                    time_difference = (front_time - back_time)
                    print('time difference: ' + str(time_difference))
                    if(time_difference > 3):
                        print('SENDING DATA...')
                        print(self.queue)
                        self.send_data()
                        print('DATA HAS BEEN SENT!')

                        self.interrupt = False 
                        self.queue = [] # Empty the queue



if __name__ == '__main__':
    inst = Decoder()
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('1,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('1,234,765,667')
    time.sleep(0.5)    
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
    time.sleep(0.5)
    inst.data_manipulation('0,234,765,667')
