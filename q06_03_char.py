class Character:
    def __init__(self, name='', hp=0, mp=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def __str__(self):
        return f'name={self.name} hp={self.hp} mp={self.mp}'
