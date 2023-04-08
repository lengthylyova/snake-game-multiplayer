import time
from websockets.sync.client import connect
from pynput import keyboard
from settings import keys
from threading import Thread

def on_press(key, websocket):
    if key == keys['w']:
        websocket.send('w')
    elif key == keys['a']:
        websocket.send('a')
    elif key == keys['s']:
        websocket.send('s')
    elif key == keys['d']:
        websocket.send('d')

def main(websocket):
    wasd_listener = keyboard.Listener(on_press=lambda key: on_press(key, websocket))
    wasd_listener.start()
    while True:
        message = websocket.recv()
        print(message)


if __name__ == '__main__':
    with connect('ws://127.0.0.1:80') as websocket:
        main(websocket)