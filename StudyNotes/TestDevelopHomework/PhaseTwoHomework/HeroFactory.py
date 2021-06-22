from StudyNotes.TestDevelopHomework.PhaseTwoHomework.Jinx import Jinx
from StudyNotes.TestDevelopHomework.PhaseTwoHomework.Timo import Timo


class HeroFactory:
    def createHero(self,hero_HP,hero_power,hero_name):
        if hero_name == "Jinx":
            return Jinx(hero_HP,hero_power,"Jinx")
        elif hero_name == "Timo":
            return Timo(hero_HP,hero_power,"Timo")
        else:
            print("此人不在此人物传")


heroFactory = HeroFactory()
jinx = heroFactory.createHero(1000,100,"Jinx")
timo = heroFactory.createHero(500,800,"Timo")
jinx.fight(timo.hero_HP,timo.hero_power,timo.hero_name)
