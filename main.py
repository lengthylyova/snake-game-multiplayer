from settings import field_width as w, field_height as h, answers
from funcs import snake_create, apple_create, tick
from pynput import keyboard
from objects import Field, Game
from os import system

snake = snake_create()
snake.spawn(w,h)

apple = apple_create()
apple.spawn(w,h,snake)

field = Field(w,h)
field.build()
field.paint(snake, apple)

# Status for pauses or game stops.
game = Game()

start_stop_toogle = keyboard.Listener(on_press=lambda key: game.start_stop(key))
wasd_listener = keyboard.Listener(on_press=lambda key: snake.move_direction_change(key))


if __name__ == '__main__':
	system('cls')
	answer = input('Wanna play a snake game? (Y/N):\t')
	while answer not in answers:
		system('cls')
		answer = ('Wanna play a snake game? (Y/N):\t')

	if answer in ['Y', 'y']:
		system('cls')
		start_stop_toogle.start()
		wasd_listener.start()
		tick(snake, apple, field, game)
		while True:
			if game.status:
				system('cls')
				tick(snake, apple, field, game)
	exit()