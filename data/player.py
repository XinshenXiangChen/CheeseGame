class Player:
    def __init__(self):
        self.hp = 100
        self.attack = 30
        self.full_hp = 100

        self.bar = 375
        self.full_bar = 375
        self.cheese = 0
        # self.equipped_object = {'weapon': None}

    def reset(self):
        self.hp = self.full_hp
        self.bar = self.full_bar