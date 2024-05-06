from BaseClasses import MultiWorld


def link_bo3_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
bo3_regions = [
    ("Menu", ["SoE Select","TG Select","DE Select","ZnS Select","GK Select","REV Select"]),
    ("Shadows of Evil", []),
    ("The Giant", []),
    ("Der Eisendrache", []),
    ("Zetsubou no Shima", []),
    ("Gorod Krovi", []),
    ("Revelations", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("SoE Select", "Shadows of Evil"),
    ("TG Select", "The Giant"),
    ("DE Select", "Der Eisendrache"),
    ("ZnS Select", "Zetsubou no Shima"),
    ("GK Select", "Gorod Krovi"),
    ("REV Select", "Revelations"),
]

