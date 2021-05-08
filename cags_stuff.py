import regexes

with open("death.txt", "w") as f:
    for rx in regexes.death_regex_raw:
        f.write(rx.replace("<player>", "KILLED")+"\n")

with open("kill.txt", "w") as f:
    for rx in regexes.kill_regex_raw:
        f.write(rx.replace("<player>", "KILLED")
                .replace("<player/mob>", "KILLER") + "\n")

with open("kill_weapon.txt", "w") as f:
    for rx in regexes.item_regex_raw:
        f.write(rx.replace("<player>", "KILLED")
                .replace("<player/mob>", "KILLER")
                .replace("<item>", "ITEM")+"\n")

