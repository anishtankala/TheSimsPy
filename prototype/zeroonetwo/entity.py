import random
import heapq
import sys
from dataclasses import *
import jsoneng

guardEncounter = """
you stumbled onto some guards in the place, roll to determine

roll d4
>4: you are safe
3: the guards saw you but not your face
check speed >4 to escape
2: the guards stops you for a routine inspection
check sanity >4 to escape
1: the guards saw you and your face
check speed >4 to escape
0: the guards stops you and initiate combat
create 1 to 4 guards as enemy
"""


events = [guardEncounter]

wraithInTheMirror = """
the player next to you saw a wraith in the mirror
it is their future self, and in order to help them
they must discard one item to the mirror
"""

omens = [wraithInTheMirror]

revolver = """
this military patterend revolver
is made from the best weapon smith in englandia

increase grit by 2
allows you to use speed to attack
for that attack only, increase speed by 2
"""

silverSword = """
a fine silver sword

increase grit by 2
"""

bloodySpear = """
a bloody spear, embued with power

increase grit by 2
"""

weapons = [revolver, silverSword, bloodySpear]

firstAidKit = """
a set of military mandages

heals 2 physical damage
"""

sokolovPhysicRemedy = """
alternative medicine created by the great
natural philosopher anton sokolov
can heal mental damage

heals 2 mental damage
"""

items = [firstAidKit, sokolovPhysicRemedy]

serf = """
a common serf working the farms

grit = 2
speed = 2
knowledge = 0
sanity = 2
"""

commoner = """
a commmoner belonging to an urban area

grit = 2
speed = 2
knowledge = 0
sanity = 2
"""

gangster = """
a roaming gangster

grit = 6
speed = 4
knowledge = 2
sanity = 2
"""

inquisitor = """
an inquisitor of the church, hunting monsters and heretics

grit = 6
speed = 6
knowledge = 6
sanity = 6
"""

humans = [serf, commoner, gangster, inquisitor]

allEntities = [events, omens, weapons, items, humans]


def entity(arrList):
    print(random.choice(arrList))


entity(random.choice(allEntities))
