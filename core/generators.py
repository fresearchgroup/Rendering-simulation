from abc import ABC, abstractmethod
from .blocks import *

class BlockGenerator(ABC):

    def __init__(self, block_root):
        self.data=[]
        if self.ScilabString:
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

class CLSS(BlockGenerator):
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
    ScilabString = None

    def _generate(self):
        pass
class POSTONEG_f(BlockGenerator):
    ScilabString = None

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

class SUMMATION(BlockGenerator):
    ScilabString = "./ScilabString/data"

    def _generate(self):
        return Summation(self.data)



class SourceP(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Sourcep(self.data)

class MATEIG(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Mateig(self.data)
        

class Bache(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Bacheb(self.data)

class ROOTCOEF(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Rootcoef(self.data)    
        


class PerteDP(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return PerteDp(self.data)


class EXTRACT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Extract(self.data)    
        


class SATURATION(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Satur(self.data)

class INTEGRAL_m(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Integral_m(self.data)

class scifunc_block_m(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return Sci_func_block_m(self.data)

class SUM_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        pass

class CLR_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Clrf(self.data)

class MATINV(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matinv(self.data)

class CURV_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        pass
class PuitsP(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Puits(self.data)

class MUX(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Mux(self.data)    
        

class GAINBLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Gainblkf(self.data)

class GENSQR_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Gensqr(self.data)
        

class CMSCOPE(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Cmscope(self.data)


class Inductor(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Induct(self.data)

class SineVoltage(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return SineV(self.data)



class Switch(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return SwitchB(self.data)



class CCS(BlockGenerator):
    ScilabString = ""


    def _generate(self):
        return CCSB(self.data)



