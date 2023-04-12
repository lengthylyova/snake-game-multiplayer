from settings import field_width, field_height, direction, header, speed
from objects import Snake, Apples
from time import sleep
from os import system



#___SNAKE___
def snake_create():
	head = Snake.Head(field_width, field_height)
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
	if snake.head.y > field_height:
		snake.head.y -= field_height
	elif snake.head.y < 1:
		snake.head.y += field_height

	if snake.head.x > field_width:
		snake.head.x -= field_width
	elif snake.head.x < 1:
		snake.head.x += field_width

	return True


#___APPLE___
def apples_create():
	apples = Apples()
	return apples


def was_apple_eaten(head, apples):
	result = False
	for apple in apples:
		if apple == (head.y, head.x):
			del apples[apples.index(apple)]
			result = True

	return result



#___GAME___
def restore(snake, players):
	snake.spawn(field_width, field_height, players)


# tick = frame
def tick(field, players:dict, apples):
	for player in players:
		snake = players[player].snake

		# checking for eaten apple.
		if was_apple_eaten(snake.head, apples.arr):
			snake.tail.add()
			snake.tail.update(snake.head)

		# moving snake
		snake.head.previous_position = [snake.head.y, snake.head.x]
		snake_move(snake)

		# cheking for snake's self bite.
		if snake.suicide():
			restore(snake, players)


	apples.spawn(field_width, field_height, players)
	# printing frame.
	field.build()
	field.paint(players, apples.arr)