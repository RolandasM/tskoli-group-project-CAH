#main running file for Cards Against Humanity pycharm game
import player
import card
import random

gameState = "" #identifies current game state:
#menu = user is in the menu
#lobby = user is in the game lobby, ready to enter a game
#newround = a new round is starting, used to prep game for new round
#qna = a question is being asked and players are answering
#choice = all answers have been entered and the asking player is choosing the winning entry
#gameend = the game has ended, scores are tallied
#quit = user has chosen to quit the game

drawArr = [](str)#
roundPos = 0#the current round position in the game, from 0 to however many players are in the game
bigBlackDeck = [](card)#the deck holding the black cards. the deck is really big and really black
players = [](player)#array of players in the user's game, used for drawing the game. to be populated by the server
userId = 0#temporary value, user will be assigned an ID by the server

#
#main game loop
#
while gameState != "quit":
    a=1#temporary to stop error

    #drawBase()
    #if gameState == 'r':#
    #   players[userId].fillHand()
    #   gameState = 'a'

def newBlackCard(bigBlackDeck):#draws a new black card from the deck
    if len(bigBlackDeck) > 0:
        return bigBlackDeck.pop(random.randrange(0, len(bigBlackDeck)))
    else:
        error("flaccidblackdeck")#error, bigBlackDeck array is empty

def error(errorCode):#takes error codes and displays appropriate message
    if errorCode == "flaccidblackdeck":#error, bigBlackDeck array is empty
        print("no cards present in black deck")
