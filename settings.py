from pynput.keyboard import KeyCode

# playground field size
field_width = 10
field_height = 10

# Status for pauses or game stops.
game_status = 'OFF'

# snakes start direction
direction = 'DOWN'

# available colors
colors = {
	"green_fill" : ['\33[42m', '\33[0m'],
	"red_fill" : ['\33[41m', '\33[0m'],
	"purple_fill" : ['\33[45m', '\33[0m'],
	"white_fill" : ['\33[47m', '\33[0m'],
	"yellow_fill" : ['\33[43m', '\33[0m'],
}

# possible start game answers
answers = ['Y','y','N','n']

# playscreen header
header = f'<Esc> - PAUSE\n<Enter> - START'

# game speed:
# lower value -> faster gameplay
# must be grater than 0
speed = 0.05

# control buttons
keys = {}
keys['w'] = KeyCode.from_char('w')
keys['a'] = KeyCode.from_char('a')
keys['s'] = KeyCode.from_char('s')
keys['d'] = KeyCode.from_char('d')
