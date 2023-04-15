<h2><ins>Multiplayer</ins> SnakeGame 
<img src="https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white"></h2>
<img src="https://i.imgur.com/jKUswZS.gif">
<h3>Rules</h3>
	1. Going out of field -> return on the other side.<br>
	2. Biting an apple (red square) -> earn 100 points to score.<br>
	3. Biting yourself -> respawn (score resets).<br>
<img src="https://i.imgur.com/90vfssE.gif">
4. Biting someone else -> respawn (score resets)<br>
<img src="https://i.imgur.com/OTZliXz.gif">
5. Biting someone else's HEAD -> both respawn (both scores resets)<br>
<img src="https://i.imgur.com/tcljXc1.gif">

<h2>client/setting.py</h2>

```python
# control buttons
## to change buttons - change KeyCode
keys = {}
keys['UP'] = KeyCode.from_char('w')
keys['LEFT'] = KeyCode.from_char('a')
keys['DOWN'] = KeyCode.from_char('s')
keys['RIGHT'] = KeyCode.from_char('d')

# connect to
host = '127.0.0.1'
port = 80
```

<h2>server/settings.py</h2>

```python
# playground field size
field_width = 40
field_height = 30

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

# game speed:
# lower value -> faster gameplay
# must be grater than 0
speed = 0.1
```

<h2>server/config.py</h2>

```python
# server configuration
host = '0.0.0.0'
port = 80
```