class Character:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

class Attacker(Character):
    def __init__(self, name, hp, mp, strength=1):
        Character.__init__(self, name, hp, mp)
        self.strength = strength

    def attack(self, target):
        target.hp -= self.strength

class Healer(Character):
    def __init__(self, name, hp, mp, power=1):
        Character.__init__(self, name, hp, mp)
        self.power = power

    def heal(self, target):
        if self.mp > 2:
            target.hp += self.power
            self.mp -= 2

class HealerAttacker(Healer, Attacker):
    def __init__(self, name, hp, mp, strength=1, power=1):
        Attacker.__init__(self, name, hp, mp, strength)
        self.power = power

players = [
    Character('Zeta', 5, 4),
    Attacker('Alice', 20 ,30, 5),
    Healer('Bob', 15, 20, 5),
    HealerAttacker('Charlie', 45, 30, 10, 10)
]

attack_player = [character for character in players if hasattr(character, 'attack')]
print(len(attack_player))

print(HealerAttacker.mro())
print(Character in HealerAttacker.mro())