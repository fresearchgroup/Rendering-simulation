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
        return Negtopos_f(self.data)
class POSTONEG_f(BlockGenerator):
    ScilabString = None

    def _generate(self):
        return Postoneg_f(self.data)

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
        return Saturation(self.data)

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
        return Sum_f(self.data)

class CLR(BlockGenerator):
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

class VoltageSensor(BlockGenerator):
    ScilabString= None

    def _generate(self):
        return Voltagesen(self.data)

class CurrentSensor(BlockGenerator):
    ScilabString= None

    def _generate(self):
        return Currentsen(self.data)

class Resistor(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Resist(self.data)

class STEP_FUNCTION(BlockGenerator):
    ScilabString="./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"

    def _generate(self):
        return Step_function(self.data)

class Ground(BlockGenerator):
    ScilabString= None

    def _generate(self):
        return Groundb(self.data)

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
    ScilabString = None


    def _generate(self):
        return CCSB(self.data)

class BIGSOM_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return BigSom(self.data)

class generic_block3(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Generic_block(self.data)


class c_block(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return Cblock(self.data)

class fortran_block(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return Fortran(self.data)



class DEBUG(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return Debug(self.data)


class EXPRESSION(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Expression(self.data)

class CBLOCK4(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return Cblock4(self.data)

class CBLOCK(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return Cblock2(self.data)


class MBLOCK(BlockGenerator):
    ScilabString = ".Array/ScilabString/data"


    def _generate(self):
        return MBlock(self.data)



class BPLATFORM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Bplatform(self.data)

class Flowmeter(BlockGenerator):
    ScilabString = None

    def _generate(self):
        return FlowMeter(self.data)

class CLKINV_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Clkinv(self.data)



class TIME_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Timef(self.data)


class RAMP(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Ramp(self.data)


class CONST_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Const_f(self.data)


class CONST(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Const(self.data)




class SAWTOOTH_f (BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Sawtooth(self.data)



class PULSE_SC(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Pulse(self.data)



class Sigbuilder(BlockGenerator):
    ScilabString="./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"

    def _generate(self):
        return SigBuild(self.data)

class Modulo_Count(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return ModCount(self.data)


class Counter(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Count(self.data)

class TKSCALE(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return TkScale(self.data)


class FROMWSB(BlockGenerator):
    ScilabString="./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"

    def _generate(self):
        return FromWsb(self.data)


class READAU_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return TkScale(self.data)


class READC_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Readc(self.data)


class RFILE_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Rfile(self.data)

class INIMPL_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Inimpl(self.data)

class IN_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return In_f(self.data)

class CONSTRAINT_c(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Constraint_c(self.data)

class DIFF_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Diff_f(self.data)
class GENERAL_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return GenF(self.data)

class ZCROSS_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Zcrossf(self.data)

class AFFICH_m(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Affichm(self.data)

class BARXY(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Barxy(self.data)


class CSCOPXY3D(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Cscopxy3d(self.data)


class WRITEAU_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Writeauf(self.data)


class CANIMXY(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Canimxy(self.data)


class CMAT3D(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Cmat3d(self.data)




class WRITEC_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Writecf(self.data)



class CANIMXY3D(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Canimxy3d(self.data)


class CFSCOPE(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Cfscope(self.data)

class CSCOPXY(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Cscopxy(self.data)




class CMATVIEW(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Cmatview(self.data)


class TRASH_f (BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Trashf(self.data)

class TOWS_c(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Cmatview(self.data)

class OUT_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Outf(self.data)

class OUTIMPL_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Outimpf(self.data)

class DEMUX(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Demux(self.data)

class DEMUX_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Demuxf(self.data)

class EXTRACTOR(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Extractor(self.data)

class SELF_SWITCH(BlockGenerator):
    ScilabString=None

    def _generate(self):
        return Self_switch(self.data)

class ISELECT_m(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Iselectm(self.data)


class SCALAR2VECTOR(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Scalar2Vec(self.data)


class MUX_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Muxf(self.data)



class M_SWITCH(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Mswitch(self.data)

class FROM(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return From(self.data)

class FROMMO(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return FromMo(self.data)

class NRMSOM_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Nrmsomf(self.data)


class RELAY_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Relayf(self.data)

class GotoTagVisibility(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Gototagvis(self.data)

class GotoTagVisibilityMO(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return GototagvisMO(self.data)

class SELECT_m(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Selectm(self.data)

class SWITCH_f(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Switchf(self.data)

class SWITCH2_m(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Switch2m(self.data)

class CVS(BlockGenerator):
    ScilabString=None

    def _generate(self):
        return CvsB(self.data)

class Capacitor(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Capacit(self.data)

class ConstantVoltage(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return ConstVolt(self.data)

class Diode(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Diodeb(self.data)

class OpAmp(BlockGenerator):
    ScilabString=None

    def _generate(self):
        return Opamp(self.data)


class IdealTransformer(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return IdealTrans(self.data)


class Gyrator(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Gyrat(self.data)

class PotentialSensor(BlockGenerator):
    ScilabString=None

    def _generate(self):
        return PotSensor(self.data)


class VsourceAC(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return VSource(self.data)

class VVsourceAC(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return VVSource(self.data)

class VariableResistor(BlockGenerator):
    ScilabString=None

    def _generate(self):
        return VarResist(self.data)

class NMOS(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Nmos(self.data)

class PMOS(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Pmos(self.data)

class PNP(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Pnpb(self.data)

class NPN(BlockGenerator):
    ScilabString="./ScilabString/data"

    def _generate(self):
        return Npnb(self.data)


class BACKLASH(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Backlash(self.data)


class DEADBAND(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Backlash(self.data)

class DELAYV_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Delayv_f(self.data)

class HYSTHERESIS(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Hystheresis(self.data)

class RATELIMITER(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Ratelimiter(self.data)

class QUANT_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Quant_f(self.data)
'''
class SATURATION(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Saturation(self.data)
'''
class AUTOMAT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Automat(self.data)


class DOLLAR_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Dollar_f(self.data)

class DOLLAR_m(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Dollar_m(self.data)

class DOLLAR(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Dollar(self.data)

class REGISTER_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Delay_f(self.data)

class DLSS(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Dlss(self.data)

class TCLSS(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Tclss(self.data)

class DLR(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Dlr(self.data)

class REGISTER(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Register(self.data)

class DLRADAPT_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Dlradapt_f(self.data)

class SAMPHOLD_m(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Samphold_m(self.data)

class DELAY_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Delay_f(self.data)

class INTRPLBLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Interp(self.data)


class INTRP2BLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Interp2(self.data)

class LOOKUP_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Lookup_f(self.data)

class ANDLOG_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Lookup_f(self.data)

class EVTVARDLY(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Evtvardly(self.data)

class EVTGEN_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Evtgen_f(self.data)

class VirtualCLK0(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Virtualclock0(self.data)

class ANDBLK(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Andblk(self.data)

class Extract_Activation(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Extract_activation(self.data)

class CLKOUTV_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Clkoutv_f(self.data)

class CLKGOTO(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Clkgoto(self.data)

class M_freq(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Mfreq(self.data)

class END_c(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return End(self.data)

class ENDBLK(BlockGenerator):
    ScilabString = "./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"


    def _generate(self):
        return Endblk(self.data)

class freq_div(BlockGenerator):
    ScilabString = "./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"


    def _generate(self):
        return freqdiv(self.data)

class MCLOCK_f(BlockGenerator):
    ScilabString = "./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"


    def _generate(self):
        return Mclock_f(self.data)

class HALT_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Halt_f(self.data)

class MFCLCK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Mfclck_f(self.data)

class ESELECT_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Eselect_f(self.data)

class CLKFROM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Clkfrom(self.data)



class EDGE_TRIGGER(BlockGenerator):
    ScilabString = "./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"


    def _generate(self):
        return Edge_trigger(self.data)

class CLKGotoTagVisibility(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Clkgototagvisiblity(self.data)

class EVTDLY_c(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Evtdly_c(self.data)

class SINBLK_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Sinblk_f(self.data)
'''
class GAINBLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Gainblkf(self.data)
'''

class GAIN_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Gain_f(self.data)

class PROD_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Prod_f(self.data)

class COSBLK_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Cosblk_f(self.data)

class TANBLK_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Tanblk_f(self.data)

class MAX_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Max_f(self.data)


class MIN_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Min_f(self.data)
'''
class MIN_f(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Min_f(self.data)
'''

class PRODUCT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Product(self.data)

class SIGNUM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Signum(self.data)

class ABS_VALUE(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Absvalue(self.data)

class INVBLK(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Invblk(self.data)
'''
class TANBLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Tanblk_f(self.data)
'''

class LOGBLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Logblk_f(self.data)

class MAXMIN(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Maxmin(self.data)


class MATZREIM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matzreim(self.data)

class SQRT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Sqrt(self.data)

class RELATIONALOP(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Relationalop(self.data)

class POWBLK_f(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Powblk_f(self.data)

class EXPBLK_m(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Expblk_m(self.data)

class TrigFun(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Trigfun(self.data)

class MATMAGPHI(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matmagphi(self.data)

class DLATCH(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Dlatch(self.data)

class MATRESH(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matresh(self.data)

class MATSING(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matsing(self.data)

class DFLIPFLOP(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Dflipflop(self.data)


class MATPINV(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matpinv(self.data)

class BITCLEAR(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Bitclear(self.data)

class BITSET(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Bitset(self.data)

class EXTTRI(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Exttri(self.data)

class MATBKSL(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matbksl(self.data)

class LOGICAL_OP(BlockGenerator):
    ScilabString = "./mxGraphModel/root/BasicBlock/SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"


    def _generate(self):
        return Logical_op(self.data)

class MATZCONJ(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Matzconj(self.data)

class MATDIAG(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matdiag(self.data)

class MATDIV(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matdiv(self.data)

class MATDET(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matdet(self.data)

class MATLU(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matlu(self.data)

class MATEXPM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matexpm(self.data)

class INTMUL(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Intmul(self.data)

class RICC(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Ricc(self.data)

class CONVERT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Convert(self.data)

class CUMSUM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Cumsum(self.data)

class MATSUM(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Matsum(self.data)

class SUBMAT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Submat(self.data)

class EXTRACTBITS(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Extractbits(self.data)


class SHIFT(BlockGenerator):
    ScilabString = "./ScilabString/data"


    def _generate(self):
        return Shift(self.data)

class DERIV(BlockGenerator):
    ScilabString = None


    def _generate(self):
        return Deriv(self.data)
