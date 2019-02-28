import socketio 
from d4_conversion_classes import Decoder
import ArduinoSerial from comms_class
url = 'http://138.68.140.17/' # For the deployed server it will differ
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('I\'m connected!')

@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')

@sio.on('reset')
def on_reset(data):
    print('reset received:' + str(data))
    inst.restart_data()

@sio.on('stop')
def on_stop(data):
    print('stop received:' + str(data))
    sio.emit('modify', True)
    inst.stop_data()
    
@sio.on('start')
def on_stop(data):
    print('start received:' + str(data))
    sio.emit('I\'m starting', True)
    inst.start_data()

@sio.on('modify')
def on_modify(data):
    print('modify received:' + str(data))
    return('TEST')


inst = ArduinoSerial()
sio.connect(url)
sio.wait()

