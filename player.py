import card
class player:
    def __init__(self, playerId, gameId, playerName, playerHand, playerPos):
        self.playerId = playerId#integer, unique identifier for each player
        self.gameId = gameId#integer, unique identifier indicating the game this player is part of
        self.playerName = playerName#string, the name the player has selected
        self.playerHand = playerHand(card)#list holding the cards the player has in hand
        self.playerPos = playerPos#integer, player's position in the rotation