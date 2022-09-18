from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.trigger_lists import Attribute, DiplomacyState

import sys

class _const:
    class ConstError(TypeError):
        pass

    def __init__(self):
        # Version counter
        self.VERSION = 'va0'

        # Logic Labels
        self.DIPLO_ALLY = DiplomacyState.ALLY
        self.NOT = 1
        self.DISABLED = 0
        self.ENABLED = 1

        # Flag for commonly using logic
        self.BIN_FLAG = OtherInfo.ES_FLAG

        # Kill Counter Attribute
        self.NUM_OF_KILLS = {
            PlayerId.ONE: Attribute.KILLS_BY_P1,
            PlayerId.TWO: Attribute.KILLS_BY_P2,
            PlayerId.THREE: Attribute.KILLS_BY_P3,
            PlayerId.FOUR: Attribute.KILLS_BY_P4,
            PlayerId.FIVE: Attribute.KILLS_BY_P5,
            PlayerId.SIX: Attribute.KILLS_BY_P6,
            PlayerId.SEVEN: Attribute.KILLS_BY_P7,
            PlayerId.EIGHT: Attribute.KILLS_BY_P8,
        }

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value

sys.modules[__name__]=_const()