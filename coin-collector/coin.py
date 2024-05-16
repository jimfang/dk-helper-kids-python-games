import pgzrun

from random import randint

WIDTH = 400
HEIGHT = 400
MOVE_SPEED = 4

score = 0
game_over = False

# fox = Actor("fox")
fox = Actor("hedgehog")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(50, 160), fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))
    

def time_up():
    global game_over
    game_over = True


def update():
    global score
    if keyboard.left:
        fox.x = fox.x - MOVE_SPEED
    elif keyboard.right:
        fox.x = fox.x + MOVE_SPEED
    elif keyboard.up:
        fox.y = fox.y - MOVE_SPEED
    elif keyboard.down:
        fox.y = fox.y + MOVE_SPEED

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()


# main
clock.schedule(time_up, 10.0)

place_coin()

pgzrun.go()