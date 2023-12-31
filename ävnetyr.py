import random as rand
import time

class Player:
    def __init__ (self, hjältenamn, hjältestyrka, hjälteliv, ryggsäck, level):
        self.namn = hjältenamn
        self.styrka = hjältestyrka
        self.liv = hjälteliv
        self.ryggsäck = ryggsäck
        self.level = level

class Monster:
    def __init__(self, namn, styrka, liv):
        self.namn = namn
        self.styrka = styrka
        self.liv = liv
        
def fälla(hjälte):
    slumptal = rand.randint(1,3)
    if slumptal == 1:
        slumptal = rand.randint (1,20)
        print("             Gissa ett tal, 1 - 20: ")
        antal_gissning = 1
        gissning = int(input("            Vad är din gissning?\n "))
        while gissning != slumptal:
            if gissning > slumptal:
                print("För stort! ")  
            else:
                print("För lågt! ")
            gissning = int(input("Vad är din gissning? "))
            antal_gissning += 1
        print(f"Talet var {slumptal}. Du gissa {antal_gissning} gånger.")
        time.sleep(2)   
        if antal_gissning <= 4:
            print("Du överlevde ")
            hjälte.level += 1
        else:
            print(f"Du gissade för många gånger och FÖRLORADE {antal_gissning} LIV")     
            hjälte.liv -= antal_gissning  
    elif slumptal == 2:
        print("STORY")
        print("Den som tillverkar mig behöver mig inte, den som köper mig använder mig inte, den som använder mig kan varken se eller känna mig. Vad är jag?")
        valet = input(
            """
            1. Yxa
            2. Sword
            3. Cocaine 
            4.Lik Kista
            """)
        
        if valet == 1 or valet == 2 or valet == 3: 
            print("Fel")
            hjälte.liv -= 5              
        else:
            print("Rätt")

    else:
        pass
    #fälla

def strid(hjälte, monster):

    print(f"O HElVETE! Du har gått in i ett rum med monstret {monster.namn}.\n Nu får vi se om du lever länge till\n")
    time.sleep(2)
    print(
    f"""
    {monster.namn}: 
    Har styrkan {monster.styrka} och har {monster.liv} liv.

    Du: 
    Har styrkan {hjälte.styrka} och {hjälte.liv} liv. \n
    """
    )
    time.sleep(2)
    valet = input(
    f"""
    Vad vill du göra?
        1. Strid som en hjälte
        2. Fly därifrån som en nolla
    """)
    stridljud_spelaren = ["haaaa! Haaa", "ditt jävla monster! DÖ", "Ojj", "du ska betala för det här", "mitt ansikte är det sista du ser", "smaka på mitt kalla järn", "ohhhhhaaa"]
    stridljud_monster = ["bwhhaaaa", "spspsspsps", "rlrlrlrl", "jahahdn", "hoaaaa"]
    if valet == "1":
        while hjälte.liv > 0 and monster.liv > 0:
            valt_ljud_spelaren = rand.choice(stridljud_spelaren)
            valt_ljud_monster = rand.choice(stridljud_monster)
            time.sleep(1)
            print(f"{hjälte.namn} slår monstret")
            time.sleep (1)
            print(f"    Du skriker {valt_ljud_spelaren}!\n") 
            time.sleep(1)
            print("Monstret slår dig")
            print(f"    Monstret {monster.namn} skriker {valt_ljud_monster}!\n") 
            hjälte.liv -= monster.styrka 
            monster.liv -= hjälte.styrka
            if hjälte.liv <= 0:
                time.sleep (1)
                print("Monstret var ditt slut!")
                return hjälte.liv
            else:
                time.sleep (1)
                print(f"""\nDu lyckades döda {monster.namn} monstret!
                                                               
                      """)
            return hjälte.liv
    elif valet == "2":
        print("     Ok fegis")
        return hjälte.liv
    else:
        print("     Lägg av")
 
def stats(hjälte):
    print(f"""
             {hjälte.namn}:
             liv    = {hjälte.liv}
             styrka = {hjälte.styrka}
             level = {hjälte.level}
""")
    
def beting(hjälte):
    slumptal = rand.randint (1,20)
    print("             Gissa ett tal, 1 - 20: ")
    antal_gissning = 1
    gissning = int(input("            Vad är din gissning?\n "))
    while gissning != slumptal:
        if gissning > slumptal:
         print("För stort! ")  
        else:
          print("För lågt! ")
        gissning = int(input("Vad är din gissning? "))
        antal_gissning += 1
    print(f"Talet var {slumptal}. Du gissa {antal_gissning} gånger.")
    time.sleep(2)
    if antal_gissning <= 4:
        kista (hjälte)
    else:
        print("Du gissade för många gånger och FÖRLORA")

def ryggsäck (hjälte):
    for föremål in hjälte.ryggsäck:
        print (f"Föremål: {föremål.namn} Styrka: {föremål.styrka}")

class Föremål():
    def __init__(self,namn,styrka,liv):
        self.namn = namn
        self.styrka = styrka
        self.liv = liv

def kista(hjälte):

    F1 = Föremål("träklubba",4,0)
    F2 = Föremål("Rostig dolk",2,0)  
    F3 = Föremål("Svärd",8,0)
    F4 = Föremål("träslev",12,5)
    F5 = Föremål("Farlig panna",6,0)  
    F6 = Föremål("Hårda ord",15,-4)
    F7 = Föremål("Toffel",5,0)
    F8 = Föremål("lycktstolpe",1,2)
    F9 = Föremål("Joint",0,10)
    F10 = Föremål("Bakade Bönor",0,2)
    F11 = Föremål("Melkers Mamma",5,8)


    items = [F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11]

    hittad = rand.choice(items)
    print(f"Du hittade {hittad.namn}. Den har {hittad.styrka} styrka och ger dig {hittad.liv} liv.")
    hjälte.ryggsäck.append(hittad)
    hjälte.styrka += hittad.styrka
    hjälte.liv += hittad.liv
 
def main():
    hjältenamn = input("vad ska du heta?\n")
    print(f"Var hälsad {hjältenamn} välkommen till Mumindalen")

    hjälte = Player(hjältenamn, 5, 20, [], 1)
             
    while hjälte.liv > 0:        
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
                slumptal = rand.randint(1,3)
                if slumptal == 1:
                    monster_namn = ["Abdul", "Jens", "Stenhårde Tomas", "Bertius"]
                    monster = Monster (rand.choice (monster_namn), rand.randint (1,10), rand.randint (15,25))
                    strid (hjälte, monster)                          
                elif slumptal == 2:
                    kista(hjälte)
                elif slumptal == 3:
                    print("Fälla")
                    fälla(hjälte)
                else: print("Fan gör du")
            
        elif val == "2":
            ryggsäck (hjälte)
        elif val == "3":
            stats(hjälte)
        elif val =="4":
            valet = input(
            """
            Vad vill du göra?
            För att vinna behöver du gissa på 4 eller mindre gånger ett tal mellan 1 - 20. 
            1. Gambla
            2. Inte gambla\n
            """)
            if valet == "1":
                beting(hjälte)
            elif valet == "2":
                print("Ok din tråkiga gubbe")
            else:
                print("Lägg av")
        elif val == "5":
            print("Det här spelet är gjorta av Arvid Folkesson och Erik Brodin.Vi vill tack all suport vi har fått under utvecklingens gång och kan glat säga att detta har varit en fantastisk upplevelse. ")
        else:
            print("Är du helt från vettet människa! Det finns bara 4 val, din idiot! BRYT INTE MATRIX!\n Välj 1, 2, 3 eller 4!")
    else:
        print("DU DOG :(")
main()