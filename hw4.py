#Name: Nana Kwasi Owusu
#Drexel id: no329
#Purpose of file: This is the main game file for a simple ball-and-paddle game implemented using Pygame.
import pygame
import random
from ball import Ball
from paddle import Paddle
from text import Text

pygame.init()
surface = pygame.display.set_mode((800, 600))
DREXEL_BLUE = (7, 41, 77)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Variables related to the game state
score = 0
lives = 10  
timer = 60000  # 60 seconds in milliseconds
gameOver = False
won = False

# Initializing all the objects for the game to work
myBall = Ball(400, 300, 25, DREXEL_BLUE)
myPaddle = Paddle(200, 25, DREXEL_BLUE)
myScoreBoard = Text(f'Score: {score}', 10, 10)
myLives = Text(f'Lives: {lives}', 10, 30)
myTimer = Text(f'Time: {timer // 1000}', 10, 50)

# Creating rectangles used to represent the bombs
bombs = []
for i in range(4):  
    x = random.randint(50, 750)
    y = 0  
    width = 30
    height = 30
    bomb = pygame.Rect(x, y, width, height)
    bombs.append(bomb)

# Variable used to keep track of the exploded bombs so that a bomb does damage only once
exploded_bombs = set()

running = True
fpsClock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
bomb_spawn_time = pygame.time.get_ticks()

while running:
    surface.fill((255, 255, 255))

    # Drawing the game objects onto the surface
    myBall.draw(surface)
    myPaddle.draw(surface)
    myScoreBoard.draw(surface)
    myLives.draw(surface)
    myTimer.draw(surface)

    for bomb in bombs:
        if tuple(bomb) not in exploded_bombs:
            pygame.draw.rect(surface, RED, bomb)

    # Checks for collisions to update the game state
    if myBall.intersects(myPaddle):
        myBall.setYSpeed(myBall.getYSpeed() * -1)
        lives -= 1
        score += 20

    for bomb in bombs:
        if bomb.colliderect(myPaddle.get_rect()) and tuple(bomb) not in exploded_bombs:
            if score >= 20:
                score -= 20
            else:
                score = 0
            exploded_bombs.add(tuple(bomb))

    # Updating the game state
    ball_hit_bottom = myBall.move()
    if ball_hit_bottom:
        myBall.setYSpeed(myBall.getYSpeed() * -1)  # Bounce off the bottom
        lives -= 1# Deduct a life
        myBall.setX(400)  # Reset ball position to the center
        myBall.setY(150)
        myBall.randomize_speed()

    myScoreBoard.setMessage(f'Score: {score}')
    myLives.setMessage(f'Lives: {lives}')

    # The logic for how the timer works
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = timer - elapsed_time
    myTimer.setMessage(f'Time: {remaining_time // 1000}')
    if remaining_time <= 0:
        gameOver = True
        running = False

    # Spawning new bombs every two seconds
    current_time = pygame.time.get_ticks()
    if current_time - bomb_spawn_time >= 2000:  
        bomb_spawn_time = current_time
        x = random.randint(50, 750)
        y = 0
        width = 30
        height = 30
        bomb = pygame.Rect(x, y, width, height)
        bombs.append(bomb)

    #removes bombs that are spawned outside the screen
    for i, bomb in enumerate(bombs):
        bomb.y += 2  
        if bomb.y > 600: 
            bombs.pop(i)
    
    #Game Over or win conditions
    if lives <= 0:
        gameOver = True
        won = False
        running = False

    if score >= 100:
        gameOver = True
        won = True
        running = False

    #Displaying the game results 
    if gameOver:
        over_surface = pygame.Surface((400, 200))
        over_surface.fill((255, 255, 250))
        game_over_text = Text("Game Over", 100, 50)
        game_over_text.draw(over_surface)
        if won:
            resultText = Text("You win!", 100, 100, (0, 255, 0))
        else:
            resultText = Text("You lose!", 100, 100, (255, 0, 0))
        resultText.draw(over_surface)
        surface.blit(over_surface, (200, 200))
        pygame.display.update()
        pygame.time.wait(3000)  
        running = False
    
    #Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    fpsClock.tick(150)

pygame.quit()
