import random
import time

names_of_moves = ["Thunderbolt", "Strike", "Rollout"]
list_of_moves = {"Thunderbolt": 30, "Strike": 50, "Rollout": 10}
health = 100

def getMove():
    move = input("Which move do you want to make: ")
    return move


def doBattle(monsterName, initialHealth, lowerDamage, higherDamage):
    monsterHealth = initialHealth
    global health
    while monsterHealth > 0:
        # Monster attacks you
        monsterDamage = random.randint(lowerDamage, higherDamage)
        health = health - monsterDamage
        if health <= 0:
            print("You're dead lmao.")
            break
        else:
            print(f"The {monsterName} hit you for {monsterDamage} damage and now you have {health} health left")
        time.sleep(1)
        for name in names_of_moves:
            print(name)

        move = getMove()
        damage = list_of_moves[move]

        monsterHealth = monsterHealth - damage
        if monsterHealth <= 0:
            print(f"The {monsterName} was killed. LOL")
        else:
            print("The monster has " + str(monsterHealth) + " health left.")
        time.sleep(1)

doBattle("Celia", 100, 10, 20)
doBattle("Gremlin", 50, 5, 10)
