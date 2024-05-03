from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class BO3Advancement(Location):
    game: str = "BO3"

bo3LocTable = {
    "Juggernog (SoE)"                       AdvData(210001, "Shadows of Evil"),
    "Quick Revive (SoE)"                       AdvData(210002, "Shadows of Evil"),
    "Stamin-up (SoE)"                       AdvData(210003, "Shadows of Evil"),
    "Doubletap (SoE)"                       AdvData(210004, "Shadows of Evil"),
    "Widow's Wine (SoE)"                       AdvData(210005, "Shadows of Evil"),
    "Speedcola (SoE)"                       AdvData(210006, "Shadows of Evil"),
    "Mule Kick (SoE)"                       AdvData(210007, "Shadows of Evil"),

}
