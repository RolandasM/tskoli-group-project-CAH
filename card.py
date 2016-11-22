class card:
    def __init__(self, cardId, cardText, cardType):
        self.cardId = cardId#unique identifier for each card
        self.cardText = cardText#the text on the front of the card
        self.cardType = cardType#indicates if the card is a question or an answer, used for graphics