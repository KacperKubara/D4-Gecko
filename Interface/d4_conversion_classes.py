import time
import threading

class decode_data():
    def __init__(self):
        self.interrupt = 0
        self.force_1 = 0
        self.force_2 = 0
        self.force_3 = 0
        self.timestamp = 0
        self.queue = []
        self.t0 = time.time()
        threading.Thread(target=self.queue_length()).start()

    def decode_data(self,data):
        array = data.split(',')
        print(array)
        self.interrupt = array[0]
        self.force_1 = array[1]
        self.force_2 = array[2]
        self.force_3 = array[3]
        self.timestamp = time.time() - self.t0

    def queue_data(self):
        dictionary = {'front grip':self.force_1,'rear grip':self.force_2,'bottom grip':self.force_3,'timestamp':self.timestamp}
        (self.queue).append(dictionary)

    def dequeue_data(self):
        popped = (self.queue).pop(0)
        return popped

    def is_empty(self):
        if (self.queue):
            return False
        else:
            return True

    def interrupt_triggered(self):
        if self.interrupt == 0:
            return False
        else:
            return True
            
    def queue_length(self):
        while True:
            while not self.interrupt_triggered():
                if len(self.queue)!=0:
                    length = len(self.queue)
                    front_time = (self.queue[0])['timestamp']
                    back_time = (self.queue[length-1])['timestamp']
                    time_difference = (front_time - back_time)
                    if (time_difference >2.5):
                        self.dequeue_data()
            while self.interrupt_triggered():
                length = len(self.queue)
                front_time = (self.queue[0])['timestamp']
                back_time = (self.queue[length-1])['timestamp']
                time_difference = (front_time - back_time)
                if(time_difference >3):
                    print(self.queue)
                    self.interrupt_triggered = False
        
    
    def data_manipulation(self,data):
        self.decode_data(data)
        boolean = self.interrupt_triggered()
        self.queue_data()
        
if __name__ == '__main__':
    inst = decode_data()
    inst.data_manipulation('1,234,765,667')
    

