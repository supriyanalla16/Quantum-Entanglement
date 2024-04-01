import pygame
import random
import math 

#initialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800, 600))

#backgroud
back=pygame.image.load(r'D:\pygame\sship_game\background.jpg')

# Sound
pygame.mixer.music.load(r"D:\pygame\sship_game\background.wav")
pygame.mixer.music.play(-1)
# z=pygame.mixer.sound("D:\pygame\sship_game\background.wav")
# z.play(-1)


#Caption and icon
pygame.display.set_caption('Space Invaders')
icon=pygame.image.load(r'D:\pygame\sship_game\ufo1.png')
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load(r'D:\pygame\sship_game\PlayerImg.png')
playerX=370
playerY=480
playerX_change=0

# Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load(r'D:\pygame\sship_game\alien.png'))
    EnemyX.append(random.randint(0, 736))
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(1)
    EnemyY_change.append(40)

#Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
BulletImg=pygame.image.load(r'D:\pygame\sship_game\bullet.png')
BulletX=0
BulletY=480
BulletX_change=0
BulletY_change=5
Bullet_state = "ready"

# Score
score_value = 0
font1 = pygame.font.Font(r'D:\pygame\sship_game\game_over.ttf', 50 )
textX = 10
testY = 10

def player(x, y):
    screen.blit(playerImg, (x, y))
#     screen.blit(playerImg, (370, 480))

def Enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))

def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x+16, y+10))  #since x and y are the leftmost position of the spaceship, so (x+16, y) is the center of the spaceship and (x+16, y+10)will be the topmost and center of the spaceship

def isCollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt(math.pow(EnemyX - BulletX, 2) + (math.pow(EnemyY - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score = font1.render("Score : " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_font = pygame.font.Font(r'D:\pygame\sship_game\game_over.ttf', 186)
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (180, 200))

#Game Loop
running="True"
while running:
    #RGB-Red, Green, Blue
    # screen.fill((220, 208, 255))

    #background image
    screen.blit(back, (0, 0))

    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False

        # if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # playerX-=1
                playerX_change=-5
            if event.key == pygame.K_RIGHT:
                # playerX+=1
                playerX_change=5
            if event.key == pygame.K_SPACE:
                if Bullet_state=="ready":
                    bulletSound = pygame.mixer.Sound(r"D:\pygame\sship_game\laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    BulletX = playerX
                    fire_bullet(playerX, BulletY)
        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # playerX= 0+playerX
                playerX_change=0


    playerX+=playerX_change

    #Checking for boundaries for spaceship, so it doesn't go out of bounds
    if(playerX<0):
        playerX=0
    if(playerX>736):
        playerX=736

    # Bullet Movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"

    if Bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    player(playerX, playerY)
    # playerImg=pygame.image.load('playerImg.png')
    # screen.blit(playerImg, (370, 480))

    # Enemy Movement
    for i in range(num_of_enemies):
        # Game Over
        if EnemyY[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break
        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 1
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -1
            EnemyY[i] += EnemyY_change[i]
        # Collision
        collision = isCollision(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            x=pygame.mixer.Sound(r"D:\pygame\sship_game\explosion.wav")
            x.play()
            # pygame.mixer.Sound.play()
            BulletY = 480
            Bullet_state = "ready"
            score_value+= 1
            EnemyX[i] = random.randint(0, 736)
            EnemyY[i] = random.randint(50, 150)
        Enemy(EnemyX[i], EnemyY[i], i)
    show_score(textX, testY)
    pygame.display.update()
        