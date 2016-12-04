import pygame, txt, random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("SansitaOne.tff", 50)
font2 = pygame.font.SysFont("SansitaOne.tff", 30)
# Color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (190,190,190)
window_size = window_width, window_height = 1600,900
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Cards Against Humanity")
unit = 100
rect = pygame.Rect(30, 200, 2.5*unit, 3.5*unit)




window.fill(WHITE)

running = True
list1 = ["I got 99 problems but _ ain't one.", "What's a girl's best friend?",
         "This is the way the world ends / This is the way the world ends / Not with a bang but with _.",
         "TSA guidelines now prohibit _ on airplanes.",
         "MTV's new reality show features eight washed-up celebrities living with _."]

black_card_color = BLACK
black_card = "Cards Against Humanity"
#get_string gives black_card a value
def get_string():
        list1 = ["Why can't I sleep at night?","I got 99 problems but _ ain't one.","What's a girl's best friend?","What's that smell?","This is the way the world ends / This is the way the world ends / Not with a bang but with _.","What is Batman's guilty pleasure?","TSA guidelines now prohibit _ on airplanes.","What ended my last relationship?","MTV's new reality show features eight washed-up celebrities living with _."]
        return random.choice(list1)

def draw_users(userList):
    x = 30
    y = 30
    unit = 260
    counter = 0
    for u in userList:
           pygame.draw.rect(window,GRAY,(30+unit*counter,30,250,150))
           txt.drawText(window, black_card, BLACK, (30+unit*counter,30,250,150), font2, False)
           counter+=1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                black_card_color = WHITE
        if event.type == pygame.MOUSEBUTTONUP:
            if rect.collidepoint(event.pos):
                black_card_color = BLACK
                draw_users(list1)
                black_card =get_string()

    pygame.draw.rect(window, black_card_color, rect)
    #txt.text_to_screen(window, s, 100, 100, 75, WHITE)
    txt.drawText(window,black_card,WHITE,rect,font,True)
    pygame.display.update()

pygame.quit()
