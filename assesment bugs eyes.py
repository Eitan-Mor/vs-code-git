import pygame, sys, random, time
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup/Global variables
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1200
score = 0
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Beat the Bug Eyes!')
 
# Function definitions
def findPosition (int) :


  if int == 1 :
    down = 5
    across = 1
  elif int == 2 :
    down = 1
    across = 9
  elif int == 3 :
    down = 5
    across = 18
  else :
    down = 10
    across = 7
  return (down, across)

def drawEyes (position) :
  return ()



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
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
    fpsClock.tick(FPS)

    # Game progression
    print ("BUG EYES")
    # set turns
    while turn <= 10 :
      # Delay game for a random time between 2 and 4 seconds
      time.sleep(random.uniform(2,4))
      #Debugging output statement
      #print(turn)
      rand = random.randint(1, 4)
      position = findPosition(rand)
      drawEyes(position)


      turn += 1
    pygame.quit()
    quit()
main()