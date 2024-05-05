from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class BO3Advancement(Location):
    game: str = "BO3"
bo3LocTable = {
    "(SoE) Juggernog Machine":                           AdvData(915001, "Shadows of Evil"),
    "(SoE) Quick Revive Machine":                        AdvData(915002, "Shadows of Evil"),
    "(SoE) Stamin-up Machine":                           AdvData(915003, "Shadows of Evil"),
    "(SoE) Doubletap Machine":                           AdvData(915004, "Shadows of Evil"),
    "(SoE) Widow's Wine Machine":                        AdvData(915005, "Shadows of Evil"),
    "(SoE) Speedcola Machine":                           AdvData(915006, "Shadows of Evil"),
    "(SoE) Mule Kick Machine":                           AdvData(915007, "Shadows of Evil"),

    "(SoE) Shield Top":                                  AdvData(915008, "Shadows of Evil"),
    "(SoE) Shield Rockets":                              AdvData(915009, "Shadows of Evil"),
    "(SoE) Shield Bottom":                               AdvData(915010, "Shadows of Evil"),

    "Margwa Heart":                                      AdvData(915011, "Shadows of Evil"),
    "Xenomatter":                                        AdvData(915012, "Shadows of Evil"),
    "Margwa Tentacle":                                   AdvData(915013, "Shadows of Evil"),

    "Apothicon Sword":                                   AdvData(915014, "Shadows of Evil"),
    "Reborn Sword":                                      AdvData(915015, "Shadows of Evil"),
    "Fumigator":                                         AdvData(915016, "Shadows of Evil"),

    "Spawn to Junction Door":                            AdvData(915017, "Shadows of Evil"),
    "Junction to Footlight Door":                        AdvData(915018, "Shadows of Evil"),
    "Junction to Canal Door":                            AdvData(915019, "Shadows of Evil"),
    "Junction to Waterfront Door":                       AdvData(915020, "Shadows of Evil"),

    "Footlight to Ritual Zone Door":                     AdvData(915021, "Shadows of Evil"),
    "Footlight Ritual Zone to Walkway Door":             AdvData(915022, "Shadows of Evil"),

    "Canal to Ritual Zone Door":                         AdvData(915023, "Shadows of Evil"),
    "Canal to Walkway Door":                             AdvData(915024, "Shadows of Evil"),

    "Waterfront to Ritual Zone Door":                    AdvData(915025, "Shadows of Evil"),
    "Waterfront to Walkway Door":                        AdvData(915026, "Shadows of Evil"),

    "Barricade 1":                                       AdvData(915027, "Shadows of Evil"),
    "Barricade 2":                                       AdvData(915028, "Shadows of Evil"),
    "Barricade 3":                                       AdvData(915029, "Shadows of Evil"),
    "Barricade 4":                                       AdvData(915030, "Shadows of Evil"),

    "(SoE) Wall KRM-262":                                AdvData(915031, "Shadows of Evil"),
    "(SoE) Wall RK5":                                    AdvData(915032, "Shadows of Evil"),
    "(SoE) Wall Sheiva":                                 AdvData(915033, "Shadows of Evil"),
    "(SoE) Wall Kuda":                                   AdvData(915034, "Shadows of Evil"),
    "(SoE) Wall M8A7":                                   AdvData(915035, "Shadows of Evil"),
    "(SoE) Wall Bootlegger":                             AdvData(915036, "Shadows of Evil"),
    "(SoE) Wall HVK-30":                                 AdvData(915037, "Shadows of Evil"),
    "(SoE) Wall Trip Mine":                              AdvData(915038, "Shadows of Evil"),
    "(SoE) Wall Bowie Knife":                            AdvData(915039, "Shadows of Evil"),
    "(SoE) Wall L-CAR 9":                                AdvData(915040, "Shadows of Evil"),
    "(SoE) Wall KN-44":                                  AdvData(915041, "Shadows of Evil"),
    "(SoE) Wall VMP":                                    AdvData(915042, "Shadows of Evil"),
    "(SoE) Wall Vesper":                                 AdvData(915043, "Shadows of Evil"),
}

