from pynput.keyboard import KeyCode


# control buttons
keys = {}
keys['w'] = KeyCode.from_char('w')
keys['a'] = KeyCode.from_char('a')
keys['s'] = KeyCode.from_char('s')
keys['d'] = KeyCode.from_char('d')

# connect to
host = '127.0.0.1'
port = 80