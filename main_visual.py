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
rect = pygame.Rect(30, 200, 250, 350)

answers = ["Steve;Man meat.;A sad handjob.",
           "Bob;A micropenis.;Panda sex.",
           "Michael;Preteens.;Pixelated bukkake.",
           "xxNoscopez;Keanu Reeves.;Britney Spears at 55."]
answers2 = ["YOU MUST CONSTRUCT ADDITIONAL PYLONS.;Steve","Being rich.;Bob", "Preteens.;Michael", "Nipple blades.;xxNoscopezzZxx"]




window.fill(GRAY)

running = True
list1 = ["During sex, I like to think about _.", "What did I bring back from Mexico?",
         "What's there a ton of in heaven?",
         "TSA guidelines now prohibit _ on airplanes.",
         "MTV's new reality show features eight washed-up celebrities living with _.", "What never fails to liven up the party?", "When I was tripping on acid, _ turned into _."]
user_list = ["Steve", "Bob", "Michael", "xxNoscopez", "Barry"]
white_card_list = ["A good sniff.", "Pedophiles.", "72 virgins.","A stray pube.", "A brain tumor.", "Stephen Hawking talking dirty."]
white_card_rect_list = []
answer_rect_list = []
black_card_color = BLACK
black_card_text = "Cards Against Humanity"
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
#get_string gives black_card a value
def get_string():
        return random.choice(list1)

def draw_users(userList):
    unit = 260
    counter = 0

    for u in userList:
           pygame.draw.rect(window,WHITE,(30+unit*counter,30,250,150))
           txt.drawText(window, u, BLACK, (30+unit*counter,30,250,150), white_card_font, True)
           counter= counter + 1

def draw_white_cards(cards):
    unit = 260
    counter = 0
    for c in cards:
           white_card_rect_list.append(pygame.draw.rect(window,WHITE,(30+unit*counter,670,250,200)))
           txt.drawText(window, c, BLACK, (30+unit*counter,670,250,200), white_card_font, True)
           counter+=1


draw_white_cards(white_card_list)
draw_answers(answers)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                black_card_color = WHITE
        if event.type == pygame.MOUSEBUTTONUP:
            temp = 0
            print(len(answer_rect_list))
            for a in answer_rect_list:
               if a.collidepoint(event.pos):
                   black_card_text = answers[temp].split(';')[0]+" wins!"
                   print(answers[temp].split(';')[0]+" wins!")
               temp = temp + 1
            temp = 0
            for c in white_card_rect_list:
                if c.collidepoint(event.pos):
                    black_card_color = BLACK
                    black_card_text = white_card_list[temp]
                temp = temp + 1

            if rect.collidepoint(event.pos):
                black_card_color = BLACK
                draw_users(user_list)
                black_card_text =get_string()

    pygame.draw.rect(window, black_card_color, rect)
    #txt.text_to_screen(window, s, 100, 100, 75, WHITE)
    txt.drawText(window,black_card_text,WHITE,rect,black_card_font,True)
    pygame.display.update()

pygame.quit()
