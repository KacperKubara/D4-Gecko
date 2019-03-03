import time
import threading
import requests

buffer_lock = threading.Lock()


class Decoder:
    def __init__(self):
        self.grip_url = "http://138.68.140.17/grip"
        self.accelerometer_url = "http://138.68.140.17/accelerometer"
        self.interrupt = 0
        self.interrupt_triggered = 0
        self.buffer = []
        threading.Thread(target=self.buffer_manager).start()

    # on call adds data to list in dictionary format
    def data_manipulation(self, data):
        # decoding data received from the pi
        data_input = data.split(',')
        # the value in there should be parameterised in case we measure more
        # changes all values in the array to int or float and ensures that there are seven elements
        for i in range(7):
            try:
                data_input[i] = self.from_string_to_float(data_input[i])
            except IndexError:
                data_input.append(0)

        if data_input.pop(0) == 1:
            self.interrupt_triggered = True
        # create dictionary and add to list
        dictionary = {'front_grip': data_input[0], 'rear_grip': data_input[1],
                      'bottom_grip': data_input[2], 'timestamp': time.time(),
                      'x_axis': data_input[3], 'y_axis': data_input[4], 'z_axis': data_input[5]}
        self.buffer.append(dictionary)

        #print('Queue: ')
        #print(self.queue)
        print('Queue length:' + str(len(self.buffer)))

    def from_string_to_float(self, value):
        try:
            try:
                return int(value)
            except ValueError:
                print('Value error')
                return float(value)
        except ValueError: # error id: could not convert string to float
            temp = list(value)
            for i, element in enumerate(temp):
                try:
                    if element is not '.':
                        int(element)
                except Exception as e:
                    temp[i] = '0'
            return float("".join(temp))

    def send_data(self, buffer):
        grip_sensor_data_dict = {}
        accelerometer_data_dict = {}
        for element in buffer:
            grip_sensor_data_dict['front_grip'] = element['front_grip']
            grip_sensor_data_dict['rear_grip'] = element['rear_grip']
            grip_sensor_data_dict['bottom_grip'] = element['bottom_grip']
            accelerometer_data_dict['x_axis'] = element['x_axis']
            accelerometer_data_dict['y_axis'] = element['y_axis']
            accelerometer_data_dict['z_axis'] = element['z_axis']
            requests.post(self.grip_url, grip_sensor_data_dict)
            requests.post(self.accelerometer_url, grip_sensor_data_dict)
        
    def buffer_manager(self):
        while True:
            # print('queue_length(): '+ str(self.interrupt))
            while self.interrupt_triggered == 0:
                # print(self.queue)
                # eh
                time.sleep(0.2)
                if len(self.buffer) > 1:
                    # print('interrupt == 0')
                    front_time = (self.buffer[len(self.buffer) - 1])['timestamp']
                    back_time = (self.buffer[0])['timestamp']
                    time_difference = (front_time - back_time)
                    # print('time difference: ' + str(time_difference))
                    if time_difference > 2.5:
                        self.buffer.pop(0)
            while self.interrupt_triggered == 1:
                if len(self.buffer) > 1:
                    time.sleep(0.2)               
                    # print('interrupt == 1')
                    front_time = (self.buffer[len(self.buffer) - 1])['timestamp']
                    back_time = (self.buffer[0])['timestamp']
                    time_difference = (front_time - back_time)
                    # print('time difference: ' + str(time_difference))
                    if time_difference > 3:
                        print('SENDING DATA...')
                        # print(len(self.queue))
                        with buffer_lock:
                            sender_buffer = self.buffer
                            self.buffer = []
                        self.send_data(sender_buffer)
                        print('DATA HAS BEEN SENT!')
                        self.interrupt_triggered = False 

    def start_run(self):
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('0,234,765,667')
        time.sleep(0.5)
        self.data_manipulation('1,234,765,667')
        time.sleep(0.5)


if __name__ == '__main__':
    inst = Decoder()
