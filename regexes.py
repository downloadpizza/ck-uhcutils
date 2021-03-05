import re

killed = r'(?P<killed>[a-zA-Z0-9_]{3,})'
killer = r'(?P<killer>[a-zA-Z0-9_]{3,})'
item = r'(?P<item>.+)'
prefix = r'\[(?P<time>[0-9]{2}:[0-9]{2}:[0-9]{2})] \[.+\/INFO]: \[CHAT] '

start_regex = re.compile(prefix + "The Overworld world border started shrinking\.")
end_regex = re.compile(prefix + "(?P<winner>.+) has won the game!")
        

def make_regex(s):
    mod = s.replace("<player>", "KILLED").replace("<player/mob>", "KILLER").replace("<item>", "ITEM")
    mod = re.escape(mod)
    mod = prefix + mod.replace("KILLED", killed).replace("KILLER", killer).replace("ITEM", item)
    return re.compile(mod)

death_regex = [
 '<player> was pricked to death',
 '<player> drowned',
 '<player> experienced kinetic energy',
 '<player> blew up',
 '<player> was killed by [Intentional Game Design]',
 '<player> hit the ground too hard',
 '<player> fell from a high place',
 '<player> fell off a ladder',
 '<player> fell off some vines',
 '<player> fell off some weeping vines',
 '<player> fell off some twisting vines',
 '<player> fell off scaffolding',
 '<player> fell while climbing',
 '<player> was squashed by a falling anvil',
 '<player> was squashed by a falling block',
 '<player> was skewered by a falling stalactite',
 '<player> went up in flames',
 '<player> burned to death',
 '<player> went off with a bang',
 '<player> tried to swim in lava',
 '<player> was struck by lightning',
 '<player> discovered the floor was lava',
 '<player> was killed by magic',
 '<player> froze to death',
 '<player> was stung to death',
 '<player> starved to death',
 '<player> suffocated in a wall',
 '<player> was squished too much',
 '<player> was poked to death by a sweet berry bush',
 '<player> fell out of the world',
 '<player> withered away',
 '<player> was roasted in dragon breath',
 '<player> died',
 '<player> was doomed to fall',
 '<player> was killed by even more magic',
 '<player> was too soft for this world',
 '<player> was slain by Arrow',
 '<player> was pricked to death',
 '<player> drowned',
 '<player> experienced kinetic energy',
 '<player> blew up',
 '<player> hit the ground too hard',
 '<player> fell from a high place',
 '<player> was squashed by a falling anvil',
 '<player> was squashed by a falling block',
 '<player> went up in flames',
 '<player> burned to death',
 '<player> went off with a bang',
 '<player> tried to swim in lava',
 '<player> was struck by lightning',
 '<player> discovered floor was lava',
 '<player> was killed by magic',
 '<player> was slain by Small Fireball',
 '<player> starved to death',
 '<player> suffocated in a wall',
 '<player> fell out of the world',
 '<player> withered away',
 '<player> died',
 '<player> fell off a ladder',
 '<player> fell off some vines',
 '<player> fell out of the water',
 '<player> was doomed to fall'
]

death_regex = [make_regex(it) for it in death_regex]

kill_regex = [
 '<player> was shot by <player/mob>',
 '<player> was pummeled by <player/mob>',
 '<player> walked into a cactus whilst trying to escape <player/mob>',
 '<player> drowned whilst trying to escape <player/mob>',
 '<player> experienced kinetic energy whilst trying to escape <player/mob>',
 '<player> was blown up by <player/mob>',
 '<player> hit the ground too hard whilst trying to escape <player/mob>',
 '<player> was impaled on a stalagmite whilst fighting <player/mob>',
 '<player> was squashed by a falling anvil whilst fighting <player/mob>',
 '<player> was squashed by a falling block whilst fighting <player/mob>',
 '<player> was skewered by a falling stalactite whilst fighting <player/mob>',
 '<player> walked into fire whilst fighting <player/mob>',
 '<player> was burnt to a crisp whilst fighting <player/mob>',
 '<player> tried to swim in lava to escape <player/mob>',
 '<player> was struck by lightning whilst fighting <player/mob>',
 '<player> walked into danger zone due to <player/mob>',
 '<player> was killed by magic whilst trying to escape <player/mob>',
 '<player> was killed by <player/mob> using magic',
 '<player> was frozen to death by <player/mob>',
 '<player> was slain by <player/mob>',
 '<player> was fireballed by <player/mob>',
 '<player> was shot by a skull from <player/mob>',
 '<player> starved to death whilst fighting <player/mob>',
 '<player> suffocated in a wall whilst fighting <player/mob>',
 '<player> was squashed by <player/mob>',
 '<player> was poked to death by a sweet berry bush whilst trying to escape <player/mob>',
 '<player> was killed trying to hurt <player/mob>',
 '<player> was impaled by <player/mob>',
 "<player> didn't want to live in the same world as <player/mob>",
 '<player> withered away whilst fighting <player/mob>',
 '<player> was roasted in dragon breath by <player/mob>',
 '<player> died because of <player/mob>',
 '<player> was doomed to fall by <player/mob>',
 '<player> fell too far and was finished by <player/mob>',
 '<player> was stung to death by <player/mob>',
 '<player> went off with a bang whilst fighting <player/mob>',
 '<player> was too soft for this world (<player/mob> helped)',
 '<player> was shot by <player/mob>',
 '<player> was blown up by <player/mob>',
 '<player> was killed by <player/mob> using magic',
 '<player> was slain by <player/mob>',
 '<player> was killed trying to hurt <player/mob>',
 '<player> was impaled to death by <player/mob>',
 '<player> was fireballed by <player/mob>',
 '<player> was sniped by <player/mob>',
 '<player> was spitballed by <player/mob>',
 '<player> walked into a cactus whilst trying to escape <player/mob>',
 '<player> drowned whilst trying to escape <player/mob>',
 '<player> walked into fire whilst fighting <player/mob>',
 '<player> tried to swim in lava to escape <player/mob>',
 '<player> walked on danger zone due to <player/mob>',
 '<player> was burnt to a crisp whilst fighting <player/mob>',
 '<player> was pummeled by <player/mob>',
 '<player> was doomed to fall by <player/mob>',
 '<player> fell too far and was finished by <player/mob>'
]

kill_regex = [make_regex(it) for it in kill_regex]

item_regex = [
 '<player> was shot by <player/mob> using <item>',
 '<player> was pummeled by <player/mob> using <item>',
 '<player> was blown up by <player/mob> using <item>',
 '<player> went off with a bang due to a firework fired from <item> by <player/mob>',
 '<player> was killed by <player/mob> using <item>',
 '<player> was slain by <player/mob> using <item>',
 '<player> was fireballed by <player/mob> using <item>',
 '<player> was killed by <item> trying to hurt <player/mob>',
 '<player> was impaled by <player/mob> with <item>',
 '<player> was doomed to fall by <player/mob> using <item>',
 '<player> fell too far and was finished by <player/mob> using <item>',
 '<player> was shot by <player/mob> using <item>',
 '<player> was fireballed by <player/mob> using <item>',
 '<player> was killed by <player/mob> using <item>',
 '<player> was pummeled by <player/mob> using <item>',
 '<player> was doomed to fall by <player/mob> using <item>',
 '<player> fell too far and was finished by <player/mob> using <item>'
]

item_regex = [make_regex(it) for it in item_regex]
