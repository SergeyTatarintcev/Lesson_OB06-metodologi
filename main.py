import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"\nБитва начинается! {self.player.name} против {self.computer.name}!\n")
        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"--- Раунд {round_number} ---")
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)

            print(f"{self.player.name}: {self.player.health} HP")
            print(f"{self.computer.name}: {self.computer.health} HP\n")
            round_number += 1

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    name = input("Введите имя вашего героя: ")
    game = Game(name)
    game.start()
