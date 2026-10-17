class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, enemy):
        print(self.name, "attacks", enemy.name)
        enemy.health -= 20

    def show_info(self):
        print("Name:", self.name)
        print("Health:", self.health)


class Player(Character):

    def heal(self):
        self.health += 10
        print(self.name, "healed by 10")


class Enemy(Character):

    def attack(self, player):
        print(self.name, "attacks", player.name)
        player.health -= 15


player = Player("Harshu", 100)
enemy = Enemy("Monster", 80)

player.show_info()
enemy.show_info()

print()

player.attack(enemy)
enemy.attack(player)

print()

player.heal()

print()

player.show_info()
enemy.show_info()