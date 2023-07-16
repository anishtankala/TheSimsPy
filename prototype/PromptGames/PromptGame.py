def textToDict(textFile):
    import re

    dictionary = {}
    key = ""

    with open(textFile, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()  # remove trailing newline character

            # Check if the line ends with a letter indicating a new key
            if re.match(r"[0-9]+[a-z]$", line):
                key = line
                dictionary[key] = []
            else:
                # Add the line to the current key's value list
                dictionary[key].append(line.strip())

    return dictionary


def randomRoll(dictionary):
    import random

    def roll_dice():
        return random.randint(1, 10) - random.randint(1, 6)

    def assign_part(counts, roll):
        current_count = counts.get(roll, 0) + 1
        counts[roll] = current_count
        return f"{roll}{chr(ord('a')+current_count-1)}"

    counts = {}
    out = {}
    roll = 0
    while roll <= 80:
        roll = roll_dice() + roll + 5
        part = assign_part(counts, roll)

        if part in dictionary:
            out[part] = dictionary[part]

    return out


def create(textFile, game):
    import jsoneng

    jdb = jsoneng.JsonDB()
    jdb.create(textToDict(textFile), game)


def play(game, output):
    import jsoneng
    from termcolor import colored

    jdb = jsoneng.JsonDB()
    jdb.create({}, output)

    dictionary = randomRoll(jdb.retrieve(game))

    q1 = "broad summary of your previous life"
    c1 = "a character you are familiar with"
    c2 = "another character you are familiar with"
    s1 = "a skill you have"
    s2 = "another skill you have"
    r1 = "a resource you have"
    r2 = "another resource you have"
    e1 = "an experience you have relating to two of the things you described"

    preGame = [q1, c1, c2, s1, s2, r1, r2, e1]

    for i in range(len(preGame)):
        print(colored(preGame[i], "red"))
        text = input("> ")
        jdb.patch({i: {"prompt": preGame[i], "answer": text}}, output)

    for i, (k, v) in enumerate(dictionary.items()):
        print(colored(f"prompt {k}", "light_blue"))
        print(colored(v[0], "red"))
        text = input("> ")
        jdb.patch({k: {"prompt": v[0], "answer": text}}, output)


# create("ThousandYearOldVampire.txt", "TYOV")
play("TYOV", "Play")
