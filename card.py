class card:
    def __init__(self, cardId, cardText, cardType, playerId):
        self.cardId = cardId#unique identifier for each card
        self.cardText = cardText#the text on the front of the card
        self.cardType = cardType#indicates if the card is a question or an answer, used for graphics, question=b1/b2/b3, answer=wh
        self.playerId = playerId#for white cards, identifies which player answered with this card