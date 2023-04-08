import asyncio
from websockets.server import serve
from objects import Players
from funcs import snake_create

p = Players()

async def echo(websocket):
    player = Players.Player(snake_create())
    p.add(websocket_id=websocket.id, player=player)
    async for message in websocket:
        player_snake = p.all[websocket.id].snake
        player_snake.move_direction_change(message)
        print(player_snake.move_direction)

    

async def main():
    async with serve(echo, "127.0.0.1", 80):
        await asyncio.Future()  # run forever


asyncio.run(main())