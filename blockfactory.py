from abc import ABCMeta, abstractstaticmethod


class IBlockFactory(metaclass=ABCMeta):
    """The Block Interface"""
    @abstractstaticmethod
    def parameters():
        """A static interface method"""


class GenSin(IBlockFactory):
    """The GenSin Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._magnitude = data[1]
        self._frequency = data[2]
        self._phase = data[3]

    def parameters(self):
        return {"magnitude": self._magnitude, "frequency": self._frequency, "phase": self._phase}


class CScope(IBlockFactory):
    """The CScope Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._colorvector = data[1]
        self._ymin = data[2]
        self._ymax = data[3]
        self._refresh_period = data[4]
        self._buffer_size = data[5]
        self._accept_herited_events = data[6]
        self._scope_name = data[7]


    def parameters(self):
        return {"Color or mark vector:" :self._colorvector, "Ymin": self._ymin, "Ymax": self._ymax,"Refresh period" : self._refresh_period ,"Buffer Size": self._buffer_size,"Accept herited events": self._accept_herited_events,"Name of Scope": self._scope_name}


class CSuper(IBlockFactory):
    """The CSuper Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._period = data[1]
        self._intime = data[2]

    def parameters(self):
        return {"Period": self._period, "Initialisation Time": self._intime}



class BlockFactory:
    """Tha Factory Class"""

    @staticmethod
    def get_block(data):
        """A static method to get a block"""
        try:
            if data[0] == "GenSin":
                return GenSin(data)
            if data[0] == "CScope":
                return CScope(data)
            if data[0] == "CSuper":
                return CSuper(data)
            raise AssertionError("Block Not Found")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    inlist1=["GenSin",5,1,0]
    inlist2=["CScope",[1,3,5,7,9,11,13,15],-15,15,30,20,0,None]
    inlist3=["CSuper",0.1,0.1]

    BLOCK_FACTORY1 = BlockFactory().get_block(inlist1)
    BLOCK_FACTORY2 = BlockFactory().get_block(inlist2)
    BLOCK_FACTORY3 = BlockFactory().get_block(inlist3)
print(f"{BLOCK_FACTORY1.__class__} : {BLOCK_FACTORY1.parameters()}")
print(f"{BLOCK_FACTORY2.__class__} : {BLOCK_FACTORY2.parameters()}")
print(f"{BLOCK_FACTORY3.__class__} : {BLOCK_FACTORY3.parameters()}")


