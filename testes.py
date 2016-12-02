import pygame
import txt
import random
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("SansitaOne.tff", 50)
# Color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (190,190,190)
window_size = window_width, window_height = 1280,720
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

# Create a box and put it in a variable.
# You should note that the variable now has the type Rect(is a Rect)
unit = 100
rect = pygame.Rect(30, 30, 2.5*unit, 3.5*unit)




# choose the color for the box
color = BLACK

pygame.display.set_caption('Test')
window.fill(WHITE)

running = True

# To be able to detect if the mouse is within the box I use a very handy
# function of the Rect class, called collidepoint()
# I only need to get the position of the mouse and use that as a parameter to
# the collidepoint function.  It is possible to get the coordinates with this:event.pos

# The demonstration itself draws a red rectangle on the screen and if the user
# clicks the mouse within this rect the color changes to green.
# If the user releases the mouse within the rectangle(box) the color changes back to red
# Now the question is:  What happens if the user releases the mouse outside of the rectangle(box)  :-)
s = 'To be able to detect if the mouse is within the box I use a very handy'
def get_string():
        list1 = ["Why can't I sleep at night?","I got 99 problems but _ ain't one.","What's a girl's best friend?","What's that smell?","This is the way the world ends / This is the way the world ends / Not with a bang but with _.","What is Batman's guilty pleasure?","TSA guidelines now prohibit _ on airplanes.","What ended my last relationship?","MTV's new reality show features eight washed-up celebrities living with _."]
        return random.choice(list1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                color = WHITE
        if event.type == pygame.MOUSEBUTTONUP:
            if rect.collidepoint(event.pos):
                color = BLACK
                s =get_string()

    pygame.draw.rect(window, color, rect)
    #txt.text_to_screen(window, s, 100, 100, 75, WHITE)
    txt.drawText(window,s,WHITE,rect,font,True)
    pygame.display.update()

pygame.quit()
