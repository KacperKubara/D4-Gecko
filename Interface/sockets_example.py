import socketio 
from d4_conversion_classes import Decoder
url = 'http://138.68.140.17/' # For the deployed server it will differ
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('I\'m connected!')
    inst.start_run()

@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')

@sio.on('reset')
def on_reset(data):
    print('reset received:' + str(data))

@sio.on('stop')
def on_stop(data):
    print('stop received:' + str(data))
    sio.emit('modify', True)

@sio.on('modify')
def on_modify(data):
    print('modify received:' + str(data))
    return('TEST')


inst = Decoder()
sio.connect(url)
sio.wait()

