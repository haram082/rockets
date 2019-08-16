class Card(object):
    cardtype='Staff'
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack= attack
        self.defense= defense
    def power(self, other_card):
        return (self.attack-self.defense)/2


    
