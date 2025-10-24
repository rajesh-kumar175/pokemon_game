import random
import time


class Pokemon:
    def __init__(self, name, level, type, max_health, health, attacks):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.health = health
        self.attacks = attacks

    def attack(self, opponent, attack_name):
        if attack_name in self.attacks:
            damage = self.attacks[attack_name]
            opponent.health -= damage
            if opponent.health < 0:
                opponent.health = 0
            print(f"{self.name} used {attack_name}! It dealt {damage} damage.")
            print(f"{opponent.name} has {opponent.health}/{opponent.max_health} HP left.")
        else:
            print(f"{self.name} doesn't know {attack_name}.")

    def is_fainted(self):
        return self.health <= 0

    def level_up(self):
        self.level += 1
        self.max_health += random.randint(5, 10)
        self.health = self.max_health
        print(f"{self.name} leveled up! Now at level {self.level} with {self.max_health} HP.")

    def heal(self):
        self.health = self.max_health
        print(f"{self.name} healed to full health: {self.max_health} HP.")


def battle(pokemon1, pokemon2):
    print(f"\nTrainer battle: {pokemon1.name} vs {pokemon2.name}!\n")
    while not pokemon1.is_fainted() and not pokemon2.is_fainted():
        # Pokémon 1 attacks
        attack1 = random.choice(list(pokemon1.attacks.keys()))
        pokemon1.attack(pokemon2, attack1)
        time.sleep(1)

        if pokemon2.is_fainted():
            print(f"\n{pokemon2.name} fainted! {pokemon1.name} wins!")
            pokemon1.level_up()
            break

        # Pokémon 2 attacks
        attack2 = random.choice(list(pokemon2.attacks.keys()))
        pokemon2.attack(pokemon1, attack2)
        time.sleep(1)

        if pokemon1.is_fainted():
            print(f"\n{pokemon1.name} fainted! {pokemon2.name} wins!")
            pokemon2.level_up()
            break


# Sample Pokémon
charmander = Pokemon(name="Charmander", level=5, type="Fire", max_health=30, health=30,
                     attacks={"Scratch": 6, "Ember": 8})
bulbasaur = Pokemon(name="Bulbasaur", level=5, type="Grass", max_health=32, health=32,
                    attacks={"Tackle": 5, "Vine Whip": 7})

# Game loop
while True:
    print("\n1. Battle\n2. Heal Pokémon\n3. Quit")
    choice = input("Choose an action: ")
    if choice == '1':
        battle(charmander, bulbasaur)
    elif choice == '2':
        charmander.heal()
        bulbasaur.heal()
    elif choice == '3':
        print("Exiting game...")
        break
    else:
        print("Invalid choice. Try again.")