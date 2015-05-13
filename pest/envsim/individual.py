__author__ = 'Lucas Amaral'
import random

class Individual:
    health = " "
    power = 9
    movestatus = False
    infectionAbility = 0
    life = 0

    def __init__(self):
        opt = random.randint(0, 4)
        if opt <= 2:
            self.health = 'S'
            self.life = 10
            self.power = 0
        elif opt == 3:
            self.health = '*'
            self.life = 10
            self.power = 9
        elif opt == 4:
            self.health = '@'
            self.life = 4
            self.power = random.randint(0, 9)

    def killIndividual(self):
        self.setLife(0)
        self.health = 'X'
        self.power = 0
        self.infectionAbility = 0

    def setLife(self, newage):
        self.life = newage

    def infectIndividual(self, target):
        infectionPower = random.randint(1, 9)
        if target.health != 'O' and target.health != 'X':
            print("[%s P:%d I:%d] tentando infectar [%s P:%d I:%d] com %d de Poder de infecção" % (self.health, self.power, self.infectionAbility, target.health, target.power, target.infectionAbility, infectionPower), end=' | ')
            if self.infectionAbility:
                print("Virus Ativo", end=' | ')
                if target.power < infectionPower:
                    target.health = 'O'
                    target.infectionAbility = 0
                    if target.life > 3:
                        target.setLife(3)
                    print("Infectado")
                else:
                    print("Poder de Infecção insuficiente",)
            else:
                print("Virus Inativo")

    def decayLife(self):
        if self.life > 1:
            self.setLife(self.life - 1)
        else:
            self.killIndividual()