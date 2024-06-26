from BaseClasses import MultiWorld


def link_tln_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
tln_regions = [
    ("Menu", ["Game Start"]),
    ("Stage 00", ["Defeat Meiling"]),
    ("Stage 01", ["Defeat Marisa"]),
    ("Stage 02", ["Defeat Patchouli"]),
    ("Stage 03", ["Defeat Remilia"]),
    ("Stage 04", ["Defeat Nitori"]),
    ("Stage 05", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("Game Start", "Stage 00"),
    ("Defeat Meiling", "Stage 01"),
    ("Defeat Marisa", "Stage 02"),
    ("Defeat Patchouli", "Stage 03"),
    ("Defeat Remilia", "Stage 04"),
    ("Defeat Nitori", "Stage 05"),
]
