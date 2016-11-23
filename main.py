#main running file for Cards Against Humanity pycharm game
import player
import card
import random

gameState = ''#identifies current game state, m=menu, l=lobby, r=new round, q=user is asking, a=user is answering and q=quit
bigBlackDeck = [](card)#the deck holding the black cards. the deck is really big and really black
players = [](player)#array of players in the user's game, used for drawing the game. to be populated by the server
userId = 0#temporary value, user will be assigned an ID by the server

while gameState != 'q':#main game loop
    a=1#temporary to stop error

    #drawBase()
    #if gameState == 'r':
    #   drawHand(players[userId])#

def newBlackCard(bigBlackDeck):#draws a new black card from the deck
    if len(bigBlackDeck) > 0:
        return bigBlackDeck.pop(random.randrange(0, len(bigBlackDeck)))
    else:
        error("flaccidblackdeck")

def error(errorCode):#takes error codes and displays appropriate message
    if errorCode == "flaccidblackdeck":
        print("no cards present in black deck")
