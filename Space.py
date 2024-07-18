import pgzrun
import random

WIDTH = 1024
HEIGHT = 700

player = Actor("playership1_blue")
player.pos = (WIDTH/2,HEIGHT/2)


enemies = []
player_laser = []

def update():
    if random.randint(0,100)<5:
        enemy = Actor ("enemyblack1")
        enemies.append(enemy)
        enemy.x = random.randint(0,WIDTH)
        enemies.append(enemy)

        
    if keyboard.space:
    
        laser = Actor ("laserblue15")
        laser.pos = player.pos
        player_laser.append(laser)
        laser

    if keyboard.up:
        player.y-=5
    if keyboard.down:
        player.y+=5
    if keyboard.left:
        player.x-=5
    if keyboard.right:
        player.x+=5

    if player.left<0:
        player.left = 0
    if player.right>WIDTH:
        player.right = WIDTH
    if player.top<0:
        player.top = 0
    if player.bottom>HEIGHT:
        player.bottom = HEIGHT


    



    


 

def on_key_down(key):
    if key == keys.UP:
        player.y-=5
    if key == keys.DOWN:
        player.y+=5
    if key == keys.LEFT:
        player.x-=5
    if key == keys.RIGHT:
        player.x+=5

def draw():
    screen.clear()
    player.draw()
    for enemy in enemies:
        enemy.draw() 
        laser.draw()
    
    



pgzrun.go()