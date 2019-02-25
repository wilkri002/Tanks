import pygame
import math
import time
from tank import tank
import random

#window dimensions
windowHeight = 400
windowWidth = 600

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (112, 175, 66)
DARK_GREEN = (84, 130, 50)
RED = (255, 0, 0)
BLUE = (68, 182, 255)
BROWN = (155, 121, 27)

#initiate pygame
pygame.init()
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Tanks!")
clock = pygame.time.Clock()
#create fonts
font = pygame.font.SysFont(None, 24)
bigFont = pygame.font.SysFont("comicsansms", 72)

def draw_tank(player):
    #Barrel
    pygame.draw.line(gameDisplay, BLACK, [player.x + player.width/2, player.y], [player.barrel*math.cos(player.angle)+(player.x + player.width/2), player.barrel*math.sin(player.angle)+(player.y)], 3)
    #Bottom body
    pygame.draw.rect(gameDisplay, DARK_GREEN, (player.x, player.y, player.width, player.height))
    #Top body
    pygame.draw.rect(gameDisplay, GREEN, ((player.x + player.width/4), (player.y - player.height/2), player.top, player.top))
    if player.bulletInAir == True:
        #Bullet
        player.shoot()
        pygame.draw.circle(gameDisplay, BLACK, (player.bulletX, player.bulletY), player.bulletRadius)
    #life
    life = font.render("Player " + str(player.player) + " life: " + str(round(player.health)), True, BLACK)
    if player.player == 2:
        gameDisplay.blit(life, (470,0))
    else:
        gameDisplay.blit(life, (0,0))


def draw_display(player1, player2):
    #backround
    gameDisplay.fill(BLUE)
    #ground
    pygame.draw.rect(gameDisplay, BROWN, [0, 170, windowWidth, windowHeight])
    #draw player1
    draw_tank(player1)
    #draw player2
    draw_tank(player2)
      
    pygame.display.update()
    

def winGame(player1, player2):
    #win screen, display win message and reset
    if player1.health <= 0 or player2.health <= 0:
        if player1.health <= 0:
            win = bigFont.render("Player 2 wins", True, BLACK)
        else:
            win = bigFont.render("Player 1 wins", True, BLACK)
        gameDisplay.blit(win, (100, 50))
        pygame.display.update()
        clock.tick(30)
        time.sleep(2)
        game_loop()
        
        
def playerAction(player, player2):
    #move tank
    player.move()             
    #move barrel
    player.aim()              
    #check hitbox
    player.hitbox(player2)    
    
    
def playerKeyPress(player1, player2):
        #needs to be here for game to run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                #close game if escape is pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                #move players
                if event.key == pygame.K_LEFT:
                    player1.dirx = -1
                        
                if event.key == pygame.K_RIGHT:
                    player1.dirx = 1
                
                if event.key == pygame.K_UP:
                    player1.angleMov = -1
                
                if event.key == pygame.K_DOWN:
                    player1.angleMov = 1
                
                if event.key == pygame.K_a:
                    player2.dirx = -1
                        
                if event.key == pygame.K_d:
                    player2.dirx = 1
                
                if event.key == pygame.K_w:
                    player2.angleMov = -1
                
                if event.key == pygame.K_s:
                    player2.angleMov = 1
                
                #shoot if space is pressed
                if event.key == pygame.K_SPACE:
                    if player1.canShoot == True:
                        player1.bulletInAir = True
                        player1.shoot()
                        
                    if player2.canShoot == True:
                        player2.bulletInAir = True
                        player2.shoot()
                    
            if event.type == pygame.KEYUP:
                #reset when key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player1.dirx = 0
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player1.angleMov = 0
                    
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player2.dirx = 0
                    
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player2.angleMov = 0


def game_loop():
    
    #start player 1
    player1 = tank(540, 135, 1)
    
    #start player 2
    player2 = tank(20, 45, 2)

    #random who will start
    playerStart = random.randint(0, 1)
    if playerStart == 0:
        player1.canShoot = True
    else:
        player2.canShoot = True
    
    while True:
        #check keys pressed
        playerKeyPress(player1, player2)
        
        #action for player1
        playerAction(player1, player2)
        #action for player2
        playerAction(player2, player1)
        
        #draw the display
        draw_display(player1, player2)
        
        #check if someone is winning
        winGame(player1, player2)
        
        #tick clock
        clock.tick(30)

game_loop()
pygame.quit()
quit()