import math

class tank:
    
    def __init__(self, pos_x, angle, nrPlayer):
        #init tank
        self.x = pos_x
        self.y = 150
        self.health = 100
        self.height = 20
        self.width = 40
        self.top = 20
        self.angle = -angle*math.pi/180
        self.barrel = 25
        self.bulletX = -100
        self.bulletY = -100
        self.bulletRadius = 2
        self.bulletPower = 10
        self.time = 0
        self.bulletInAir = False
        self.bulletExploded = False
        self.canShoot = False
        self.wWidth = 600
        self.wHeigth = 400
        self.player = nrPlayer
        self.dirx = 0
        self.angleMov = 0
        
    def move(self):
        #move tank
        self.move_x = self.dirx*5
        self.x += self.move_x
        
    def aim(self):
        #move barrel
        self.moveBarrel = 2*self.angleMov 
        if self.angle < 0 and self.moveBarrel > 1 or self.angle > -math.pi and self.moveBarrel < 1:
            self.angle += self.moveBarrel*math.pi/180
        
    def shoot(self):
        #check if new bullet can be fired
        if self.time == 0 and self.canShoot == True:
            self.bulletX = int(self.barrel*math.cos(self.angle)+(self.x + self.width/2))
            self.bulletY = int(self.barrel*math.sin(self.angle)+(self.y))
        
        #move bullet in air
        if self.bulletInAir == True:
            self.canShoot = False
            self.bulletX += int(self.bulletPower*math.cos(self.angle))
            self.bulletY += int(self.bulletPower*math.sin(self.angle) + 0.3*self.time)
            self.time += 1           
        
    def hitbox(self, otherPlayer):
        #border for tank
        if self.x < 0:
            self.x = 0
        elif self.x + self.width  > self.wWidth:
            self.x = self.wWidth - self.width
        
        #border for bullet    
        if (0 > self.bulletX or self.bulletX > self.wWidth) or (-50 > self.bulletY or self.bulletY > 150):
            self.bulletInAir = False
            self.bulletExploded = True
            if self.time == 0:
                self.bulletExploded = False
            self.time = 0
            
        
        #damage from bullet on other player
        if self.bulletInAir == False and self.bulletExploded == True:
            self.damage = 150/abs(otherPlayer.x - self.bulletX + 1)
            if abs(otherPlayer.x - self.bulletX) < 50:
                self.health -= self.damage
            
            bulletExploded = False
            self.bulletX = -100
            self.bulletY = -100
            otherPlayer.canShoot = True
   