import asyncio
import websockets
from time import sleep
from websockets.server import serve
from objects import Players, Field, Apples, Color
from settings import field_width as w, field_height as h, speed
from funcs import tick, snake_create, get_random_color
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
        # if p.total < 2:
        #     websockets.broadcast(connected, 'Waiting for more players.')
        #     sleep(1)
        #     continue

        json_data = tick(field, p.all, apples)
        websockets.broadcast(connected, json_data)
        sleep(speed)


async def main():
    game_session_thread = asyncio.to_thread(game_session)
    async with serve(handler, host, port):
        await game_session_thread


def server_init():
    global field, apples, p, connected

    field = Field(w,h)
    field.build()
    print(f'>>> Field size: {w}x{h}.')

    p = Players()
    connected = set()
    print(f'>>> Players list created.')

    apples = Apples()
    apples.spawn(w,h,p.all)
    print(f'>>> First apple spawned.')

    print(f'>>> Starting server on {host}:{port}\n')
    asyncio.run(main())


if __name__ == '__main__':
    server_init()