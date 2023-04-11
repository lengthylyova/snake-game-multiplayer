import asyncio
from threading import Thread
import websockets
from time import sleep
from websockets.server import serve
from objects import Players, Field, Apple
from settings import field_width as w, field_height as h, speed
from funcs import tick, snake_create

p = Players()
connected = []
field = Field(w,h)
field.build()
apple = Apple()
apple.spawn(w,h,p.all)


async def echo(websocket):
    player = Players.Player(snake_create())
    p.add(websocket_id=websocket.id, player=player)
    connected.append(websocket)
    async for message in websocket:
        player_snake = p.all[websocket.id].snake
        player_snake.move_direction_change(message)


def game_session():
    while True:
        tick(field, p.all, apple)
        websockets.broadcast(connected, field.to_string())
        sleep(speed)



async def main():
    gmFRED = asyncio.to_thread(game_session)
    async with serve(echo, "127.0.0.1", 80):
        await gmFRED


asyncio.run(main())