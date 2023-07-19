from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

# ESCAPE FROM IRELANDIA


# ITEMS


@dataclass
class Action:
    name: str
    desc: str
    actionRollTable: dict


@dataclass
class Item:
    name: str
    desc: str
    actions: list[Action]


class Gun(Item):
    def __init__(self):
        self.name = "Gun"
        self.desc = "This revolver contains six bullets, but it tends to jam"

        class ShootFullClip(Action):
            def __init__(self):
                self.name = "Shoot (Full Clip)"
                self.desc = "you take aim with your finesess and shoot, you can use this once per turn"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["4", "incapicate target"],
                        ["3", "miss"],
                    ],
                }

        class ShootHalfClip(Action):
            def __init__(self):
                self.name = "Shoot (Half Clip)"
                self.desc = "you take aim with your finesess and shoot, you can use this once per turn"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["8", "incapicate target"],
                        ["7", "miss"],
                    ],
                }

        class Reload(Action):
            def __init__(self):
                self.name = "Reload"
                self.desc = "you reload your gun, remove bullets from your inventory"
                self.actionRollTable = {
                    "rollType": "knowledge",
                    "roll": [
                        ["2", "reload succeed"],
                        ["1", "reload failed, try again"],
                    ],
                }

        class Aim(Action):
            def __init__(self):
                self.name = "Aim"
                self.desc = "you aim your gun, allowing an easier time to fire"
                self.actionRollTable = {
                    "rollType": "sanity",
                    "roll": [
                        ["8", "increase speed +2 to your next shoot"],
                        ["4", "increase speed +1 to your next shoot"],
                    ],
                }

        self.actions = [ShootFullClip(), ShootHalfClip(), Reload(), Aim()]


gun = Gun()

# choice = input(f"> {[a.name for a in gun.actions]} ")
class GuardsKey(Item):
    def __init__(self):
        self.name = "Guard's Key"
        self.desc = "This key is used to unlock doors and access restricted areas."

        class Unlock(Action):
            def __init__(self):
                self.name = "Unlock"
                self.desc = "You use the key to unlock doors and access restricted areas."
                self.actionRollTable = {
                    "rollType": "knowledge",
                    "roll": [
                        ["6", "Successfully unlock the door"],
                        ["3", "Fail to unlock the door"],
                    ],
                }

        class SilentUnlock(Action):
            def __init__(self):
                self.name = "Silent Unlock"
                self.desc = "You use the key to unlock doors silently, avoiding detection."
                self.actionRollTable = {
                    "rollType": "stealth",
                    "roll": [
                        ["8", "Successfully unlock the door without making any noise"],
                        ["4", "Make a slight noise while unlocking the door"],
                    ],
                }

        class QuickUnlock(Action):
            def __init__(self):
                self.name = "Quick Unlock"
                self.desc = "You quickly use the key to unlock doors, saving time."
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["7", "Successfully unlock the door in record time"],
                        ["5", "Unlock the door, but it takes a bit longer than expected"],
                    ],
                }

        self.actions = [Unlock(), SilentUnlock(), QuickUnlock()]


class Shovel(Item):
    def __init__(self):
        self.name = "Shovel"
        self.desc = "A sturdy shovel used for digging and excavation."

        class Dig(Action):
            def __init__(self):
                self.name = "Dig"
                self.desc = "You use the shovel to dig holes or trenches."
                self.actionRollTable = {
                    "rollType": "strength",
                    "roll": [
                        ["8", "Successfully dig the hole or trench"],
                        ["4", "Struggle to dig, takes more effort"],
                    ],
                }

        class ClearPath(Action):
            def __init__(self):
                self.name = "Clear Path"
                self.desc = "You use the shovel to clear obstacles and create a path."
                self.actionRollTable = {
                    "rollType": "agility",
                    "roll": [
                        ["7", "Successfully clear the path"],
                        ["5", "Encounter some difficulties while clearing the path"],
                    ],
                }

        self.actions = [Dig(), ClearPath()]

class Bed(Item):
    def __init__(self):
        self.name = "Bed"
        self.desc = "A comfortable bed for resting."

        class Rest(Action):
            def __init__(self):
                self.name = "Rest"
                self.desc = "You can rest on the bed to regain energy."
                self.actionRollTable = {
                    "rollType": "endurance",
                    "roll": [
                        ["8", "Fully rested and rejuvenated"],
                        ["5", "Partially rested, still feeling tired"],
                    ],
                }

        self.actions = [Rest()]

class Food(Item):
    def __init__(self):
        self.name = "Food"
        self.desc = "Delicious food for nourishment."

        class Eat(Action):
            def __init__(self):
                self.name = "Eat"
                self.desc = "You can eat the food to satisfy your hunger."
                self.actionRollTable = {
                    "rollType": "skill",
                    "roll": [
                        ["6", "Enjoy a delicious meal"],
                        ["3", "The food is average in taste"],
                    ],
                }

        self.actions = [Eat()]

