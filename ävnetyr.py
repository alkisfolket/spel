import random as rand

class Monster():
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.styrka = rand.randint(0,10)
        self.liv = rand.randint(1,100)

M1 = Monster("Eld", "Jonas")
M2 = Monster("Vatten", "Lennart")
M3 = Monster("Luft", "Stina")
M4 = Monster("jord", "Pelle")
M5 = Monster("invandraren","Abdull")    
monsters=[M1,M2,M3,M4,M5]


class Föremål():
    def __init__(self,type,):
        self.type = type
        self.styrka = rand.randint(1,20)

F1 = Föremål("träklubba")
F2 = Föremål("Rostig dolk")        
class Kista():
    def __init__(self):
        pass

class Fälla():    
    def __init__(self):
        pass

def strid(hjältehp, hjältestyrka,monster):
    stridljud = ["Haaaa! Haaa!", "Ditt jävla monster! DÖ!", "Ojj", "Du ska betala för det här", "Mitt ansikte är det sista du ser!!", "Smaka på mitt kalla järn", "Ohhhhhaaa"]
   
    random_monster = rand.choice(monsters)
    monsterhp = random_monster.liv

    while hjältehp > 0 and monsterhp > 0:
        valt_ljud = rand.choice(stridljud)
        print(valt_ljud)
        stridljud.remove(valt_ljud) 
        hjältehp -= random_monster.styrka 
        monsterhp -= hjältestyrka
        if hjältehp <= 0:

            print("Monstret var ditt slut!")
        elif monsterhp <= 0:
            print("Du dödade monstret!")

    return hjältehp

 
def stats(hp,styrka,rädd):
    print(f"""
             liv = {hp}
             styrka = {styrka}
             rädsla = {rädd}
           
           """
         
          )
    
def slump():
    slumptal = rand.randint (1,15)
    print("Gissa ett tal, 1 - 15: ")
    antal_gissning = 1
    gissning = int(input("Vad är din gissning? "))
    while gissning != slumptal:
        if gissning > 10 or gissning < 1:
         print ("Lägg av! ")  
        elif gissning > slumptal:
         print("För stort! ")  
        else:
          print("För lågt! ")
        gissning = int(input("Vad är din gissning? "))
        antal_gissning += 1
    print(f"RÄTT! talet jag tänkte på var {slumptal}. Du gissa du så här många gånger {antal_gissning}")
    if antal_gissning < 4:
        print("Bra skit")
        #Not done here 

def main():

    
   

    hjältenamn = input("vad ska du heta?")
    print(f"Var hälsad {hjältenamn} välkommen till Mumidalen")
             
    hjältehp = 100
    hjältestyrka = 1
    rädlsa = 0

    ryggsäck = []

    while hjältehp >= 0:        
        print(
            """

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            4. Beta
            5. Credits
            
            """)
        
        val = input("")

        if val == "1":
            monster = rand.choice(monsters)
            hjältehp = strid(hjältehp,hjältestyrka, monster)
        elif val == "2":
            pass
        elif val == "3":
            stats(hjältehp,hjältestyrka,rädlsa)
        elif val =="4":
            valet = input(
            """
            Vad vill du göra?
            För att vinna behöver du gissa på 4 eller mindre gånger ett tal mellan 1 - 20. 
            1. Gambla
            2. Inte gambla
            """)
            if valet == "1":
                slump()
            elif valet == "2":
                print("Ok din tråkiga jävel")
            else:
                print("Lägg av")


        elif val == "5":
            print("Det här spelet är gjorta av Arvid Folkesson och Erik Brodin.Vi vill tack all suport vi har fått under utvecklingens gång och kan glat säga att detta har varit en fantastisk upplevelse. ")

        else:
            print("Är du helt från vettet det finns bara 4 val, din idiot! BRYT INTE MATRIX")
            print("Välj 1, 2, 3 eller 4!")

main()