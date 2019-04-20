# -*- coding: utf-8 -*-

from planets import Planet
from ships import *
import numbers


class Player:

    def __init__(self, name, age, galaxy, pilot, fighter, trader, engineer):
        self.name = name
        self.age = age
        self.wallet = 1000
        self.ship = Scorpion()
        self.location = galaxy.earth
        self.pilotPoints = pilot
        self.fighterPoints = fighter
        self.traderPoints = trader
        self.engineerPoints = engineer


    def viewWallet(self):
        print(self.wallet)

    def viewAge(self):
        print(self.age)

    def describeShip(self):
        print("You fly a {} valued at {} credits.".format(self.ship.shipClass, self.ship.value))

    def travel(self, distance):
        if distance > self.ship.range:
            print("That's out of range!")
        else:
            self.ship.range = self.ship.range - distance

    def buyResource(self):
        resource = input("What would you like to buy?\n")

        if resource in self.location.supply and self.location.supply[resource] > 0:
            amount = int(input("How much {} would you like to buy?\n".format(resource)))

            cost = self.location.prices[resource] * amount

            if amount <= self.location.supply[resource]:
                if resource == 'Fuel' and self.ship.range + amount <= self.ship.maxRange:

                    if cost <= self.wallet:
                        self.ship.range += amount
                        self.wallet -= cost
                        self.location.economy += cost
                        self.location.supply['Fuel'] -= amount
                    else:
                        print("You can't afford that much fuel.")

                elif resource == 'Fuel' and self.ship.range + amount > self.ship.maxRange:
                    print("That's more fuel than your ship can hold.")

                if resource != 'Fuel' and self.ship.getEncumberance() + amount <= self.ship.capacity:

                    if cost <= self.wallet:
                        self.ship.supply[resource] += amount
                        self.wallet -= cost
                        self.location.economy += cost
                        self.location.supply[resource] -= amount
                    else:
                        print("You can't afford that much {}".format(resource))
                else:
                    print("{} doesn't have that much {}".format(self.location.name, resource))
            else:
                print("{} doesn't have that much {}".format(self.location.name, resource))
        else:
            print("{} doesn't have any {} right now".format(self.location.name, resource))

    def inspectPlanetSupply(self):
        for key in self.location.supply:
            print("{}: {}".format(key, self.location.supply[key]))

    def inspectPlanetPrices(self):
        for key in self.location.prices:
            print("{}: {}".format(key, self.location.prices[key]))


class Galaxy():

    def __init__(self):
        self.earth = Planet("Earth")
        self.aarakis = Planet("Aarakis")
        self.alpha_centauri = Planet("Alpha Centauri II")
        self.coruscant = Planet("Coruscant")
        self.eden_prime = Planet("Eden Prime")
        self.titan = Planet("Titan")
        self.vulcan = Planet("Vulcan")

def printOptions():
    print("\nYou can:")
    print("1) Get Location")
    print("2) View Travel Distances")
    print("3) Travel")
    print("4) Inspect Ship")
    print("5) Rename Ship")
    print("6) View Wallet")
    print("7) Inspect Planet Supply")
    print("8) Inspect Planet Prices")
    print("9) Buy")
    print("10) Sell")
    print("11) Quit")
    print()

def main():

    galaxy = Galaxy()

    playerName = input("What is your name?\n")
    playerAge = input("How old are you?\n")
    print("You have a max of 16 skill points, please choose wisely\n")
    pilot = 5
    fighter = 3
    trader = 5
    engineer = 3
    correct = False
    total = 16
    while not correct:
        pilotVal = input("please enter how many points you would like for pilot, no more than 16!\n")

        try:
            pilot = int(pilotVal)
            if 16 >= pilot >= 0:
                correct = False
                total = total - pilot
                break
            else:
                print("Sorry, input not valid, please try again\n")
        except ValueError:
            print("Sorry, please enter an integer again\n")

    correct = False
    while not correct:
        fighterVal = input("please enter how many points you would like for fighter, no more than {}!\n".format(total))

        try:
            fighter = int(fighterVal)
            if 0 <= fighter <= total:
                correct = False
                total = total - fighter
                break
            else:
                print("Sorry, input not valid, please try again\n")
        except ValueError:
            print("Sorry, please enter an integer again\n")

    correct = False
    while not correct:
        traderVal = input("please enter how many points you would like for trader, no more than {}!\n".format(total))

        try:
            trader = int(traderVal)
            if 0 <= trader <= total:
                correct = False
                total = total - trader
                break
            else:
                print("Sorry, input not valid, please try again\n")
        except ValueError:
            print("Sorry, please enter an integer again\n")

    correct = False
    while not correct:
        engineerVal = input("please enter how many points you would like for engineer, no more than {}!\n".format(total))

        try:
            engineer = int(engineerVal)
            if 0 <= engineer <= total:
                correct = False
                total = total - engineer
                break
            else:
                print("Sorry, input not valid, please try again\n")
        except ValueError:
            print("Sorry, please enter an integer again\n")


    player = Player(playerName, playerAge, galaxy, pilot, fighter, trader, engineer)


    print()
    print("Hello {}. You start with {} credits and no cargo. You have been assigned a {}-class ship.".format(player.name, player.wallet, player.ship.shipClass))
    print("Your pilot has {} points".format(player.pilotPoints))
    print("Your fighter has {} points".format(player.fighterPoints))
    print("Your trader has {} points".format(player.traderPoints))
    print("Your engineer has {} points".format(player.engineerPoints))
    print()
    print("You are on {}.".format(player.location.name))

    play = True

    while play:

        topChoice = input("What would you like to do? Enter 12 for help. > \n")

        try:
            if int(topChoice) == 12:
                printOptions()

            if int(topChoice) == 11:
                play = False

            elif int(topChoice) == 1:
                print(player.location.name)
                print()

            elif int(topChoice) == 2:

                print()

            elif int(topChoice) == 3:

                print()

            elif int(topChoice) == 4:
                player.ship.viewCargo()
                print()

            elif int(topChoice) == 5:
                player.ship.renameShip()
                print("{} is a fitting name.".format(player.ship.name))
                print()

            elif int(topChoice) == 6:
                player.viewWallet()
                print()

            elif int(topChoice) == 7:
                player.inspectPlanetSupply()
                print()

            elif int(topChoice) == 8:
                player.inspectPlanetPrices()
                print()

            elif int(topChoice) == 9:

                print()

            elif int(topChoice) == 10:

                print()

            else:
                print("Please enter an integer corresponding to an action.")

        except ValueError:
            print("Please enter an integer corresponding to an action.\n")




if __name__ == "__main__":
    main()
