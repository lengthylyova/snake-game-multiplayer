import time
from os import system
import websockets
from websockets.sync.client import connect
from pynput import keyboard
from settings import keys
import json


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
        try:
            data = websocket.recv()
            try:
                json_data = json.loads(data)
                system('cls')
                print(json_data['field'])
                print(f'Players on server: {json_data["players_total"]}')
            except:
                system('cls')
                print(data)
        except websockets.ConnectionClosedError:
            print('>>> Oops, connection lost...')
            time.sleep(2)
            exit()


if __name__ == '__main__':
    input('>>> Press enter to connect\t')
    with connect('ws://127.0.0.1:80') as websocket:
        main(websocket)