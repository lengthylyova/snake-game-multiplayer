import asyncio
from threading import Thread
from websockets.server import serve
from objects import Players, Field, Apple
from settings import field_width as w, field_height as h
from funcs import tick, snake_create

p = Players()
field = Field(w,h)
field.build()
apple = Apple()
apple.spawn(w,h,p.all)

async def echo(websocket):
    player = Players.Player(snake_create())
    p.add(websocket_id=websocket.id, player=player)
    async for message in websocket:
        player_snake = p.all[websocket.id].snake
        player_snake.move_direction_change(message)
        print(player_snake.move_direction)
        await websocket.send(player_snake.move_direction)


def game_session():
    while True:
        tick(field, p.all, apple)



async def main():
    gmFRED = asyncio.to_thread(game_session)
    async with serve(echo, "127.0.0.1", 80):
        await gmFRED



asyncio.run(main())