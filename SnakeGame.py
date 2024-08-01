from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):  #changes snake direction function.
  aim.x = x  #Sets x component of the aim vector to the provided x value
  aim.y = y  # Same but for y


def inside(head):
  return -200 < head.x < 190 and -200 < head.y < 190  #returns true if head position is within given boundries


def move():  #function to move forward by 1 segment
  head = snake[-1].copy(
  )  #copies the last element of snake list (the head) to get the next position
  head.move(aim)  #moves in the direction of the aim vector

  if not inside(
      head
  ) or head in snake:  #checks if head isn outside the boundriews or collides with the snake itself.
    square(
        head.x, head.y, 9,
        'red')  #draws a red square at the heads position to indicate game over
    update()  #Updates turtles graphics screen
    return  # exits move function and ends game.
  snake.append(head)  #Adds new head position to snake list.

  if head == food:  #checks if snake has eaten the food
    print('snake:', len(snake))  #prints the lenght of the snake (the score)
    food.x = randrange(-15, 15) * 10  #sets a new x position for food at random
    food.y = randrange(-15, 15) * 10  #sets a new y position for food at random
  else:
    snake.pop(0)  #removes the tail segment of the snake if no food is eaten

  clear()  # clears screen for redrawing.
  for body in snake:
    square(body.x,body.y,9,'orange')
    
  square(food.x,food.y,9,'blue') #food on screen as a green square size 9
  update() #updates graphics to show enw position (turtle)
  ontimer(move, 75)  #sets a timer to call the move function again after 100 milliseconds 

setup(400, 400, 370, 0)   #sets turtle graphics window size and poisiton
hideturtle()    #hides turtle cursor
tracer(False)  #disables animation for speed (turtle)
listen() # sets turtle hraphics window to listen for key events 
# binds arrow keys to change function to change snakes direction
# lambda is used to create annomymous functions for each key bind
onkey(lambda: change(10,0), 'd')
onkey(lambda: change(-10,0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0,-10), 's')
move() #calls the move function to star5t the game 
done()  # keeps the window open until the usr closes it or game end