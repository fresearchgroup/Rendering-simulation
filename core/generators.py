from abc import ABC, abstractmethod
from .blocks import *

class BlockGenerator(ABC):

    def __init__(self, block_root):
        self.data=[]
        for y in block_root.findall(self.ScilabString):
              self.data.append(y.get('value'))
        self.block = self._generate()

    @abstractmethod
    def _generate(self):
        pass
        



class GENSIN_f(BlockGenerator):  
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return GenSin(self.data)


class CSCOPE(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return CScope(self.data)


class CLOCK_c(BlockGenerator):
    ScilabString = "./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"

    def _generate(self):
        return CSuper(self.data)

class CLSS_f(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Csslti(self.data)

class CLOCK_f(BlockGenerator):
    ScilabString = "./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"

    def _generate(self):
        return CSuper(self.data)
class CEVENTSCOPE(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Cevscpe(self.data)

class NEGTOPOS_f(BlockGenerator):
    ScilabString = ""

    def _generate(self):
        pass
class POSTONEG_f(BlockGenerator):
    ScilabString = ""

    def _generate(self):
        pass

class BOUNCEXY(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Bouncexy(self.data)

class BOUNCE(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Bounceball(self.data)


class IFTHEL_f(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Ifthel(self.data)


class VanneReglante(BlockGenerator):

    ScilabString = "./ScilabString/data"

    def _generate(self):
        return VanneReg(self.data)





class SampleCLK(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Sampleclk(self.data)


class RAND_m(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Rand_m(self.data)

class MATCATV(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matcatv(self.data)

class MATCATH(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matcath(self.data)


class CONST_m(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Const_m(self.data)

class GAINBLK(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Gainblk(self.data)

class MATTRAN(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Mattran(self.data)

class MATMUL(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matmul(self.data)
