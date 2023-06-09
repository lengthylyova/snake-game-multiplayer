from random import randint
from settings import colors, field_width, field_height


class Players():
	def __init__(self, color=None):
		self.all = {}
		self.total = 0

	class Player:
		def __init__(self, snake, nickname):
			self.snake = snake
			self.nickname = nickname
			self.score = 0

	def add(self, player):
		self.all[player.nickname] = player
		self.total += 1
	
	def player_delete(self, websocket_id):
		del self.all[websocket_id]
		self.total -= 1

	def get(self, websocket_id):
		return self.all[websocket_id].snake.tail.arr



class Snake():
	def __init__(self, head, tail, direction, color=None):
		self.head = head
		self.tail = tail
		self.move_direction = direction
		self.color = color


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
		def __init__(self, field_width, field_height):
			self.y = randint(1, field_height)
			self.x = randint(1, field_width)
			self.previous_position = [self.y, self.x]


	def suicide(self,  players):
		head = self.head

		not_able = []
		for player in players:
			s = players[player].snake

			condition1 = (head.y, head.x) == (s.head.y, s.head.x)
			condition2 = head.previous_position != s.head.previous_position

			if condition1 and condition2:
				s.spawn(field_width, field_height, players)
				return True
			
			for tail_part in s.tail.arr:
				not_able.append(tail_part)
				
		if [head.y, head.x] in not_able:
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
		if key == 'RIGHT' and self.move_direction != 'LEFT':
			self.move_direction = 'RIGHT'
		elif key == 'LEFT' and self.move_direction != 'RIGHT':
			self.move_direction = 'LEFT'
		elif key == 'UP' and self.move_direction != 'DOWN':
			self.move_direction = 'UP'
		elif key == 'DOWN' and self.move_direction != 'UP':
			self.move_direction = 'DOWN'



class Apples():
	def __init__(self):
		self.arr = []

	def spawn(self, field_width, field_height, players:dict):
		not_able = []
		for player in players:
			s = players[player].snake
			not_able.append((s.head.y, s.head.x))
			for tail_part in s.tail.arr:
				not_able.append(tail_part)

		for i in range(3-len(self.arr)):
			y = randint(1, field_height)
			x = randint(1, field_width)
			while [y, x] in not_able:
				y = randint(1, field_height)
				x = randint(1, field_width)
			self.arr.append((y, x))



class Field():
	def __init__(self, field_width, field_height):
		self.width = field_width
		self.height = field_height
		self.header = 'SnakeGame'
		self.empty = []
		self.full = []


	def build(self):
		self.empty = []
		for y in range(self.height + 2):
			self.empty.append([])
			for x in range(self.width + 2):
				if (y == 0) or (y == self.height + 1):
					self.empty[y].append('--')
					continue
				if (x == 0) or (x == (self.width + 1)):
					self.empty[y].append(' | ')
					continue
				self.empty[y].append(f'  ')


	def paint(self, players=None, apples=None):
		self.full = self.empty
		if apples != None:
			for apple in apples:
				self.full[apple[0]][apple[1]] = '\33[41m' + '  ' + '\33[0m'

		if players != None:
			for player in players:
				snake = players[player].snake
				self.full[snake.head.y][snake.head.x] = snake.color.start + '  ' + snake.color.end
				for tail_part in snake.tail.arr:
					self.full[tail_part[0]][tail_part[1]] = snake.color.start + '  ' + snake.color.end


	def to_string(self):
		subs = []
		for y in range(len(self.full)):
			subs.append(''.join(self.full[y]))
		return '\n'.join(subs)


	def print(self, string=None):
		arr = self.full
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				print(arr[i][j], end='')
			print()


class Color():
	def __init__(self, color_name:str):
		self.start = colors[color_name][0]
		self.end = colors[color_name][1]