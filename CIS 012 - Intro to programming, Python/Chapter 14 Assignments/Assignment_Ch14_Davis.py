import random


class Tamagotchi:
    gender = ["Male", "Female", "Binary", "Fluid", "Quasar", "Not Defined"]
    character_type = ["Mammal", "Reptile", "Bird", "Fish", "Plant", "Interdimensional Being", "Amoeba", "Virus"]
    def __init__(self, name):
        self.name = name

    def description(self):
        return "Your Tamagotchi, {}, has gender {} and type {}.  {} has no special attributes".format(self.name, Tamagotchi.gender[random.randint(0,len(Tamagotchi.gender)-1)], Tamagotchi.character_type[random.randint(0,len(Tamagotchi.character_type)-1)], self.name)

    def display(self):
        return self.name


class Hungry(Tamagotchi):
    def attribute(self):
        return "Your Tamagotchi, {}, has gender {} and type {}.  {} seems to have a bigger stomach!".format(self.name, Tamagotchi.gender[random.randint(0,len(Tamagotchi.gender)-1)], Tamagotchi.character_type[random.randint(0,len(Tamagotchi.character_type)-1)], self.name)

class Ill(Tamagotchi):
    def attribute(self):
        return "Your Tamagotchi, {}, has gender {} and type {}.  {} seems to get sick easier!".format(self.name, Tamagotchi.gender[random.randint(0,len(Tamagotchi.gender)-1)], Tamagotchi.character_type[random.randint(0,len(Tamagotchi.character_type)-1)], self.name)



def turns():
    while True:
        print("Would you like to [1]Feed, [2]Play, or [3]do nothing?")
        user = input(">> ")
        try:
            feedback = int(user)
        except:
            print()
            print("Please enter 1, 2, or 3\n")

        if 0 < feedback < 4:
            break
        else:
            print()
            print("Please enter 1, 2, or 3\n")


    return feedback


def aliveTamagotchi(pet):
    alive = True
    happy = 10
    hunger = 10
    sickness = 0

    while alive == True:
        print()
        print("{}'s meters are:\nHappiness ({}/10)\nHunger ({}/10)\nSickness ({}/10)\n".format(pet.display(), happy, hunger, sickness))

        action = turns()

        if action == 1:
            hunger += 2
            happy -= 1
            if hunger > 10:
                sickness = sickness + (hunger - 10)
                hunger = 10
                if sickness >= 10:
                    alive = False
            elif hunger == 0 or happy == 0:
                alive = False

        elif action == 2:
            hunger -= 1
            happy += 3
            if happy > 10:
                happy = 10
            elif hunger == 0 or happy == 0:
                alive = False

        elif action == 3:
            hunger -= 1
            happy -= 1
            if hunger == 0 or happy == 0:
                alive = False

    print()
    print("{}'s meters are:\nHappiness ({}/10)\nHunger ({}/10)\nSickness ({}/10)\n".format(pet.display(), happy, hunger, sickness))


def aliveHungry(pet):
    alive = True
    happy = 10
    hunger = 10
    sickness = 0

    while alive == True:
        print()
        print("{}'s meters are:\nHappiness ({}/10)\nHunger ({}/10)\nSickness ({}/10)\n".format(pet.display(), happy, hunger, sickness))

        action = turns()

        if action == 1:
            hunger += 2
            happy -= 1
            if hunger > 10:
                sickness = sickness + (hunger - 10)
                hunger = 10
                if sickness >= 10:
                    alive = False
            elif hunger == 0 or happy == 0:
                alive = False

        elif action == 2:
            hunger -= 2
            happy += 3
            if happy > 10:
                happy = 10
            elif hunger == 0 or happy == 0:
                alive = False

        elif action == 3:
            hunger -= 2
            happy -= 1
            if hunger == 0 or happy == 0:
                alive = False

    print()
    print("{}'s meters are:\nHappiness ({}/10)\nHunger ({}/10)\nSickness ({}/10)\n".format(pet.display(), happy, hunger, sickness))


def aliveIll(pet):
    alive = True
    happy = 10
    hunger = 10
    sickness = 0

    while alive == True:
        print()
        print("{}'s meters are:\nHappiness ({}/10)\nHunger ({}/10)\nSickness ({}/10)\n".format(pet.display(), happy, hunger, sickness))

        action = turns()

        if action == 1:
            hunger += 2
            happy -= 1
            if hunger > 10:
                sickness = sickness + (hunger - 10) + 1
                hunger = 10
                if sickness >= 10:
                    alive = False
            elif hunger == 0 or happy == 0:
                alive = False

        elif action == 2:
            hunger -= 1
            happy += 3
            if happy > 10:
                happy = 10
            elif hunger == 0 or happy == 0:
                alive = False

        elif action == 3:
            hunger -= 1
            happy -= 1
            if hunger == 0 or happy == 0:
                alive = False

    print()
    print("{}'s meters are:\nHappiness ({}/10)\nHunger ({}/10)\nSickness ({}/10)\n".format(pet.display(), happy, hunger, sickness))


def main():
    option = random.randint(1,3)
    print("Hello! Welcome to the world of Tamagotchi!\n\nPlease enter a name for your new pet:")

    if option == 1:
        tama = Tamagotchi(input("").capitalize())
        print()
        print(tama.description())
        aliveTamagotchi(tama)
        #print("Oh no! Your Tamagotchi has died!\nCome back after some caretaker lessons.")
    elif option == 2:
        tama = Hungry(input("").capitalize())
        print()
        print(tama.attribute())
        aliveHungry(tama)
        #print("Oh no! Your Tamagotchi has died!\nCome back after some caretaker lessons.")
    elif option == 3:
        tama = Ill(input("").capitalize())
        print()
        print(tama.attribute())
        aliveIll(tama)
        #print("Oh no! Your Tamagotchi has died!\nCome back after some caretaker lessons.")

    print("Oh no! Your Tamagotchi has died!\nCome back after some caretaker lessons.")


main()
