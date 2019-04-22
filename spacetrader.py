# -*- coding: utf-8 -*-

from planets import Planet
from ships import *
import numbers
import random


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
            print("That's out of range! Your range is only {}".format(self.ship.range))
            return False
        else:
            self.ship.range = self.ship.range - distance
            return True

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
    def viewLocation(self):
        return self.location


class Galaxy():

    def __init__(self):
        self.earth = Planet("Earth")
        self.aarakis = Planet("Aarakis")
        self.alpha_centauri = Planet("Alpha Centauri II")
        self.coruscant = Planet("Coruscant")
        self.eden_prime = Planet("Eden Prime")
        self.titan = Planet("Titan")
        self.vulcan = Planet("Vulcan")
        self.mars = Planet("Mars")
        self.venus = Planet("Venus")
        self.yeet = Planet("Yeet")

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
    print(r"  _________                           ___________                  .___            ")
    print(r" /   _____/__________    ____  ____   \__    ___/___________     __| _/___________")
    print(r" \_____  \\____ \__  \ _/ ___\/ __ \    |    |  \_  __ \__  \   / __ |/ __ \_  __ \ ")
    print(r" /        \  |_> > __ \\  \__\  ___/    |    |   |  | \// __ \_/ /_/ \  ___/|  | \/")
    print(r"/_______  /   __(____  /\___  >___  >   |____|   |__|  (____  /\____ |\___  >__|   ")
    print(r"        \/|__|       \/     \/    \/                        \/      \/    \/      ")

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
    print("You are on {}.\n".format(player.location.name))


    galaxyNames = []
    galaxyNames.append(galaxy.aarakis.name)
    galaxyNames.append(galaxy.alpha_centauri.name)
    galaxyNames.append(galaxy.coruscant.name)
    galaxyNames.append(galaxy.earth.name)
    galaxyNames.append(galaxy.eden_prime.name)
    galaxyNames.append(galaxy.mars.name)
    galaxyNames.append(galaxy.titan.name)
    galaxyNames.append(galaxy.venus.name)
    galaxyNames.append(galaxy.vulcan.name)
    galaxyNames.append(galaxy.yeet.name)

    galaxyList = []
    galaxyList.append(galaxy.aarakis)
    galaxyList.append(galaxy.alpha_centauri)
    galaxyList.append(galaxy.coruscant)
    galaxyList.append(galaxy.earth)
    galaxyList.append(galaxy.eden_prime)
    galaxyList.append(galaxy.mars)
    galaxyList.append(galaxy.titan)
    galaxyList.append(galaxy.venus)
    galaxyList.append(galaxy.vulcan)
    galaxyList.append(galaxy.yeet)

    print("The planets are: ")
    print(*galaxyNames, sep = ", ")
    print()
    print()
    print()

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
                currlocation = player.viewLocation().coordinates[1]
                for x in galaxyList:
                    if (x.name == player.viewLocation().name):
                        continue
                    else:
                        planetLocation = x.coordinates[1]
                        distanceVal = abs(currlocation - planetLocation)
                        print("Distance to {} is {}".format(x.name, distanceVal))

            elif int(topChoice) == 3:

                realGalaxyList = []
                for x in galaxyList:
                    if (x.name == player.viewLocation().name):
                        continue
                    else:
                        realGalaxyList.append(x)
                counter = 1
                for x in realGalaxyList:
                    print("{}. {}".format(counter, x.name))
                    counter+=1
                choice = player.viewLocation()
                correct = False
                while not correct:
                    num = input("Please select the number of the planet you'd like to travel to: \n")
                    try:
                        realnum = int(num)
                        if 1 <= realnum <= len(realGalaxyList):
                            choice = realGalaxyList[realnum - 1]
                            #print("NEXT LOCATION IS {}".format(choice.name))
                        else:
                            print("Sorry, input not valid, please try again\n")
                    except ValueError:
                        print("Sorry, please enter an integer again\n")
                    currlocation = player.location.coordinates[1]
                    planetLocation = x.coordinates[1]
                    distanceVal = abs(currlocation - planetLocation)
                    correct = player.travel(distanceVal)
                x = random.randint(0, 10)
                if x < 5:
                    y = random.randint(1, 100)
                    print("You found money in your toilet, you gain {} credits!".format(y))
                    player.wallet += y


                print("Your remaining range is {}".format(player.ship.range))
                player.location = choice

                print("Your location is now {}".format(player.viewLocation().name))


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
                player.buyResource()
                print()

            elif int(topChoice) == 10:
                sellItem = input("What would you like to sell?")
                if (sellItem not in player.ship.supply):
                    sellItem = input("That item is not a valid choice, please try again.")
                amountOfItem = int(input("How much of {} would you like to sell?".format(sellItem)))
                if (amountOfItem > player.ship.supply[sellItem]):
                    amountOfItem = int(input("Sorry, you only have a max {} {} on your ship, please try again with a lower amount".format(player.ship.supply[sellItem], sellItem)))
                if (amountOfItem > player.ship.supply[sellItem]):
                    amountOfItem = int(input("Sorry, you only have a max {} {} on your ship, please try again with a lower amount".format(player.ship.supply[sellItem], sellItem)))
                if (amountOfItem > player.ship.supply[sellItem]):
                    amountOfItem = int(input("Sorry, you only have a max {} {} on your ship, please try again with a lower amount".format(player.ship.supply[sellItem], sellItem)))
                priceOnPlanet = player.location.prices[sellItem]
                revenue = priceOnPlanet * amountOfItem
                player.location.supply[sellItem] += amountOfItem
                player.ship.supply[sellItem] -= amountOfItem
                player.ship.capacity += amountOfItem
                player.wallet += revenue
                print("You have successfully sold {} {} at a revenue of {} to planet {}".format(amountOfItem, sellItem, revenue, player.location.name))
                print()

            else:
                print("Please enter an integer corresponding to an action.")

        except ValueError:
            print("Please enter an integer corresponding to an action.\n")




if __name__ == "__main__":
    main()
