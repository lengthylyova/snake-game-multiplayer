from time import sleep
from os import system
import websockets
from websockets.sync.client import connect
from pynput import keyboard
from settings import keys, host, port
import json


def on_press(key, websocket):
    if key == keys['UP']:
        websocket.send('UP')
    elif key == keys['LEFT']:
        websocket.send('LEFT')
    elif key == keys['DOWN']:
        websocket.send('DOWN')
    elif key == keys['RIGHT']:
        websocket.send('RIGHT')


def main(websocket, nickname):
    websocket.send(nickname)
    wasd_listener = keyboard.Listener(on_press=lambda key: on_press(key, websocket))
    wasd_listener.start()
    while True:
        try:
            data = websocket.recv()
            try:
                json_data = json.loads(data)
                system('cls')
                print(f'Players on server: {json_data["players_total"]}')
                print(json_data['field'])
                print('Scores:')
                for score in json_data['scores']:
                    print(score)
            except:
                system('cls')
                print(data)
        except websockets.ConnectionClosedError:
            print('>>> Oops, connection lost...')
            sleep(2)
            exit()


if __name__ == '__main__':
    nickname = ''
    while nickname == '':
        nickname = input('>>> Enter your nickname\t')

    with connect(f'ws://{host}:{port}') as websocket:
        main(websocket, nickname)