class Card(object):
    cardtype='Staff'
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack= attack
        self.defense= defense
    def power(self, other_card):
        return (self.attack-self.defense)/2
class Player(object):
    def __init__(self, deck, name):
        self.deck=deck
        self.name=name
    def play(self, card_index):
        self.deck.remove(card_index)
    
