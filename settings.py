from pynput.keyboard import KeyCode

# playground field size
field_width = 15
field_height = 10

# Status for pauses or game stops.
game_status = 'OFF'

# snakes start direction
direction = 'DOWN'

# possible start game answers
answers = ['Y','y','N','n']

# playscreen header
header = f'<Esc> - PAUSE\n<Enter> - START'

# game speed:
# lower value -> faster gameplay
# must be grater than 0
speed = 0.8

# control buttons
keys = {}
keys['w'] = KeyCode.from_char('w')
keys['a'] = KeyCode.from_char('a')
keys['s'] = KeyCode.from_char('s')
keys['d'] = KeyCode.from_char('d')
