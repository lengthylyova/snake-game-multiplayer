from pynput.keyboard import Key
from random import randint
from settings import keys


class Game():
	def __init__(self):
		self.status = False
		self.score = 0

	def start_stop(self, key):
		if key == Key.enter:
			self.status = True
		elif key == Key.esc:
			self.status = False


class Head():
	def function(self):
		self.y = 0
		self.x = 0
		self.previous_position = [self.y, self.x]


class Tail():
	def __init__(self):
		self.arr = []

	def add(self):
		self.arr.append([0, 0])
		return True

	def pop(self):
		self.arr.pop()
		return True

	def update(self, head):
		self.arr.pop()
		prev_pos = head.previous_position
		self.arr.insert(0, prev_pos)


class Snake():
	def __init__(self, head, tail, direction):
		self.head = head
		self.tail = tail
		self.move_direction = 'DOWN'

	def suicide(self):
		head = self.head
		if [head.y, head.x] in self.tail.arr:
			return True
		return False

	def spawn(self, field_width, field_height):
		self.head.y = randint(0, field_height-1)
		self.head.x = randint(0, field_width-1)
		self.tail.arr = []

	def move_direction_change(self, key):
		if key == keys['d'] and self.move_direction != 'LEFT':
			self.move_direction = 'RIGHT'
		elif key == keys['a'] and self.move_direction != 'RIGHT':
			self.move_direction = 'LEFT'
		elif key == keys['w'] and self.move_direction != 'DOWN':
			self.move_direction = 'UP'
		elif key == keys['s'] and self.move_direction != 'UP':
			self.move_direction = 'DOWN'


class Apple():
	def __init__(self):
		self.y = 0
		self.x = 0

	def spawn(self, field_width, field_height, snake):
		
		not_able = [i for i in snake.tail.arr]
		not_able.append([snake.head.y, snake.head.x])
		while [self.y, self.x] in not_able:
			self.y = randint(0, field_height-1)
			self.x = randint(0, field_width-1)


class Field():
	def __init__(self, field_width, field_height):
		self.width = field_width
		self.height = field_height
		self.arr = []

	def build(self):
		for y in range(self.height):
			self.arr.append([])
			for x in range(self.width):
				self.arr[y].append("")
		return True

	def paint(self, snake, apple):
		for y in range(self.height):
			for x in range(self.width):
				if ([y, x] == [snake.head.y, snake.head.x]) or ([y, x] in snake.tail.arr):
					self.arr[y][x] = " @ "
				elif [y, x] == [apple.y, apple.x]:
					self.arr[y][x] = " $ "	
				else:
					self.arr[y][x] = "   "


	def print(self):
		for y in range(0, self.height+2):
			for x in range(0, self.width+2):
				if y == 0 or y == self.height+1:
					print("---", end="")
				elif x == 0 or x == self.width+1:
					print(" | ", end="")
				else:
					print(self.arr[y-1][x-1], end="")
			print()
		return True