import sys

class _const:
    class ConstError(TypeError):
        pass

    def __init__(self):
        # Version counter
        self.VERSION = 'va0'

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value

sys.modules[__name__]=_const()