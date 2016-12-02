import card
import random

class player:
    def __init__(self, playerId, gameId, playerName, playerHand, playerPos, cardPool, handSize):
        self.playerId = playerId#integer, unique identifier for each player
        self.gameId = gameId#integer, unique identifier indicating the game this player is part of
        self.playerName = playerName#string, the name the player has selected
        self.playerHand = playerHand(card)#array holding the cards the player has in hand
        #playerHand variable will only be used for player on local machine, for all other players array will be empty
        self.playerPos = playerPos#integer, player's position in the rotation
        self.cardPool = cardPool(card)#array holding the cards the user can draw from, possibly temporary
        self.handSize = handSize#maxmimum amount of cards the player can have in hand

    def fillHand(self):#fills the player's hand with new cards
        if len(self.playerHand) < self.handSize:
            self.playerHand.append(self.cardPool.pop(random.randrange(0, len(self.cardpool))))
            self.fillHand()

    def fetchCards(self):#fetch the pool of cards this player will use
        todo = True