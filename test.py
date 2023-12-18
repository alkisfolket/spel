import random as rand

ryggsäck = []
def kista():
    hittad = rand.choice(items)
    print(f"Du hittade {hittad.name}. Den har {hittad.styrka} styrka")
    ryggsäck.append(hittad)


class Föremål():
    def __init__(self,name):
        self.name = name
        self.styrka = rand.randint(1,20)

F1 = Föremål("träklubba")
F2 = Föremål("Rostig dolk")  
F3 = Föremål("Svärd")      

items = [F1,F2,F3]

def main():
    print
