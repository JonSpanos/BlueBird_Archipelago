from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any
    quantity: int = 1


class BO3Item(Item):
    game: str = "BO3"


item_table = {
    "Juggernog (SoE)":                          ItemData(115001, ItemClassification.progression),
    "Quick Revive (SoE)":                       ItemData(115002, ItemClassification.progression),

    "Stamin-up (SoE)":                          ItemData(115003, ItemClassification.useful),
    "Doubletap (SoE)":                          ItemData(115004, ItemClassification.useful),
    "Widow's Wine (SoE)":                       ItemData(115005, ItemClassification.useful),
    "Speedcola (SoE)":                          ItemData(115006, ItemClassification.useful),
    "Mule Kick (SoE)":                          ItemData(115007, ItemClassification.useful),
    "Shield Top (SoE)":                         ItemData(115008, ItemClassification.useful),
    "Shield Rockets (SoE)":                     ItemData(115009, ItemClassification.useful),
    "Shield Bottom (SoE)":                      ItemData(115010, ItemClassification.useful),

    "Margwa Heart":                             ItemData(115011, ItemClassification.useful),
    "Xenomatter":                               ItemData(115012, ItemClassification.useful),
    "Margwa Tentacle":                          ItemData(115013, ItemClassification.useful),

    "Apothicon Sword":                          ItemData(115014, ItemClassification.useful),
    "Reborn Sword":                             ItemData(115015, ItemClassification.useful),
    "Fumigator":                                ItemData(115016, ItemClassification.progression),

    "Spawn to Courtyard Door":                  ItemData(115017, ItemClassification.progression),
    "Junction to Footlight Door":               ItemData(115018, ItemClassification.progression),
    "Junction to Canal Door":                   ItemData(115019, ItemClassification.progression),
    "Junction to Waterfront Door":              ItemData(115020, ItemClassification.progression),

    "Footlight to Ritual Zone Door":            ItemData(115021, ItemClassification.progression),
    "Footlight Ritual Zone to Walkway Door":    ItemData(115022, ItemClassification.progression),

    "Canal to Ritual Zone Door":                ItemData(115023, ItemClassification.progression),
    "Canal to Walkway Door":                    ItemData(115024, ItemClassification.progression),

    "Waterfront to Ritual Zone Door":           ItemData(115025, ItemClassification.progression),
    "Waterfront to Walkway Door":               ItemData(115026, ItemClassification.progression),

    "Barricade 1":                              ItemData(115027, ItemClassification.useful),
    "Barricade 2":                              ItemData(115028, ItemClassification.useful),
    "Barricade 3":                              ItemData(115029, ItemClassification.useful),
    "Barricade 4":                              ItemData(115030, ItemClassification.useful),

    "Wall KRM-262 (SoE)":                       ItemData(115031, ItemClassification.filler),
    "Wall RK5 (SoE)":                           ItemData(115032, ItemClassification.filler),
    "Wall Sheiva (SoE)":                        ItemData(115033, ItemClassification.filler),
    "Wall Kuda (SoE)":                          ItemData(115034, ItemClassification.filler),
    "Wall M8A7 (SoE)":                          ItemData(115035, ItemClassification.filler),
    "Wall Bootlegger (SoE)":                    ItemData(115036, ItemClassification.filler),
    "Wall HVK-30 (SoE)":                        ItemData(115037, ItemClassification.filler),
    "Wall Trip Mine (SoE)":                     ItemData(115038, ItemClassification.filler),
    "Wall Bowie Knife (SoE)":                   ItemData(115039, ItemClassification.filler),
    "Wall L-CAR 9 (SoE)":                       ItemData(115040, ItemClassification.filler),
    "Wall KN-44 (SoE)":                         ItemData(115041, ItemClassification.filler),
    "Wall VMP (SoE)":                           ItemData(115042, ItemClassification.filler),
    "Wall Vesper (SoE)":                        ItemData(115043, ItemClassification.filler),

}

event_table = {
    "Round 20": ItemData(None, ItemClassification.progression)
}
