#main running file for Cards Against Humanity pycharm game
import card

Playing = True#set to false to stop game
UserAnswering = True#value determining if the user is the one answering questions or questioning
CardsInHand = [](int)#array/list holding the id of the cards the user has in hand
Library = [](card)#array/list holding the cards in the game and their texts

while Playing:#main game loop
    a = 1
