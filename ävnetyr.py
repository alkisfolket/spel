import random as rand
import time
class Spelare():
    def __init__(self,name):
        self.name = name 
        self.styrka = 100
        self



class Monster():
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.styrka = rand.randint(0,5)
        self.liv = rand.randint(1,50)

M1 = Monster("Eld", "Jonas")
M2 = Monster("Vatten", "Lennart")
M3 = Monster("Luft", "Stina")
M4 = Monster("jord", "Pelle")
M5 = Monster("invandraren","Abdull")    
monsters=[M1,M2,M3,M4,M5]


class Föremål():
    def __init__(self,name,):
        self.name = name
        self.styrka = rand.randint(1,20)

F1 = Föremål("träklubba")
F2 = Föremål("Rostig dolk")  
F3 = Föremål("Svärd")      

items = [F1,F2,F3]

class Kista():
    def __init__(self):
        pass

class Fälla():    
    def __init__(self):
        pass

def strid(hjältehp, hjältestyrka, hjältenamn):
    random_monster = rand.choice(monsters)
    monsterhp = random_monster.liv
    print(f"O HElVETE! Du har gått in i ett rum med {random_monster.name}.\n Nu får vi se om du lever länge till")
    valet = input(
    """
    Vad vill du göra?
        1. Strid som en hjälte
        2. Fly därifrån som en nolla
    """)
    stridljud_spelaren = ["haaaa! Haaa!", "ditt jävla monster! DÖ!", "Ojj", "du ska betala för det här", "mitt ansikte är det sista du ser!!", "smaka på mitt kalla järn", "ohhhhhaaa"]
    stridljud_monster = ["bwhhaaaa", "spspsspsps", "rlrlrlrl", "jahahdn", "hoaaaa"]
    if valet == "1":
        while hjältehp > 0 and monsterhp > 0:
            valt_ljud_spelaren = rand.choice(stridljud_spelaren)
            valt_ljud_monster = rand.choice(stridljud_monster)
            time.sleep(2)
            print("Du slår monstret")
            print(f"    {hjältenamn} skriker {valt_ljud_spelaren}") 
            time.sleep(2)
            print("Monstret slår dig")
            print(f"    Monstret {random_monster.name} skriker {valt_ljud_monster}") 
            hjältehp -= random_monster.styrka 
            monsterhp -= hjältestyrka
            if hjältehp <= 0:
                print("Monstret var ditt slut!")
            elif monsterhp <= 0:
                print(f"\nDu lyckades dödada {random_monster.name} monstret!")
            return hjältehp
    elif valet == "2":
        print("Ok fegis")
        return hjältehp
    else:
        print("Lägg av")
 
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
        if gissning > 16 or gissning < 0:
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

ryggsäck = []
def kista():
    hittad = rand.choice(items)
    print(f"Du hittade{hittad.name}. Den har{hittad.styrka}styrka")
    ryggsäck.append(hittad)
 
def main():
 
    hjältehp = 100
    hjältestyrka = 5
    rädlsa = 0
    hjältenamn = input("vad ska du heta?")
    print(f"Var hälsad {hjältenamn} välkommen till Mumindalen")
             
    while hjältehp > 0:        
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
            print(""" 
                  1. Mossig trädörr
                  2. Rostig metalldörr
                  3. Stendörr
                  """)
            
            dörr = (input(""))
            if dörr == "1" or dörr == "2" or dörr == "3":
                slumptal = rand.randint(1,2)
                if slumptal == 1:
                    hjältehp = strid(hjältehp,hjältestyrka, hjältenamn)                          
                elif slumptal == 2:
                    kista()
                    #inte klar behöver fälla
                else: print("Fan gör du")
            
        elif val == "2":
            print()
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