class Toilet(Item):
    def __init__(self):
        self.name = "Toilet"
        self.desc = "A sanitary toilet for personal needs."

        class UseToilet(Action):
            def __init__(self):
                self.name = "Use Toilet"
                self.desc = "You can use the toilet for your personal needs."
                self.actionRollTable = {
                    "rollType": "endurance",
                    "roll": [
                        ["8", "Successfully use the toilet without any issues"],
                        ["5", "Encounter some difficulties while using the toilet"],
                    ],
                }

        self.actions = [UseToilet()]

class Table(Item):
    def __init__(self):
        self.name = "Table"
        self.desc = "A sturdy table for various purposes."

        class UseTable(Action):
            def __init__(self):
                self.name = "Use Table"
                self.desc = "You can use the table for various activities."
                self.actionRollTable = {
                    "rollType": "skill",
                    "roll": [
                        ["6", "Successfully use the table"],
                        ["3", "Encounter some difficulties while using the table"],
                    ],
                }

        self.actions = [UseTable()]

# CHARACTERS


@dataclass
class Char:
    name: str
    desc: str
    listOfItems: list[Item]
    actions: list[Action]


class Jailor(Char):
    def __init__(self):
        self.name = "Jailor"
        self.desc = "a typical jailor, they might not want to be there, just there for a paycheck, but they still do their jobs"
        self.listOfItems = [Gun()]

        class Patrol(Action):
            def __init__(self):
                self.name = "Patrol"
                self.desc = "the jailor patrols the area, they check for you"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["4", "found you"],
                        ["3", "miss you"],
                    ],
                }

        class CallBackup(Action):
            def __init__(self):
                self.name = "Call Backup"
                self.desc = "calls for backup, get some extra weapons or help"
                self.actionRollTable = {
                    "rollType": "sanity",
                    "roll": [
                        ["6", "they receive extra weapons and help"],
                        ["4", "they only receive extra weapons"],
                        ["3", "nobody comes to help"],
                    ],
                }

        self.actions = [Patrol(), CallBackup()]

class KitchenStaff(Char):
    def __init__(self):
        self.name = "KitchenStaff"
        self.desc = "a member of the kitchen staff"
        self.listOfItems = []
        self.actions = []

        class PrepareMeal(Action):
            def __init__(self):
                self.name = "Prepare Meal"
                self.desc = "prepare a meal for the inmates"
                self.actionRollTable = {
                    "rollType": "skill",
                    "roll": [
                        ["6", "the meal turns out delicious"],
                        ["4", "the meal is average"],
                        ["2", "the meal is poorly prepared"],
                    ],
                }

        class StealSupplies(Action):
            def __init__(self):
                self.name = "Steal Supplies"
                self.desc = "sneakily take some supplies from the kitchen"
                self.actionRollTable = {
                    "rollType": "stealth",
                    "roll": [
                        ["6", "successfully steal the supplies without being noticed"],
                        ["3", "get caught but manage to take some supplies"],
                        ["1", "get caught and fail to take any supplies"],
                    ],
                }

        self.actions = [PrepareMeal(), StealSupplies()]

class Inmate(Char):
    def __init__(self):
        self.name = "Inmate"
        self.desc = "an inmate residing in the prison"
        self.listOfItems = []
        self.actions = []

        class PlotEscape(Action):
            def __init__(self):
                self.name = "Plot Escape"
                self.desc = "conspire with other inmates to escape"
                self.actionRollTable = {
                    "rollType": "intelligence",
                    "roll": [
                        ["6", "escape plan is foolproof"],
                        ["4", "escape plan has some risks"],
                        ["2", "escape plan is unlikely to work"],
                    ],
                }

        class StartFight(Action):
            def __init__(self):
                self.name = "Start a Fight"
                self.desc = "instigate a fight with another inmate"
                self.actionRollTable = {
                    "rollType": "strength",
                    "roll": [
                        ["6", "overwhelming victory"],
                        ["3", "partial success"],
                        ["1", "defeat"],
                    ],
                }

        self.actions = [PlotEscape(), StartFight()]

# GOOD EVENTS


@dataclass
class GoodEvent:
    name: str
    desc: str
    eventRollTable: dict
    listOfItems: list[Item]
    listOfChars: list[Char]


# BAD EVENTS


@dataclass
class BadEvent:
    name: str
    desc: str
    eventRollTable: dict
    listOfItems: list[Item]
    listOfChars: list[Char]


class Patrol(BadEvent):
    def __init__(self):
        self.name = "Patrol"
        self.desc = "a patrol of some guards came over, roll to see the guards you get"

        self.eventRollTable = {
            "rollType": "speed",
            "roll": [
                ["6", "no guard found you"],
                ["4", "one guard found you"],
                ["3", "lots of guards found you (d4)"],
            ],
        }

        self.listOfItems = []
        self.listOfChars = [Jailor()]

