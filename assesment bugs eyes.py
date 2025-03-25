import pygame, sys, random, time
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
 
# Game Setup/Global variables
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
global score
score = 0

 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Beat the Bug Eyes!')
 
## Function definitions

# Function for drawing the eyes in a random spot
def drawEyes (int) :
  if int == 1 :
    down = random.uniform(5, 250)
    across = random.uniform(5, 350)
  elif int == 2 :
    down = random.uniform(5, 250)
    across = random.uniform(550, 900)
  elif int == 3 :
    down = random.uniform(400, 700)
    across = random.uniform(5, 350)
  else :
    down = random.uniform(400, 700)
    across = random.uniform(550, 900)
  eye1 = pygame.Rect(across, down, 40 ,70)
  eye2 = pygame.Rect(across + 50, down, 40 ,70)
  pupil1 = pygame.Rect(across, down + 30, 40 ,10)
  pupil2 = pygame.Rect(across + 50, down + 30, 40 ,10)
  pygame.draw.ellipse(WINDOW, RED, eye1)
  pygame.draw.ellipse(WINDOW, RED, eye2)
  pygame.draw.ellipse(WINDOW, GREEN, pupil1)
  pygame.draw.ellipse(WINDOW, GREEN, pupil2)
  pygame.display.update()
  fpsClock.tick(FPS)

# Function for looking for an input from the player
def inputLoop(rand) :
  pygame.display.update()
  fpsClock.tick(FPS)
  keyPressed = False
  for event in pygame.event.get() :
    while keyPressed == False :
      pygame.event.pump()
      pressed = pygame.key.get_pressed()
      initialTime = time.time()
      if rand == 1 and pressed[K_LEFT] and pressed[K_UP] :
        timePressed = time.time()
        keyPressed = True
      elif rand == 2 and pressed[K_RIGHT] and pressed[K_UP] :
        timePressed = time.time()
        keyPressed = True
      elif rand == 3 and pressed[K_LEFT] and pressed[K_DOWN] :
        timePressed = time.time()
        keyPressed = True
      elif rand == 4 and pressed[K_RIGHT] and pressed[K_DOWN] :
        timePressed = time.time()
        keyPressed = True
  pygame.display.update()
  fpsClock.tick(FPS)
  #print (keyPressed) DOS
  return(timePressed-initialTime)

        
  



# The main function that controls the game
def main () :
  looping = True
  turn = 1
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        looping = False

    # Game progression
    print ("BUG EYES")

    # set turns
    while turn <= 10 :
      pygame.event.get()
      # Render elements of the game
      WINDOW.fill(BACKGROUND)
      pygame.display.update()
      fpsClock.tick(FPS)
      # Delay game for a random time between 2 and 4 seconds
      time.sleep(random.uniform(2,4))
      #print(turn) DOS
      #rand = 3 DOS
      
      # Assigns a random integer from 1 to 4 for which quadrant the eyes are going to be in then draws them
      rand = random.randint(1, 4)
      drawEyes(rand)

      # Asks for player input
      #print (f"rand: {rand}") DOS
      inputLoop(rand)

      # Displays the player score so far
      print (f"score: {score}")
      turn += 1
    
    
    # Displays final score and closing message
    print (f"Final score: {score}")
    if score > 1000 :
      print ("Congratulations for saving your planet!")
    else :
      print ("...")
      time.sleep(1)
      print ("You let everyone die. Despicable")
      # Quit game
    pygame.quit()
    quit()

main()