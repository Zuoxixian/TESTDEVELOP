class Hero:
    hero_HP = 0
    hero_power = 0
    hero_name = ""

    def __init__(self,hero_HP, hero_power,hero_name):
            self.hero_HP = hero_HP
            self.hero_power = hero_power
            self.hero_name = hero_name

    def fight(self, enemy_hp, enemy_power, enemy_name):
        heroResidueHP = self.hero_HP - enemy_power
        enemyResidueHP = enemy_hp - self.hero_power

        if heroResidueHP > enemyResidueHP:
            return print(f"{self.hero_name}" + "获胜")
        elif heroResidueHP < enemyResidueHP:
            return print(f"{enemy_name}" + "获胜")
        else:
            return print("平局")

# class Jinx(Hero):
#     hero_HP = 1000
#     hero_power = 210
#     hero_name = "Jinx"
#
# class Timo(Hero):
#     hero_HP = 600
#     hero_power = 500
#     hero_name = "Timo"

#jinx = Jinx()
#timo = Timo()
# jinx.fight(timo.hero_HP,timo.hero_power,timo.hero_name)