class Fight(BadEvent):
    def __init__(self):
        self.name = "Fight"
        self.desc = "a physical altercation between inmates"

        self.eventRollTable = {
            "rollType": "combat",
            "roll": [
                ["6", "inmates peacefully resolve the conflict"],
                ["4", "minor injuries sustained by both parties"],
                ["2", "serious injuries and intervention by guards"],
            ],
        }

        self.listOfItems = []
        self.listOfChars = [Inmate()]

class FoodFight(BadEvent):
    def __init__(self):
        self.name = "Food Fight"
        self.desc = "an altercation between inmates involving throwing food"

        self.eventRollTable = {
            "rollType": "chaos",
            "roll": [
                ["6", "inmates quickly stop the food fight"],
                ["4", "food fight escalates, causing a mess"],
                ["2", "chaotic food fight with widespread food throwing"],
            ],
        }

        self.listOfItems = []
        self.listOfChars = [Inmate()]

# LOCALES

prison = {
    "armory": [
        "weapon cache",
        "armory entrance",
    ],
    "yard": [
        "main yard",
        "yard gates",
    ],
}


@dataclass
class Locale:
    localeName: str
    desc: str
    listOfItems: list[Item]
    listOfChars: list[Char]
    listOfGoodEvents: list[GoodEvent]
    listOfBadEvents: list[BadEvent]


@dataclass
class Biome:
    biomeName: str
    desc: str
    locales: list[Locale]


@dataclass
class Overworld:
    overworldName: str
    desc: str
    biomes: list[Biome]


class Prison(Overworld):
    def __init__(self):
        self.overworldName = "Imperial Irelandia Prison"
        self.desc = "none shall leave here without penance"

        class Armories(Biome):
            def __init__(self):
                self.biomeName = "Armory Section"
                self.desc = "the armory section, guns and lots of guards patrolling"

                class WeaponCache(Locale):
                    def __init__(self):
                        self.localeName = "Weapon Cache"
                        self.desc = "lots of weapons here"

                        self.listOfItems = [Gun()]
                        self.listOfChars = [Jailor()]
                        self.listOfGoodEvents = []
                        self.listOfBadEvents = [Patrol()]

                    def localeAffect(self):
                        import random

                        lowerBound = jdb.r("heat lower bound")
                        lowerBound -= random.randint(1, 2)
                        jdb.p("heat lower bound", lowerBound)

                class ArmoryEntrance(Locale):
                    def __init__(self):
                        self.localeName = "Armory Entrance"
                        self.desc = "lots of guards patrolling the entrance"

                        self.listOfItems = []
                        self.listOfChars = [Jailor()]
                        self.listOfGoodEvents = []
                        self.listOfBadEvents = [Patrol()]

                    def localeAffect(self):
                        import random

                        lowerBound = jdb.r("heat lower bound")
                        lowerBound += random.randint(1, 2)
                        jdb.p("heat lower bound", lowerBound)

                self.locales = [WeaponCache(), ArmoryEntrance()]
        
        class CellBlock(Biome):
            def __init__(self):
                self.biomeName = "Cell Block"
                self.desc = "the cell block area, where inmates are housed"

                class Cell(Locale):
                    def __init__(self):
                        self.localeName = "Cell"
                        self.desc = "a prison cell where an inmate resides"

                        self.listOfItems = [Bed(), Toilet()]
                        self.listOfChars = [Inmate()]
                        self.listOfGoodEvents = []
                        self.listOfBadEvents = [Fight()]

                class Cafeteria(Locale):
                    def __init__(self):
                        self.localeName = "Cafeteria"
                        self.desc = "the cafeteria where inmates have their meals"

                        self.listOfItems = [Table(), Food()]
                        self.listOfChars = [Inmate(), KitchenStaff()]
                        self.listOfGoodEvents = []
                        self.listOfBadEvents = [FoodFight()]

                self.locales = [Cell(), Cafeteria()]

        self.biomes = [Armories(), CellBlock()]


def locale(overworld, size):
    import random
    from termcolor import colored

    steps = 0
    locale = []
    while True:
        biomeType = input(f"create next locale... locale type: ")

        if biomeType == "":
            print(f"{[biome.biomeName for biome in overworld.biomes]}")
            continue

        steps += 1

        for biome in overworld.biomes:
            if biomeType == biome.biomeName:
                selectedLocale = random.choice(biome.locales)
                locale.append(selectedLocale.localeName)
                selectedLocale.status()

        if len(locale) > size:
            locale.pop(0)

        print(f"steps: {colored(steps, 'red')}")
        print(f"heat lower bound: {colored(jdb.r('heat lower bound'), 'red')}")
        print(f"heat upper bound: {colored(jdb.r('heat upper bound'), 'red')}")
        print(f"{locale}")


def setup():
    def prisonHeat():
        import random

        heatLowerBound = random.randint(100, 120)
        heatUpperBound = random.randint(200, 300)

        jdb.p("heat lower bound", heatLowerBound)
        jdb.p("heat upper bound", heatUpperBound)

        return random.randint(heatLowerBound, heatUpperBound)

    prisonHeat()

    p = Prison()

    jdb.patch(asdict(p))

    locale(p, 4)


setup()
