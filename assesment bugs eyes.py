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

 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Beat the Bug Eyes!')
 
## Function definitions

# Introduction message and controls
def intro() :
  print ("BUG EYES")
  time.sleep(1)
  print ("Bug eyes surround your ship.")
  time.sleep(1)
  print ("Bug eyes surround the earth.")
  time.sleep(1)
  print ("Kill them quickly, or everyone will die.")
  time.sleep(1)
  print ("use the arrow keys to indicate the diagonal direction the eyes appear in, your final score must be under 10.")
  print ("You have to survive 10 waves")
  time.sleep(3)

# Closing message 
def outro(score) :
  counter = 0
  print (f"Final score: {score}")
  HighScores = open('recordHighScores.txt', 'a')
  if score < 10 :
    print ("Congratulations for saving your planet! You will be remembered.")
    HighScores.write('w')
  else :
    print ("...")
    time.sleep(1)
    print ("You let everyone die. Despicable")
    HighScores.write('l') 
  HighScores.close()
  with open("recordHighScores.txt") as file :
    contents = file.read()
    W = contents.count("w")
    L = contents.count("l")
    print ("Wins: ", W)
    print ("Losses: ", L)
    if W > L :
      print ("You shoud look into a career in this!")
    elif L > W :
      print ("You might want to reconsider your career in space...")
    else :
      print ("Hey, at least you saved someone.")

    
    
  


# Function for drawing the eyes in a random spot
def drawEyes (rand) :

  pygame.display.update
  if rand == 1 :
    down = random.uniform(5, 250)
    across = random.uniform(5, 350)
  elif rand == 2 :
    down = random.uniform(5, 250)
    across = random.uniform(550, 900)
  elif rand == 3 :
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
  return ()

# Function for looking for an input from the player
def inputLoop(rand) :
  initialTime = time.time()
  pygame.display.update()
  fpsClock.tick(FPS)
  keyPressed = False
  for event in pygame.event.get() :
    pygame.event.pump()
    pressed = pygame.key.get_pressed()
    while keyPressed == False :
      pygame.event.pump()
      pressed = pygame.key.get_pressed()
      if rand == 1 and pressed[K_LEFT] and pressed[K_UP] :
        keyPressed = True
      elif rand == 2 and pressed[K_RIGHT] and pressed[K_UP] :
        keyPressed = True
      elif rand == 3 and pressed[K_LEFT] and pressed[K_DOWN] :
        keyPressed = True
      elif rand == 4 and pressed[K_RIGHT] and pressed[K_DOWN] :
        keyPressed = True
      if rand == 1 :
        if pressed[K_RIGHT] or pressed[K_DOWN] :
          keyPressed = False
      elif rand == 2 :
        if pressed[K_LEFT] or pressed[K_DOWN] :
         keyPressed = False
      elif rand == 3 :
        if pressed[K_RIGHT] or pressed[K_UP] :
          keyPressed = False
      elif rand == 4 : 
        if pressed[K_LEFT] or pressed[K_UP] :
          keyPressed = False
  return(initialTime)

# Function for handling all the functions regarding the visual bugs eyes and inputs
def bugEyes(rand) :
  drawEyes(rand)
  initialTime = inputLoop(rand)
  tps = time.time()
  #print (tps, initialTime) #DOS
  roundScore = tps - initialTime 
  return (roundScore)
  



# The main function that controls the game
def main () :
  # Decleare variables within main
  looping = True
  turn = 1
  score = 0
  # The main game loop
  while looping :
    # Get inputs, make the game quittable in the beginning
    for event in pygame.event.get() :
      if event.type == QUIT :
        looping = False

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
    fpsClock.tick(FPS)
    # Game introduction and controls
    #intro()

    # what happens each turn
    while turn <= 10 and score < 10 :
      pygame.event.get()
      # Render elements of the game
      WINDOW.fill(BACKGROUND)
      pygame.display.update()
      fpsClock.tick(FPS)
      # Delay game for a random time between 2 and 4 seconds
      time.sleep(random.uniform(2,4))
      #print(turn) #DOS
      #rand = 3 #DOS
      
      # Assigns a random integer from 1 to 4 for which quadrant the eyes are going to be in then draws them
      rand = random.randint(1, 4)
      

      # Asks for player input and assigns a score depending on the player's speed
      #print (f"rand: {rand}") #DOS
      score = round(score + bugEyes(rand), 2)
      

      # Displays the player score after every wave/turn
      print (f"score: {score}")
      turn += 1
    
    
    # Displays final score and closing message
    outro(score)
    
    # Quit game
    pygame.quit()
    quit()

main()