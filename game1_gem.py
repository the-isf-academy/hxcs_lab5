# Write your code here :-)
# imports required libraries
import pgzrun
from helpers import *
from random import randint


# sets size of screen width
WIDTH = 500
# sets size of screen height
HEIGHT = 500

# sets screen background color (rgb color value)
BACKGROUND_COLOR = (149, 161, 171)

# creates a player sprite
player = Actor(image='alien.png', anchor=('center', 'bottom'))
player.scale = 1        # scales the sprite image
player.x = 250          # sets the X position
player.y = 250          # sets the Y position
PLAYER_SPEED = 10       # sets the speed of the sprite


# controls what gets draw on the screen
def draw():

    # draws the background
    screen.fill(BACKGROUND_COLOR)

    # draws the player
    player.draw()


# controls what happens every frame
def update():

    # if the right arrow key is pressed
    if keyboard[keys.RIGHT] and player.x < WIDTH:

        # moves the player to the right
        player.x += PLAYER_SPEED

        # flips the character to face to the right
        player.flip_x = False

    if keyboard[keys.LEFT] and player.x > 0:

        # moves the player to the right
        player.x -= PLAYER_SPEED

        player.flip_x = True


    # if the down arrow is pressed
    if keyboard[keys.DOWN] and player.y < HEIGHT:

        # moves the player down
        player.y += PLAYER_SPEED

    # if the down arrow is pressed
    if keyboard[keys.UP] and player.y > 0:

        # moves the player down
        player.y -= PLAYER_SPEED



# runs the game
pgzrun.go()
