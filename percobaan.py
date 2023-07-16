class Hero:
    def __init__(self,name,health,attack,energy):
        self.name = name
        self.health = health
        self.attack = attack
        self.energy = energy
        


    def serang(self,lawan):
        print(f"{'='*50}\n{self.name} menyerang {lawan.name}")
        lawan.diserang(self)
        

    def diserang(self,selff):
        print(f"{self.name} diserang {selff.name}") 
        self.show(selff)


    def show(diserang,menyerang):
        diserang.health -= menyerang.attack
        menyerang.energy -= (menyerang.attack // 2)


        
        if diserang.health >= 0:
            print(f"{'='*25} show info {'='*25}\ndarah {diserang.name} tersisa: {diserang.health}")
            print(f"energy {menyerang.name} tersisa: {menyerang.energy}")
        elif diserang.health <= 0:
            print(f"{diserang.name} diee")

cianch = Hero("Cianch",100,7,25)
balence = Hero("Balence",100,15,17)
suisin = Hero("Suisin",100,10,25)
minvac = Hero("Minvac",100,10,25)

cianch.serang(suisin)








