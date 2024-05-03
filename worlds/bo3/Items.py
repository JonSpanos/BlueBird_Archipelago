from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any
    quantity: int = 1


class BO3Item(Item):
    game: str = "BO3"


item_table = {
    "Juggernog": ItemData(787801, ItemClassification.progression),
    "Quick Revive": ItemData(787802, ItemClassification.progression),

    "Stamin-up": ItemData(787803, ItemClassification.useful),
    "Doubletap": ItemData(787804, ItemClassification.useful),
    "Widow's Wine": ItemData(787805, ItemClassification.useful),
    "Speedcola": ItemData(787806, ItemClassification.useful),
    "Mule Kick": ItemData(787807, ItemClassification.useful),
}

event_table = {
    
}
