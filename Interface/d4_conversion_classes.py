import time
import threading


class Decoder():
    def __init__(self):
        self.interrupt = 0
        self.force_1 = 0
        self.force_2 = 0
        self.force_3 = 0
        self.timestamp = 0
        self.queue = []
        threading.Thread(target=self.queue_length).start()

    def decode_data(self, data):
        array = data.split(',')
        self.interrupt = int(array[0])
        self.force_1   = int(array[1])
        self.force_2   = int(array[2])
        self.force_3   = int(array[3])
        self.timestamp = time.time()

    def queue_data(self):
        dictionary = {'front grip': self.force_1, 'rear grip': self.force_2,
                      'bottom grip': self.force_3, 'timestamp': self.timestamp}
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

    def queue_length(self):
        while True:
            # print('queue_length(): '+ str(self.interrupt))
            while self.interrupt == 0:
                print('interrupt == 0')
                if len(self.queue) >= 2:
                    length = len(self.queue)
                    front_time = (self.queue[0])['timestamp']
                    back_time = (self.queue[length-1])['timestamp']
                    time_difference = (front_time - back_time)
                    if (time_difference > 2.5):
                        self.dequeue_data()
            while self.interrupt == 1:
               if len(self.queue) >= 2:                
                    print('interrupt == 1')
                    length = len(self.queue)
                    front_time = (self.queue[0])['timestamp']
                    back_time = (self.queue[length-1])['timestamp']
                    time_difference = (front_time - back_time)
                    if(time_difference > 3):
                        print(self.queue)
                        self.interrupt = False

    def data_manipulation(self, data):
        self.decode_data(data)
        boolean = self.interrupt
        self.queue_data()


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