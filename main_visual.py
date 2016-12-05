import pygame, txt, random

pygame.init()
pygame.font.init()
black_card_font = pygame.font.SysFont("SansitaOne.tff", 40)
white_card_font = pygame.font.SysFont("SansitaOne.tff", 35)
# Color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (190,190,190)

window_size = window_width, window_height = 1600,900
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Cards Against Humanity")


black_card_rect = pygame.Rect(30, 200, 250, 350)

#sample answers list, up to 4 items, format "nickname;answer1;answer2" or "nick;answer"
answers = ["Steve;Man meat.;A sad handjob.",
           "Bob;A micropenis.;Panda sex.",
           "Michael;Preteens.;Pixelated bukkake.",
           "xxNoscopez;Keanu Reeves.;Britney Spears at 55."]

#background color
window.fill(GRAY)

running = True
#this is black card list, it is used in get_string function to get a random string out into the black card. Can be completely replaced by something else
#just set black_card_text to the value you want
list1 = ["During sex, I like to think about _.",
         "What did I bring back from Mexico?",
         "What's there a ton of in heaven?",
         "TSA guidelines now prohibit _ on airplanes.",
         "MTV's new reality show features eight washed-up celebrities living with _.",
         "What never fails to liven up the party?",
         "When I was tripping on acid, _ turned into _."]


user_list = ["Steve", "Bob", "Michael", "xxNoscopez", "Barry"]

white_card_list = ["A good sniff.", "Pedophiles.", "72 virgins.","A stray pube.", "A brain tumor.", "Stephen Hawking talking dirty."]

#these are used to store all the rect positions, which get made in the draw functions. Used for collision detection with mouse(clicks)
white_card_rect_list = []
answer_rect_list = []

black_card_text = "Cards Against Humanity"

#intakes answers, splits it up and shows the info in the center of the screen
def draw_answers(answers):
    counter = 0
    counter2 = 0
    counter3 = 0
    unit = 520
    unit2 = 260
    for a in answers:
        if len(a.split(';')) == 2:
            answer_rect_list.append(pygame.draw.rect(window, WHITE, (290 + unit * counter, 200+ counter2*180, 510, 170)))
            txt.drawText(window, a.split(';')[1], BLACK, (290 + unit * counter, 200+ counter2*180, 510, 170), white_card_font, True)
            counter = counter + 1
            if counter == 2:
                counter2 = counter2 + 1
                counter = 0
        else:
            answer_rect_list.append(pygame.draw.rect(window, WHITE, (290 + unit * counter3, 200 + counter2 * 180, 510, 170)))
            txt.drawText(window, a.split(';')[1], BLACK, (290 + unit2 * counter, 200 + counter2 * 180, 255, 170),
                         white_card_font, True)
            counter = counter + 1
            txt.drawText(window, a.split(';')[2], BLACK, (290 + unit2 * counter, 200 + counter2 * 180, 255, 170),
                         white_card_font, True)
            counter = counter + 1
            counter3 = counter3 + 1
            if counter3 == 2:
                counter2 = counter2 + 1
                counter = 0
                counter3 = 0
            if counter == 4:
                counter2 = counter2 + 1
                counter = 0
#get_string gives black_card a value, temporary sample, to be replaced
def get_string():
        return random.choice(list1)

#draws users on to the top of the screen
#intakes list of users (string)
def draw_users(userList):
    unit = 260
    counter = 0

    for u in userList:
           pygame.draw.rect(window,WHITE,(30+unit*counter,30,250,150))
           txt.drawText(window, u, BLACK, (30+unit*counter,30,250,150), white_card_font, True)
           counter= counter + 1

#draws white cards at the bottom of the screen
#intakes list of cards (string)
def draw_white_cards(cards):
    unit = 260
    counter = 0
    for c in cards:
           white_card_rect_list.append(pygame.draw.rect(window,WHITE,(30+unit*counter,670,250,200)))
           txt.drawText(window, c, BLACK, (30+unit*counter,670,250,200), white_card_font, True)
           counter+=1

#drawing everything with sample lists
draw_white_cards(white_card_list)
draw_answers(answers)
draw_users(user_list)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            #temp used for indexing through the rect lists for collision, please ignore
            temp = 0
            #checks which of the 4 answer fields has been clicked
            for a in answer_rect_list:
               if a.collidepoint(event.pos):
                   #this sets black card to the username of the player whose answers were selected
                   #should add points to that players score, black_card_text to be removed, used for testing only
                   black_card_text = answers[temp].split(';')[0]+" wins!"
               temp = temp + 1
            #same here, used for index, ignore
            temp = 0
            #collision detection for the white cards in your hand
            for c in white_card_rect_list:
                if c.collidepoint(event.pos):
                    #sets black_card_text to the white card that has been clicked, used for testing only
                    #to be replaced with game logic, somehow sent to the other users.
                    black_card_text = white_card_list[temp]
                temp = temp + 1
            #collision for the black card, used to get a string from the get string function, this whole section should
            #this and the get_string function should be replaced with a server request for a unique black card every turn.
            if black_card_rect.collidepoint(event.pos):
                black_card_text =get_string()
    #draws the black card on to the screen
    pygame.draw.rect(window, BLACK, black_card_rect)
    #draws the white text onto the black card
    txt.drawText(window,black_card_text,WHITE,black_card_rect,black_card_font,True)

    pygame.display.update()
pygame.quit()
