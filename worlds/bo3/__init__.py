from .Items import TLNItem, item_table, event_table
from .Locations import TLNAdvancement, tlnLocTable
from .Regions import tln_regions, link_tln_areas
from .Rules import set_rules
from BaseClasses import Region, Entrance
from .Options import tln_options
from worlds.AutoWorld import World

import logging


class BO3World(World):
    """
    Touhou Luna Nights is a Metroidvania title with a heavy emphasis on exploration and action.　 
    Developed by Team Ladybug, creators of multiple fantastic action games thus far.
    """
    game = "BO3"
    option_definitions = bo3_options
    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in bo3LocTable.items()}

    data_version = 5

    def _get_bo3_data(self):
        return {
            "world_seed": self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "race": self.multiworld.is_race,
        }

    def create_items(self):
        self.multiworld.get_location("Stage 5: Flandre", self.player).place_locked_item(self.create_event("Defeat Flandre"))
        itempool = []
        for item_name, data in item_table.items():
            itempool += [self.create_item(item_name) for _ in range(0, data.quantity)]

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_regions(self):
        def BO3Region(region_name: str, exits):
            ret = Region(region_name, self.player, self.multiworld)

            for loc_name, loc_data in bo3LocTable.items():
                if loc_data.region == region_name:
                    ret.locations += [BO3Advancement(self.player, loc_name, loc_data.id, ret)]

            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [BO3Region(*r) for r in bo3_regions]
        link_bo3_areas(self.multiworld, self.player)

    def fill_slot_data(self):
        slot_data = self._get_bo3_data()

        return slot_data

    def create_item(self, name: str) -> BO3Item:
        item_data = item_table[name]
        return BO3Item(name, item_data.classification, item_data.code, self.player)

    def create_event(self, name: str) -> BO3Item:
        data = event_table[name]
        return BO3Item(name, data.classification, data.code, self.player)