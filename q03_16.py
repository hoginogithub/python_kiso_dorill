import random
from operator import attrgetter

class Character:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def __str__(self):
        return self.name + ': hp=' + str(self.hp) + ' mp:' + str(self.mp)

    def __setattr__(self, attr_name, attr_value):
        object.__setattr__(self, attr_name, attr_value)
        if attr_name in ['hp', 'mp']:
            if attr_value > getattr(self, 'max_' + attr_name):
                object.__setattr__(self, attr_name, getattr(self, 'max_' + attr_name))

            if attr_value < 0:
                object.__setattr__(self, attr_name, 0)


class Attacker(Character):
    def __init__(self, name, hp, mp, strength=1):
        Character.__init__(self, name, hp, mp)
        self.strength = strength

    def attack(self, target):
        print(self.name + 'の攻撃')
        target.hp -= self.strength
        print(target.name + 'はダメージを負った')        

class Healer(Character):
    def __init__(self, name, hp, mp, power=1):
        Character.__init__(self, name, hp, mp)
        self.power = power

    def heal(self, target):
        if self.mp > 2:
            print(self.name + 'は回復の魔法を使った')
            target.hp += self.power
            self.mp -= 2
        else:
            print(self.name + 'は、すでに回復の魔法が使えない')

class HealerAttacker(Healer, Attacker):
    def __init__(self, name, hp, mp, strength=1, power=1):
        Attacker.__init__(self, name, hp, mp, strength)
        self.power = power

def is_heal_chance(target):
    # print(target.name + ': hp=' + str(target.hp) + ' max_hp//2=' + str(target.max_hp // 2))
    if target.hp > (target.max_hp // 2):
        return False
    if hasattr(target, 'heale'):
        return False
    if target.mp < 2:
        print(target.name + 'は、すでに回復魔法は使えない')
        return False
    return True

players = [
    HealerAttacker('Alice', 20 ,15, 5, 8),
    HealerAttacker('Bob', 19, 20, 5, 9),
    HealerAttacker('Charlie', 18, 30, 9, 5)
]

'''
for i in range(0,10):
    players[0].heal(players[1])
    print(players[0])
    print(players[1])
'''

round = 0
while not([p.hp for p in players if p.hp == 0]):
    round += 1
    print('round' + str(round)+ '----')
    chose_player = []
    chose_player = random.sample(players, 2)
    if is_heal_chance(chose_player[0]):
        chose_player[0].heal(chose_player[0])
    else:
        chose_player[0].attack(chose_player[1])

print('----------------')
print('ゲーム終了')
for p in players:
    print(p)
