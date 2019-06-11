from abc import ABCMeta, abstractstaticmethod


class IBlockFactory(metaclass=ABCMeta):
    """The Block Interface"""
    @abstractstaticmethod
    def parameters():
        """A static interface method"""


class GenSin(IBlockFactory):
    """The GenSin Concrete Class which implements the IBlock interface"""

    def __init__(self):
        self._magnitude = 5
        self._frequency = 1
        self._phase = 0

    def parameters(self):
        return {"magnitude": self._magnitude, "frequency": self._frequency, "phase": self._phase}


class CScope(IBlockFactory):
    """The CScope Concrete Class which implements the IBlock interface"""

    def __init__(self):
        self._colorvector = 60
        self._ymin = 60
        self._ymax = 60
        self._refresh_period = 60
        self._buffer_size = 60
        self._accept_herited_events = 60
        self._scope_name = 60


    def parameters(self):
        return {"Color or mark vector:" :self._colorvector, "Ymin": self._ymin, "Ymax": self._ymax,"Refresh period" : self._refresh_period ,"Buffer Size": self._buffer_size,"Accept herited events": self._accept_herited_events,"Name of Scope": self._scope_name}


class CSuper(IBlockFactory):
    """The CSuper Concrete Class which implements the IBlock interface"""

    def __init__(self):
        self._period = 10
        self._intime = 10

    def parameters(self):
        return {"Period": self._period, "Initialisation Time": self._intime}



class BlockFactory:
    """Tha Factory Class"""

    @staticmethod
    def get_block(block):
        """A static method to get a block"""
        try:
            if block == "GenSin":
                return GenSin()
            if block == "CScope":
                return CScope()
            if block == "CSuper":
                return CSuper()
            raise AssertionError("Block Not Found")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    BLOCK_FACTORY = BlockFactory().get_block("GenSin")
print(f"{BLOCK_FACTORY.__class__} : {BLOCK_FACTORY.parameters()}")
