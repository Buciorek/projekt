import random




def information():
    print(
        "Du valde information om spelet:\n"
        "Spelet var skapat av tre gudar som började sitt arbete under en programmeringslektion. "
        "Gruppen består av tre nördar med en passion för spelutveckling och en dröm om att skapa fler spel i framtiden."
        "Själva idén till spelet och dess namn kommer från Saint Arvid som är huvudutvecklare  (Main Developer)."
        "De andra medlemmarna i gruppen bidrog med design, kodning och testning för att tillsammans skapa något unikt och roligt. "
        "Gruppen ser detta projekt som ett första steg mot att förverkliga sin gemensamma vision om att bli framgångsrika spelutvecklare."
    )

    print()

    tillbaka = input("Vill du gå tillbaka till start meny? [Ja/Nej] ---> ")
    
    if tillbaka in ["Ja", "ja", "jA", "JA"]:
        print()
        print_meny()
    else:
        print()
        print("Vi slår ut informationen igen!!!")
        print()
        information()



def starta_spel():
    print()
    Huvudnamn = input ("Välj ditt namn: ---> ")
    print()

    print(f"Hej {Huvudnamn}, välkommen till spelet")
    print()
    print("=== SPELINTRO ===")
    print(f"{Huvudnamn}, du är mitt ute i naturen, du märker att det är ett åskoväder påväg till dig")
    print("Du ser en gråtta, du går in i den för att vänta på att åskovädret ska sluta")
    print("Du inser att grottan magiskt stänger sig, och helt plötsligt är du under jorden")


    print()

    startspel()
    






statestik = {
    "hp": 100,
    "styrka": 0,
    "level": 1,  
    "inventory": []
}

items_to_drop_boa = [
    {"name": "Vapen: Arvidus", "strength_bonus": 2},
    {"name": "Vapen: Arvidinho", "strength_bonus": 3},
    {"name": "Vapen: Arvidzilla", "strength_bonus": 5},
    {"name": "Vapen: Arvidanator", "strength_bonus": 4},
    {"name": "Vapen: Arvidito", "strength_bonus": 1},
    {"name": "Vapen: Arvidinator", "strength_bonus": 3},
    {"name": "Vapen: Arvidski", "strength_bonus": 4},
    {"name": "Vapen: Arvidicus", "strength_bonus": 2},
    {"name": "Vapen: Arvidlito", "strength_bonus": 3},
    {"name": "Vapen: Mbappape", "strength_bonus": 5},
]

def visa_statistik():
    print(
        f"Dina statestik:\n"
        f"Ditt hp är {statestik['hp']}\n"
        f"Din styrka är {statestik['styrka']}\n"
        f"Din level är {statestik['level']}"
    )
    print()


def visa_inventory():
    if not statestik["inventory"]:
        print("Ditt inventory är tomt.")
    else:
        print("Ditt inventory innehåller:")
        for item in statestik['inventory']:
            print(f"- {item['name']} (Styrkebonus: {item['strength_bonus']})")
    print()

def uppdatera_styrka():
    statestik["styrka"] = sum(item["strength_bonus"] for item in statestik["inventory"])


def hitta_kista():
    item = random.choice(items_to_drop_boa)

    if len(statestik["inventory"]) < 5:
        statestik["inventory"].append(item)
        print(f"Du hittade en kista! Den innehåller {item['name']} med styrkan +{item['strength_bonus']}.")
    else:
        print(f"Du hittade en kista! Den innehåller {item['name']} med styrkan +{item['strength_bonus']}.")
        print()
        print("Ditt inventory är fullt. Du måste byta ut ett föremål (Du får max ha 5 saker i ditt inventory).")
        visa_inventory()
        
        while True:
            try:
                replace_index = int(input("Ange vilket föremål du vill byta ut (1-5), eller 0 för att fortsätta utan att byta ut något vapen ")) - 1

                if replace_index == -1:  
                    print("Föremålet lämnas kvar i kistan och du fortsätter gå fram.")
                    return
                elif 0 <= replace_index < len(statestik["inventory"]):
                    replaced_item = statestik["inventory"][replace_index]
                    statestik["inventory"][replace_index] = item
                    print(f"{replaced_item['name']} har bytts ut mot {item['name']}.")
                    break
                else:
                    print("FEL VAL. Välj ett nummer mellan 0 och 5.")
            except ValueError:
                print("FEL VAL. Välj ett nummer mellan 0 och 5.")
    
    uppdatera_styrka()
    print()


