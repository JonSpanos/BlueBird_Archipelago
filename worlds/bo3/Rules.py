from ..generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld, CollectionState

# Sets rules on entrances and advancements that are always applied
def set_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state: state.can_reach("Revelations", "Region", player)

    # Change the state to something else later to check game progression