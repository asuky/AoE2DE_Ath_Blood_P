from __future__ import annotations
import sys

class _vars:
    class CosntError(TypeError):
        pass

    def __init__(self):
        # List of "In-Game (on Editor)" variables (max: 0-255 (index))
        # Use "In-Game" variables via this class

        ## Enemy Kills Counter 0-7
        self.ENEMY_KILLS = 0
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value

sys.modules[__name__] = _vars()