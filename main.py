import pygame
import random
import math

pygame.init()

screen= pygame.display.set_mode((800 , 600))
pygame.display.set_caption("Kill My Enemy")
img=pygame.image.load('1.png')
pygame.display.set_icon(img)

rocket=pygame.image.load('spaceship.png')
skull=pygame.image.load('skull.png')
x=370
y=500
change=0

skull =[]
enemyX =[]

enemyY =[]

enemyX_change =[]

enemyY_change =[]

no_of_ene=6
for i in range(no_of_ene):
    skull.append(pygame.image.load('skull.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.2)
    enemyY_change.append(40)

fireimg=pygame.image.load('upload.png')
fireX=0
fireY=500
fireX_change=0
fireY_change=1.0
fire_state="ready"

amt = 0
font= pygame.font.Font("freesansbold.ttf", 32)

textX=10
textY=10

over_font= pygame.font.Font("freesansbold.ttf", 64)

def show_score(x,y):
    score = font.render("SCORE:" + str(amt), True, (255,255,255))
    screen.blit(score,(x,y))

def game_over():
    over_text = over_font.render("G A M E * O V E R" , True, (255,255,255))
    screen.blit(over_text,(120,250))
    
def player(x1,y1):
    screen.blit(rocket,(x1,y1))
def enemy(x1,y1, i):
    screen.blit(skull[i],(x1,y1))
    
def fire(x,y):
    global fire_state
    fire_state="fired"
    screen.blit(fireimg, (x+16,y+10))

def collide(enemyX, enemyY, fireX, fireY):
    distance = math.sqrt( math.pow(enemyX-fireX , 2) +
                          math.pow(enemyX-fireY , 2) )
    if distance < 24:
        return True
    return False

running = True
while running:
    screen.fill(( 0,0,0 ))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                change = -0.5
                
            if event.key == pygame.K_RIGHT:
                change = 0.5
                
            if event.key == pygame.K_SPACE:
                if fire_state is "ready":    
                    fireX=x
                    fire(fireX,fireY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
                change = 0
        

    
    x += change
    if x <=0:
        x=0
    elif x >=736:
        x=736
    for i in range(no_of_ene):
        if enemyY[i] > 300 :
            for j in range(no_of_ene):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <=0:
            enemyX_change [i]= 0.3
            enemyY [i]+= enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change [i]= -0.3
            enemyY [i]+= enemyY_change[i]
        collision = collide(enemyX[i], enemyY[i], fireX, fireY)
        if collision:
            fireY=480
            fire_state="ready"
            amt += 1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)            
        enemy(enemyX[i],enemyY[i], i)
    if fireY <= 0 :
        fireY=500
        fire_state="ready"

    if fire_state is "fired":
        fire(fireX,fireY)
        fireY -= fireY_change
        

    player(x,y)
    show_score(textX, textY)
    pygame.display.update()
