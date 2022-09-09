# Circle clicking problem

###################################################
# Student should enter code below

import simplegui
import math

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    global RED_POS, GREEN_POS, BLUE_POS
    if dist(pos,RED_POS) < RADIUS:
        print ("Color is Red")
    elif dist(pos,GREEN_POS) < RADIUS:
        print ("Color is Green")
    else:
        print ("Color is Blue")
    
          

# define draw
def draw(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


###################################################
# Sample output

#Clicked red ball
#Clicked green ball
#Clicked blue ball
#Clicked green ball
#Clicked red ball
#Clicked green ball
#Clicked blue ball