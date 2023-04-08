from settings import field_width, field_height, direction, header, speed
from objects import Snake, Apple
from time import sleep
from os import system



#___SNAKE___
def snake_create():
	head = Snake.Head()
	tail = Snake.Tail()
	snake = Snake(head, tail, direction)
	return snake


def snake_move(snake):
	if len(snake.tail.arr) > 0:
		snake.tail.update(snake.head)

	# actual move
	if snake.move_direction == 'RIGHT':
		snake.head.x += 1
	elif snake.move_direction == 'LEFT':
		snake.head.x -= 1
	elif snake.move_direction == 'UP':
		snake.head.y -= 1
	elif snake.move_direction == 'DOWN':
		snake.head.y += 1

	# not letting snake get out of field
	if snake.head.y > field_height-1:
		snake.head.y -= field_height
	elif snake.head.y < 0:
		snake.head.y += field_height

	if snake.head.x > field_width-1:
		snake.head.x -= field_width
	elif snake.head.x < 0:
		snake.head.x += field_width

	return True


#___APPLE___
def apple_create():
	apple = Apple()
	return apple


def was_apple_eaten(head, apple):
	if head.y == apple.y and head.x == apple.x:
		return True
	return False


#___GAME___
def restore(snake, apple):
	snake.spawn(field_width, field_height)
	apple.spawn(field_width, field_height, snake)
	return True


# tick = frame
def tick(field, players:dict, apple):
	for player in players:
		snake = players[player].snake
		snake.head.previous_position = [snake.head.y, snake.head.x]
		snake_move(snake)

	# cheking for apple bite.
	for player in players:
		snake = players[player].snake
		if was_apple_eaten(snake.head, apple):
			apple.spawn(field_width, field_height, players)
			snake.tail.add()
			snake.tail.update(snake.head)

	# printing frame
	print(header)
	field.paint(players, apple)
	field.print()
	# # cheking for snake's self bite.
	# if snake.suicide():
	# 	game.status = False
	# 	game.score = 0
	# 	restore(snake, apple)

	sleep(speed)
	system('cls')