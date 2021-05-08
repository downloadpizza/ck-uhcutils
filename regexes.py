import re

killed = r'(?P<killed>[a-zA-Z0-9_]{3,})'
killer = r'(?P<killer>[a-zA-Z0-9_]{3,})'
item = r'(?P<item>.+)'
prefix = r'\[(?P<time>[0-9]{2}:[0-9]{2}:[0-9]{2})] \[.+\/INFO]: \[CHAT] '

start_regex = re.compile(prefix + "The Overworld world border started shrinking\.")
end_regex = re.compile(prefix + "(?P<winner>.+) has won the game!")
        

def make_regex(s):
    s = re.escape(s)
    s = prefix + s.replace("KILLED", killed).replace("KILLER", killer).replace("ITEM", item)
    return re.compile(s)

with open("regex/death.txt", "r") as f:
    death_regex = [make_regex(it.strip()) for it in f.readlines()]

with open("regex/kill.txt", "r") as f:
    kill_regex = [make_regex(it.strip()) for it in f.readlines()]

with open("regex/kill_weapon.txt", "r") as f:
    item_regex = [make_regex(it.strip()) for it in f.readlines()]
