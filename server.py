import asyncio
from threading import Thread
import websockets
from time import sleep
from websockets.server import serve
from objects import Players, Field, Apple
from settings import field_width as w, field_height as h, speed
from funcs import tick, snake_create
from config import host, port


async def handler(websocket):
    player = Players.Player(snake_create())
    websocket_id = websocket.id.hex
    p.add(websocket_id=websocket_id, player=player)
    connected.add(websocket)
    print(f'>>> Connected with hex_id:{websocket_id}')
    try:
        async for message in websocket:
            player_snake = p.all[websocket_id].snake
            player_snake.move_direction_change(message)
    except websockets.ConnectionClosedError:
        print(f'>>> Disconnected with hex_id:{websocket_id}')
        del p.all[websocket_id]
    finally:
        connected.remove(websocket)


def game_session():
    while True:
        tick(field, p.all, apple)
        websockets.broadcast(connected, field.to_string())
        sleep(speed)


async def main():
    game_session_thread = asyncio.to_thread(game_session)
    async with serve(handler, host, port):
        await game_session_thread


def server_init():
    global field, apple, p, connected

    field = Field(w,h)
    field.build()
    print(f'>>> Field size: {w}x{h}.')

    p = Players()
    connected = set()
    print(f'>>> Players list created.')

    apple = Apple()
    apple.spawn(w,h,p.all)
    print(f'>>> First apple spawned.')

    print(f'>>> Starting server on {host}:{port}\n')
    asyncio.run(main())


if __name__ == '__main__':
    server_init()