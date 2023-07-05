import random
import json
from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

# class Char:
#     def __init__(self, charData):
#         self.charData = charData

#     def __repr__(self):
#         return f"Char:{json.dumps(self.charData, indent=2)})"


@dataclass
class Skills:
    martial: int
    larceny: int
    etiquette: int
    education: int
    journey: int
    craft: int
    silver_tongue: int


@dataclass
class Stats:
    fame: int
    body: int
    reputation: int
    wealth: int
    friends: int
    mental: int
    grit: int


@dataclass
class Char:
    name: str
    background: str
    skills: Skills
    stats: Stats


def createChar(name, background):
    skills = Skills(0, 0, 0, 0, 0, 0, 0)
    stats = Stats(0, 0, 0, 0, 0, 0, 0)
    return Char(name, background, skills, stats)


tom = createChar("tom", "COMMON")

jdb.i(asdict(tom))


@dataclass
class Role:
    type: str
    archetype: list
    history: list
    events: dict
    benefits: list
    quitting: list
    char: Char

    def genArchetype(self):
        return random.choice(self.archetype)

    def genHistory(self):
        out = {}
        years = random.randint(1, 7)
        for year in range(years):
            out["year " + str(year) + " desc"] = self.history[year - 1]["desc"]
            if self.history[year - 1].keys():
                print("ok")
            out["year " + str(year) + " event"] = self.genEvent()
        return out

    def genEvent(self):
        out = {}
        ranEvent = random.choice(self.events)
        out["title"] = ranEvent["title"]
        out["desc"] = ranEvent["desc"]
        out["choice"] = random.choice(ranEvent["choices"])["desc"]
        return out

    def genAll(self):
        out = {}
        out["archetype"] = self.genArchetype()
        out["history"] = self.genHistory()
        return out


class Soldier(Role):
    def __init__(self):
        self.type = "soldier"
        self.archetype = ["infantry", "skirmisher", "cavalry", "frontier guard"]
        self.history = [
            {
                "desc": "you're still learning the trade",
                "stats": [
                    ["martial", 1],
                ],
            },
            {"desc": "you've seen a lot on the frontline"},
            {
                "desc": "you are a seasoned soldier who has fought on many battlefields across the country",
            },
            {
                "desc": "by now, you're a jaded veteran",
                "stats": [
                    ["martial", 1],
                    ["body", -1],
                ],
            },
            {
                "desc": "by now, you're a jaded veteran",
                "stats": [
                    ["martial", 1],
                    ["body", -1],
                ],
            },
            {
                "desc": "your name is quite known among soldiers",
                "stats": [
                    ["body", -1],
                ],
            },
            {
                "desc": "sieges, sabotage, hopeless battles, desperate charges, you've done it all",
                "stats": [
                    ["martial", 1],
                ],
            },
            {
                "desc": "war legend",
                "stats": [
                    ["martial", 1],
                    ["body", -1],
                ],
            },
        ]
        self.events = [
            {
                "title": "sacking",
                "desc": "when the city fell, after a long siege, came the time of savagery. What did you do on this cruel night?",
                "choices": [
                    {
                        "desc": "you took part in the rapes and looting",
                        "stats": [["grit", 1], ["reputation", 1]],
                    },
                    {
                        "desc": "you refused to give in to your vile instincts",
                        "stats": [["reputation", 1], ["mental", -1]],
                    },
                ],
            },
            {
                "title": "smuggling",
                "desc": "you discovered that some of your officers were engaged in illegal smuggling, so you...",
                "choices": [
                    {
                        "desc": "...denounced them to your superiors",
                        "stats": [["reputation", 1], ["grit", -1]],
                    },
                    {
                        "desc": "...kept your tongue, on a condition",
                        "stats": [["wealth", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["brothers-in-arms", "survival", "weapon proficiency"]
        self.quitting = ["promotion", "moving on", "infamy", "captured"]


s = Soldier()
jdb.i(s.genAll())

sampleOut = {
    0: {
        "type": "soldier",
        "archetype": "infantry",
        "year1": "you are still learning the trade, martial + 1",
    }
}

# class RoleTemplate(Role):
#     roleData = {
#         'type': '',
#         'archetype':
#         ['','','',''],
#         'events':
#         {'': ['',''],
#         '': ['','']},
#         'rewards': ['','','']
#     }
