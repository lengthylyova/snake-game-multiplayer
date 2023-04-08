from pynput.keyboard import Key
from random import randint
from settings import keys


class Players():
	def __init__(self):
		self.all = {}


	class Player:
		def __init__(self, snake):
			self.snake = snake


	def add(self, connection_id, player):
		self.all[connection_id] = player
	
	def get(self, connection_id):
		return self.all[connection_id].snake.tail.arr


class Game():
	def __init__(self):
		self.status = False
		self.score = 0

	def start_stop(self, key):
		if key == Key.enter:
			self.status = True
		elif key == Key.esc:
			self.status = False	


class Snake():
	def __init__(self, head, tail, direction):
		self.head = head
		self.tail = tail
		self.move_direction = direction


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


	class Head():
		def __init__(self):
			self.y = 0
			self.x = 0
			self.previous_position = [self.y, self.x]


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

	def spawn(self, field_width, field_height, players:dict):
		not_able = []
		for player in players:
			s = players[player].snake
			not_able.append([s.head.y, s.head.x])
			not_able.append([i for i in s.tail.arr])

		self.y = randint(0, field_height-1)
		self.x = randint(0, field_width-1)
		while [self.y, self.x] in not_able:
			self.y = randint(0, field_height-1)
			self.x = randint(0, field_width-1)


class Field():
	def __init__(self, field_width, field_height):
		self.width = field_width
		self.height = field_height
		self.arr = []
		self.empty = []

	def build(self):
		for y in range(self.height):
			self.empty.append([])
			for x in range(self.width):
				self.empty[y].append(" - ")
		return True

	def paint(self, players=None, apple=None):
		self.arr = self.empty
		if players != None:
			for player in players:
				s = players[player].snake
				self.arr[s.head.y, s.head.x] = ' @ '
				for tail_part in s.tail.arr:
					self.arr[tail_part[0]][tail_part[1]] = ' @ '
		
		if apple != None:
			self.arr[apple.y][apple.x] = ' $ '


	def to_string(self):
		s = ''
		subs = []
		for y in range(self.height):
			subs.append(''.join(self.arr[y]))
		s = '\n'.join(subs)
		return s

	def print(self, string=None):
		if not string:
			for y in range(0, self.height+2):
				for x in range(0, self.width+2):
					if y == 0 or y == self.height+1:
						print("---", end="")
					elif x == 0 or x == self.width+1:
						print(" | ", end="")
					else:
						print(self.arr[y-1][x-1], end="")
				print()

		print(string)