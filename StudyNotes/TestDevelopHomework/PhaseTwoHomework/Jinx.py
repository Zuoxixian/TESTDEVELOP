from StudyNotes.TestDevelopHomework.PhaseTwoHomework.Hero import Hero

class Jinx(Hero):
    hero_HP = 0
    hero_power = 0
    hero_name = ""

    # def __init__(self,hero_HP, hero_power,hero_name):
    #     self.hero_HP = hero_HP
    #     self.hero_power = hero_power
    #     self.hero_name = hero_name


    # def set_Jinx_HP(self,Jinx_HP):
    #     self.Jinx_HP = Jinx_HP
    # def set_Jinx_Power(self,Jinx_Power):
    #     self.Jinx_Power = Jinx_Power
    # def set_Jinx_name(self,Jinx_name):
    #     self.Jinx_name = Jinx_name

    # def fight(self, enemy_hp,enemy_power,enemy_name):
    #     JinxResidueHP = self.Jinx_HP - enemy_power
    #     enemyResidueHP = enemy_hp - self.Jinx_Power
    #
    #     if JinxResidueHP > enemyResidueHP :
    #         return print(f"{self.Jinx_name}" + "获胜")
    #     elif JinxResidueHP < enemyResidueHP :
    #         return print(f"{enemy_name}获胜")
    #     else :
    #         return print("平局")



# class Timo(Hero):
#     Timo_HP = 500
#     Timo_Power = 900
#
#     def __init__(self):
#         self.Timo_name = "Timo"

    # def Timo_fight(self, enemy_hp,enemy_power):
    #     TimoResidueHP = self.Timo_HP - enemy_power
    #     enemyResidueHP = enemy_hp - self.Timo_Power
    #
    #     if TimoResidueHP > enemyResidueHP :
    #         return print(f"{self.Timo_name}" + "获胜")
    #     elif TimoResidueHP < enemyResidueHP :
    #         return print("敌人获胜")
    #     else :
    #         return print("平局")

# jinx = Jinx()
# jinx.Jinx_fight(Timo.Timo_HP,Timo.Timo_Power,"Timo")