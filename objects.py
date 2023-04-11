from pynput.keyboard import Key
from random import randint
from settings import keys


class Players():
	def __init__(self):
		self.all = {}


	class Player:
		def __init__(self, snake):
			self.snake = snake


	def add(self, websocket_id, player):
		self.all[websocket_id] = player
	

	def player_delete(self, websocket_id):
		del self.all[websocket_id]


	def get(self, websocket_id):
		return self.all[websocket_id].snake.tail.arr


class Snake():
	def __init__(self, head, tail, direction):
		self.head = head
		self.tail = tail
		self.move_direction = direction


	class Tail():
		def __init__(self):
			self.arr = []

		def add(self):
			self.arr.append((0, 0))
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


	def spawn(self, field_width, field_height, players:dict):
		not_able = []
		for player in players:
			s = players[player].snake
			not_able.append((s.head.y, s.head.x))
			for tail_part in s.tail.arr:
				not_able.append(tail_part)

		self.head.y = randint(1, field_height)
		self.head.x = randint(1, field_width)
		while [self.head.y, self.head.x] in not_able:
			self.head.y = randint(1, field_height)
			self.head.x = randint(1, field_width)

		self.tail.arr = []


	def move_direction_change(self, key):
		if key == 'd' and self.move_direction != 'LEFT':
			self.move_direction = 'RIGHT'
		elif key == 'a' and self.move_direction != 'RIGHT':
			self.move_direction = 'LEFT'
		elif key == 'w' and self.move_direction != 'DOWN':
			self.move_direction = 'UP'
		elif key == 's' and self.move_direction != 'UP':
			self.move_direction = 'DOWN'


class Apple():
	def __init__(self):
		self.y = 0
		self.x = 0

	def spawn(self, field_width, field_height, players:dict):
		not_able = []
		for player in players:
			s = players[player].snake
			not_able.append((s.head.y, s.head.x))
			for tail_part in s.tail.arr:
				not_able.append(tail_part)

		self.y = randint(1, field_height)
		self.x = randint(1, field_width)
		while [self.y, self.x] in not_able:
			self.y = randint(1, field_height)
			self.x = randint(1, field_width)



class Field():
	def __init__(self, field_width, field_height):
		self.width = field_width
		self.height = field_height
		self.header = 'SnakeGame\n'
		self.empty = []
		self.full = []


	def build(self):
		self.empty = []
		for y in range(self.height + 2):
			self.empty.append([])
			for x in range(self.width + 2):
				if (y == 0) or (y == self.height + 1):
					self.empty[y].append('---')
					continue

				if (x == 0) or (x == (self.width + 1)):
					self.empty[y].append(' | ')
					continue

				self.empty[y].append(f'   ')

		return True


	def paint(self, players=None, apple=None):
		self.full = self.empty
		if apple != None:
			self.full[apple.y][apple.x] = '\33[31m' + ' @ ' + '\33[0m'

		if players != None:
			for player in players:
				snake = players[player].snake
				self.full[snake.head.y][snake.head.x] = '\33[92m' + ' Q ' + '\33[0m'
				for tail_part in snake.tail.arr:
					self.full[tail_part[0]][tail_part[1]] = '\33[32m' + ' o ' + '\33[0m'


	def to_string(self):
		s = self.header
		subs = []
		for y in range(len(self.full)):
			subs.append(''.join(self.full[y]))
		s = '\n'.join(subs)
		return s


	def print(self, string=None):
		arr = self.full
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				print(arr[i][j], end='')
			print()