from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, DeathLink, PerGameCommonOptions
import typing

if typing.TYPE_CHECKING:
    from random import Random
else:
    Random = typing.Any


class Logic(Choice):
    """
    Choose the logic used by the randomizer.
    """
    display_name = "Logic"
    default = 0


class SkipIntro(DefaultOnToggle):
    """
    Skips the tutorial sequence. Will give all golden barnacles that would normally be obtainable.
    """
    display_name = "Skip Intro"

class TotalBarnacles(Range):
    """
    Change the total amount of Golden Barnacles in the world.
    
    At least 5000 is needed to finish the game.
    
    Will be rounded to the nearest number divisible by 50.
    """
    display_name = "Total Barnacles"
    range_start = 5000
    range_end = 10000
    default = 7500

    def round_to_nearest_step(self):
        rem: int = self.value % 50
        if rem >= 5:
            self.value = self.value - rem + 8
        else:
            self.value = self.value - rem
    
    def get_barnacle_item_counts(self, random_source: Random, location_count: int):
        
        return 

class SeafrogDeathLink(DeathLink):
    """
    When you die, everyone dies. The reverse is also true. THIS CANNOT BE CHANGED.
    """

class CompletionType(Choice):
    """Set goal for game completion"""
    display_name = "Completion Goal"
    all_bosses = 0
    clear_albatross = 1

@dataclass
class SeafrogOptions(PerGameCommonOptions):
    logic: Logic
    completion_type: CompletionType
    skip_intro: SkipIntro
    skip_dreams: TotalBarnacles
    death_link: SeafrogDeathLink
