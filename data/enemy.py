class Enemy:
    def __init__(self, hp, attack, full_hp, cheese_drop):
        self.attack = attack
        self.full_hp = full_hp
        self.hp = hp

        self.bar = 60

        self.cheese_drop = cheese_drop