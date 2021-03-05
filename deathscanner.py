import re
import json
import glob
import os

import regexes

def get_start_time(s):
    match = regexes.start_regex.search(s)
    if(match):
        return match.groupdict()['time']

def get_end_time(s):
    match = regexes.end_regex.search(s)
    if(match):
        dc = match.groupdict()
        return (dc["time"], dc["winner"])

def get_death(line):
    for ir in regexes.item_regex:
        match = ir.search(line)
        if(match):
            return match.groupdict()
    for kr in regexes.kill_regex:
        match = kr.search(line)
        if(match):
            return match.groupdict()
    for dr in regexes.death_regex:
        match = dr.search(line)
        if(match):
            return match.groupdict()

def get_death_with_msg(line):
    msg = re.sub(regexes.prefix, "", line)
    match = get_death(line)
    if match:
        match["msg"] = msg.strip()
    return match

def get_start(lst):
    return next((i, get_start_time(v)) for i,v in enumerate(lst) if get_start_time(v))

def get_end(lst):
    i, res = next((i, get_end_time(v)) for i,v in enumerate(lst) if get_end_time(v))
    return (i, res[0], res[1])


def create_files(name):
    with open(f"logs/{name}.log") as file:
        lines = file.readlines()
        start_index, start_time = get_start(lines)
        end_index, end_time, winner = get_end(lines)
        lines = lines[start_index:end_index]
        deaths = [it for it in [get_death_with_msg(line) for line in lines] if it]
        death_lines = [line.strip() for line in lines if get_death(line)]

    obj = {
        "start": start_time,
        "end": end_time,
        "deaths": deaths
    }

    with open(f"json/{name}.json", "w") as file:
        file.write(json.dumps(obj, indent=4))

    with open(f"text/{name}.txt", "w") as file:
        file.write('\n'.join(death_lines))

log_files = os.listdir("logs")
names = ['.'.join(name.split(".")[:-1]) for name in log_files]

if __name__=="__main__":
    for name in names:
        create_files(name)
