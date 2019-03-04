import socketio 
from comms_class import ArduinoSerial 
url = 'http://138.68.140.17/' # For the deployed server it will differ
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('I\'m connected!')

@sio.on('disconnect')
def on_disconnect():
    #should probably stop end serial comms
    print('I\'m disconnected!')

@sio.on('reset')
def on_reset(data):
    print('modify:' + str(data))
    inst.configure_arduino()

@sio.on('stop')
def on_stop(data):
    print('stop received:' + str(data))
    inst.stop_serial()
    
@sio.on('start')
def on_start(data):
    print('start received:' + str(data))
    inst.start_serial()



inst = ArduinoSerial()
try:
    sio.connect(url)
    sio.wait()
except Exception as e:
    print(e)