def falla():
    falla_damage = random.randint(2, 10)
    statestik["hp"] -= falla_damage

    print(f"\nDu gick i en fälla och förlorade {falla_damage} HP!")

    if statestik["hp"] <= 0:
        print("Du har förlorat allt dit HP. Spelet är över")







def valj_dorr():
    print("Välj en dörr att gå in")
    print("[1] Dörr till vänster\n[2] Dörr rakt fram\n[3] Dörr till höger")

    door_chocie = int(input("Väl en dörr mellan (1-3): "))
        
    if door_chocie not in [1, 2, 3]:
        print()
        print("Fel svar, fösök igen!!")
        print()
        return valj_dorr()
    
    event = random.choice(["monster", "kista", "fälla"])

    if event == "monster":
        monster_strid()
    elif event == "kista":
        hitta_kista()
    elif event == "fälla":
        falla()



def monster_strid():
    monster_strength = random.randint(3, 15)
    player_strength = statestik["styrka"] + sum(item["strength_bonus"] for item in statestik["inventory"])
    
    print(f"\nDu ska strida mot ett monster med styrka {monster_strength}!")
    if monster_strength > player_strength:
        hp_loss = random.randint(5, 10)
        statestik["hp"] -= hp_loss
        print("Monstret vann! Du förlorade 10 HP.")
    elif monster_strength < player_strength:
        statestik["level"] += 1
        styrka_bonus = random.randint(1, 2)
        statestik["styrka"] += styrka_bonus
        print(f"Du vann över monstret och gick upp en nivå! Du fick också +{styrka_bonus} i styrka.")
    else:
        print("Striden slutade oavgjort.")

    if statestik["hp"] <= 0:
        print("Du har förlorat all HP. Spelet är över.")

    print()



def startspel():
    while statestik["level"] < 10 and statestik["hp"] > 0:
        print("Välj ett alternativ:\n[1] Gå vidare\n[2] Ryggsäck\n[3] Statistik\n")

        try:
            vilketalternativ = int(input("Välj ett tal mellan 1-3 --->  "))
            print()
            if vilketalternativ not in [1, 2, 3]:
                raise ValueError 
        except ValueError:
            print("Ogiltigt alternativ, försök igen!")
            continue

        if vilketalternativ == 1:
            valj_dorr()
        elif vilketalternativ == 2:
            visa_inventory()
        elif vilketalternativ == 3:
            visa_statistik()

    if statestik["level"] >= 10:
        print("Grattis! Du van spelet, ses någon annan gång")
    

def print_meny():

    welcome_text = r"""
     _    ___   _ ______                                 __  _ ____   __  __          __          _                __         
    | |  / (_)_(_) / / /______  ____ ___  ___  ____     / /_(_) / /  / / / /___  ____/ /__  _____(_)___  _________/ /__  ____ 
    | | / / __ `/ / / //_/ __ \/ __ `__ \/ _ \/ __ \   / __/ / / /  / / / / __ \/ __  / _ \/ ___/ / __ \/ ___/ __  / _ \/ __
    | |/ / /_/ / / / ,< / /_/ / / / / / /  __/ / / /  / /_/ / / /  / /_/ / / / / /_/ /  __/ /  / / /_/ / /  / /_/ /  __/ / / /
    |___/\__,_/_/_/_/|_|\____/_/ /_/ /_/\___/_/ /_/   \__/_/_/_/   \____/_/ /_/\__,_/\___/_/__/ /\____/_/   \__,_/\___/_/ /_/ 
                                                                                           /___/                              

    """
    print(welcome_text)
    print()

    while True:
        print(f"Välkomen till underjordens hemligheter: \n[1] Start spelet  \n[2] Information om skaparna \n[3] En annan gång")
        print()
        menytal = int(input("Välj ett tal mellan 1-3 -->  "))

        if menytal == 1:
            starta_spel()
            break
        elif menytal == 2:
            information()
            break
        elif menytal == 3:
            print("Tack för din uppmärkasamhet, ses någon annan gång")
            break
        else:

            print("Fel tal, välj igen:")
            print()


print_meny()