MIN_SPELLS = 0
MAX_HP = 500

class Wizard:
    def __init__(self, hp, name, spell, again):
        self.hp = hp
        self.name = name
        self.spell = spell
        self.again = again

    def ask_action(self, player):
        while True:
            action = input("What action do you want to use, " + player + "? ")
            actions = ["1", "2", "3"]
            if action in actions:
                break
        return action

    def attack(self, name, hp, spell, player, again):
        if spell > MIN_SPELLS:
            hp = int(hp)
            hp -= 50
            spell -= 1
            print(name + " HP: " + str(hp))
            print(player + " has " + str(spell) + " spells remaining.")
            again = False
            return again
        else:
            print("You have no more spells left.")
            again = True
            return again

    def heal(self, name, hp, again):
        hp += 30
        if hp > MAX_HP:
            print("You are at max HP: " + str(MAX_HP))
            again = True
            return again
        else:
            print(name + " HP: " + str(hp))
            again = False
            return again

    def meditate(self, name, spell, again):
        if spell == 3:
            again = True
            print("You already have " + str(spell) + " spells.")
            return again
        spell = 3
        print(name + " has refilled their spells.")
        print("Spells: " + str(spell))
        again = False
        return again

def rules():
    print("Welcome to Wizard Fight!")
    print("Both players start with 500 HP.")
    print("Here are the available actions:")
    print("1) Attack: deal 50 HP damage.")
    print("2) Heal: restore 30 HP.")
    print("3) Meditate: refill your spells.")
    print("")

def ending(name,hp):
    print(name.upper(), "HAS WON WITH", hp, "HP LEFT!!!!")

def main():
    rules()
    wizard1 = Wizard(hp=300, name="Wizard 1", spell=5, again=False)
    wizard2 = Wizard(hp=300, name="Wizard 2", spell=5, again=False)
    turn = wizard1

    while True:
        # Player 1
        if turn == wizard1:
            wizard1.action = wizard1.ask_action(wizard1.name)

            if wizard1.action == "1":
                wizard1.again = wizard1.attack(name=wizard2.name, hp=wizard2.hp, spell=wizard1.spell, player=wizard1.name, again=wizard1.again)
                #print(wizard1.again)
                if wizard1.again:
                    pass
                wizard2.hp -= 50
                wizard1.spell -= 1

            elif wizard1.action == "2":
                wizard1.again = wizard1.heal(name=wizard1.name, hp=wizard1.hp, again=wizard1.again)
                # print(wizard1.again)
                if wizard1.again:
                    pass
                else:
                    wizard1.hp += 30
                # wizard1.again = False

            elif wizard1.action == "3":
                wizard1.again = wizard1.meditate(name=wizard1.name, spell=wizard1.spell, again=wizard2.again)
                wizard1.spell = 3
                # print(wizard1.spell)
                if wizard1.again:
                    pass

            print("----------------------")

            if wizard1.again == False:
                turn = wizard2

            wizard1.again = False

            if wizard2.hp <= 0:
                ending(name=wizard1.name, hp=wizard1.hp)
                break


        # Player 2
        if turn == wizard2:
            wizard2.action = wizard2.ask_action(wizard2.name)

            if wizard2.action == "1":
                wizard2.again = wizard2.attack(name=wizard1.name, hp=wizard1.hp, spell=wizard2.spell, player=wizard2.name, again=wizard2.again)
                if wizard2.again:
                    pass
                wizard1.hp -= 50
                wizard2.spell -= 1

            elif wizard2.action == "2":
                wizard2.again = wizard2.heal(name=wizard2.name, hp=wizard2.hp, again=wizard2.again)
                # print(wizard2.again)
                if wizard2.again:
                    pass
                else:
                    wizard2.hp += 30
                # wizard2.again = False

            elif wizard2.action == "3":
                wizard2.again = wizard2.meditate(name=wizard2.name, spell=wizard2.spell, again=wizard2.again)
                wizard2.spell = 3
                #print(wizard2.spell)
                if wizard2.again:
                    pass

            print("----------------------")

            if wizard2.again == False:
                turn = wizard1

            wizard2.again = False
            if wizard1.hp <= 0:
                ending(name=wizard2.name, hp=wizard2.hp)
                break


if __name__ == "__main__":
    main()
