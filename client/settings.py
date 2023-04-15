from pynput.keyboard import KeyCode


# control buttons
keys = {}
keys['UP'] = KeyCode.from_char('w')
keys['LEFT'] = KeyCode.from_char('a')
keys['DOWN'] = KeyCode.from_char('s')
keys['RIGHT'] = KeyCode.from_char('d')

# connect to
host = '127.0.0.1'
port = 80