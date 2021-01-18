from inheritance1 import viking_warrior


class berserker(viking_warrior):
    def rage_attack(self):
        print("A flurry of unstoppable attacks with an axe")

    def throw_axe(self):
        print("Ranged attack: Axe throw")

    def run_and_jump(self):
        print("The berserker sprints and leaps forward a "
              "great distance")


myWarrior = viking_warrior()
myBerserker = berserker()

myBerserker.swing_sword()
myWarrior.shoot_arrow()
myBerserker.rage_attack()
myWarrior.swing_sword()
myBerserker.throw_axe()
myWarrior.run_and_jump()
myBerserker.run_and_jump()
