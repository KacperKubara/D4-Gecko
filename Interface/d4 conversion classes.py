class decode_data():
    def __init__(self):
        self.interrupt = 0
        self.force_1 = 0
        self.force_2 = 0
        self.force_3 = 0
        self.timestamp = 0
        self.queue = []

    def decode_data(self,data):
        array = data.split(',')
        self.interrupt = int(array[0])
        self.force_1 = array[1]
        self.force_2 = array[2]
        self.force_3 = array[3]
        self.timestamp = 0

    def queue_data(self):
        dictionary = {'grip 1':self.force_1,'grip 2':self.force_2,'grip 3':self.force_3,'timestamp':self.timestamp}
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

    def data_manipulation(self,data):
        self.decode_data(data)
        boolean = self.interrupt_triggered()
        print(boolean)
        self.queue_data()
        popped = inst.dequeue_data()
        print(popped)
        
if __name__ == '__main__':
    inst = decode_data()
    inst.data_manipulation('1,234,765,667')

