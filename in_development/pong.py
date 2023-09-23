import tkinter as tk
from tkinter import messagebox

MIN_SPELLS = 0
MAX_HP = 500

class Wizard:
    def __init__(self, hp, name, spell, again):
        self.hp = hp
        self.name = name
        self.spell = spell
        self.again = again

    def attack(self, name, hp, spell, player, again):
        if spell > MIN_SPELLS:
            hp = int(hp)
            hp -= 50
            spell -= 1
            messagebox.showinfo("Attack", f"{name} HP: {hp}\n{player} has {spell} spells remaining.")
            again = False
            return again
        else:
            messagebox.showinfo("Attack", "You have no more spells left.")
            again = True
            return again

    def heal(self, name, hp, again):
        hp += 30
        if hp > MAX_HP:
            messagebox.showinfo("Heal", f"You are at max HP: {MAX_HP}")
            again = True
            return again
        else:
            messagebox.showinfo("Heal", f"{name} HP: {hp}")
            again = False
            return again

    def meditate(self, name, spell, again):
        if spell == 3:
            again = True
            messagebox.showinfo("Meditate", f"You already have {spell} spells.")
            return again
        spell = 3
        messagebox.showinfo("Meditate", f"{name} has refilled their spells.\nSpells: {spell}")
        again = False
        return again

def rules():
    messagebox.showinfo("Wizard Fight", "Welcome to Wizard Fight!\n\nBoth players start with 500 HP.\n\nHere are the available actions:\n1) Attack: deal 50 HP damage.\n2) Heal: restore 30 HP.\n3) Meditate: refill your spells.")

def ending(name, hp):
    messagebox.showinfo("Game Over", f"{name.upper()} has won with {hp} HP left!")

def show_action_dialog(player):
    global action_var

    action_label.config(text=f"What action do you want to use, {player}?")
    action_var.set("1")

    submit_button.config(command=process_action)

def process_action():
    global wizard1, wizard2, turn

    action = action_var.get()

    if turn == wizard1:
        if action == "1":
            wizard1.again = wizard1.attack(name=wizard2.name, hp=wizard2.hp, spell=wizard1.spell, player=wizard1.name, again=wizard1.again)
            if wizard1.again:
                pass
            wizard2.hp -= 50
            wizard1.spell -= 1

        elif action == "2":
            wizard1.again = wizard1.heal(name=wizard1.name, hp=wizard1.hp, again=wizard1.again)
            if wizard1.again:
                pass
            else:
                wizard1.hp += 30

        elif action == "3":
            wizard1.again = wizard1.meditate(name=wizard1.name, spell=wizard1.spell, again=wizard2.again)
            wizard1.spell = 3

        if wizard2.hp <= 0:
            ending(name=wizard1.name, hp=wizard1.hp)

    elif turn == wizard2:
        if action == "1":
            wizard2.again = wizard2.attack(name=wizard1.name, hp=wizard1.hp, spell=wizard2.spell, player=wizard2.name, again=wizard2.again)
            if wizard2.again:
                pass
            wizard1.hp -= 50
            wizard2.spell -= 1

        elif action == "2":
            wizard2.again = wizard2.heal(name=wizard2.name, hp=wizard2.hp, again=wizard2.again)
            if wizard2.again:
                pass
            else:
                wizard2.hp += 30

        elif action == "3":
            wizard2.again = wizard2.meditate(name=wizard2.name, spell=wizard2.spell, again=wizard2.again)
            wizard2.spell = 3

        if wizard1.hp <= 0:
            ending(name=wizard2.name, hp=wizard2.hp)

    switch_turn()

def switch_turn():
    global turn

    if turn == wizard1:
        turn = wizard2
    else:
        turn = wizard1
        show_action_dialog(turn.name)

def main():
    global wizard1, wizard2, turn, action_var, action_label, submit_button

    rules()
    wizard1 = Wizard(hp=300, name="Wizard 1", spell=5, again=False)
    wizard2 = Wizard(hp=300, name="Wizard 2", spell=5, again=False)
    turn = wizard1

    root = tk.Tk()
    root.title("Wizard Fight")

    action_var = tk.StringVar()

    action_label = tk.Label(root, text="")
    action_label.pack()

    radio_frame = tk.Frame(root)
    radio_frame.pack()

    attack_radio = tk.Radiobutton(radio_frame, text="Attack", variable=action_var, value="1")
    attack_radio.pack(side="left")

    heal_radio = tk.Radiobutton(radio_frame, text="Heal", variable=action_var, value="2")
    heal_radio.pack(side="left")

    meditate_radio = tk.Radiobutton(radio_frame, text="Meditate", variable=action_var, value="3")
    meditate_radio.pack(side="left")

    submit_button = tk.Button(root, text="Submit", command=process_action)
    submit_button.pack()

    show_action_dialog(turn.name)

    root.mainloop()

if __name__ == "__main__":
    main()
