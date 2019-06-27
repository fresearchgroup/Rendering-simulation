from abc import ABC, abstractmethod

class Block(ABC):
    """
    Abstract class for blocks
    """

    @abstractmethod
    def parameters(self):
        pass


class GenSin(Block):
    """The GenSin Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname = "GENSIN_f"
        self._magnitude = data[0]
        self._frequency = data[1]
        self._phase = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"magnitude:": self._magnitude, "frequency:": self._frequency, "phase:": self._phase}

class CScope(Block):
    """The CScope Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CSCOPE"
        self._colorvector = data[0]
        self._output_window_number = data[1]
        self._output_window_position = data[2]
        self._output_window_sizes = data[3]
        self._ymin = data[4]
        self._ymax = data[5]
        self._refresh_period = data[6]
        self._buffer_size = data[7]
        self._accept_herited_events = data[8]
        self._scope_name = data[9]

    def parameters(self):
        return {"Function Name:":self._funcname,"Color or mark vector:" :self._colorvector,"Output window number:":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Ymin:": self._ymin, "Ymax:": self._ymax,"Refresh period:" : self._refresh_period ,"Buffer Size:": self._buffer_size,"Accept herited events:": self._accept_herited_events,"Name of Scope:": self._scope_name}


class CSuper(Block):
    """The CSuper Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname = "CLOCK_c"
        self._period = data[0]
        self._intime = data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Period:": self._period, "Initialisation Time:": self._intime}

class Sampleclk(Block):
    """The SampleCLK Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SampleCLK"
        self._sample_time = data[0]
        self._offset = data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Sample_time:": self._sample_time, "Offset:": self._offset}

class Rand_m(Block):
    """The Rand_m Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="RAND_m"
        self._data_type = data[0]
        self._A = data[1]
        self._B = data[2]
        self._seed = data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"Data_Type:": self._data_type, "A:": self._A,"B:": self._B,"SEED:": self._seed}

class Matcatv(Block):
    """The Matcatv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATCATV"
        self._number_of_input = data[0]

    def parameters(self):
      return {"Function Name:":self._funcname,"Number of input:": self._number_of_input}
class Matcath(Block):
    """The Matcath Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATCATH"
        self._number_of_input = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Number of input:": self._number_of_input}

class Const_m(Block):
    """The Const_m Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CONST_m"
        self._constant_value = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Constant Value:": self._constant_value}



class Csslti(Block):
    """The Csslti Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._funcname = "CLSS_f"
        self._amatrix = data[0]
        self._bmatrix = data[1]
        self._cmatrix = data[2]
        self._dmatrix = data[3]
        self._initstate = data[4]


    def parameters(self):

        return {"Function Name:":self._funcname,"A Matrix:": self._amatrix,"B Matrix:": self._bmatrix,"C Matrix:": self._cmatrix,"D Matrix:": self._dmatrix ,"Initial State:": self._initstate}

class Cevscpe(Block):
    """The Cevscope Concrete Class which implements the IBlock interface"""


    def __init__(self, data):
        self._funcname = "CEVENTSCOPE"
        self._colorvector = data[0]
        self._output_window_number = data[1]
        self._output_window_position = data[2]
        self._output_window_sizes = data[3]
        self._refresh_period = data[4]

    def parameters(self):

        return {"Function Name:":self._funcname,"Color or mark vector:" :self._colorvector,"Output window number:":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes,"Refresh period:" : self._refresh_period}

class Bouncexy(Block):
     """The Bouncexy Concrete Class which implements the IBlock interface"""


     def __init__(self, data):
            self._funcname = "BOUNCEXY"
            self._colors = data[0]
            self._radii = data[1]
            self._output_window_number = data[2]
            self._animation_mode = data[3]
            self._xmin = data[4]
            self._xmax = data[5]
            self._ymin = data[6]
            self._ymax = data[7]


     def parameters(self):

        return {"Function Name:":self._funcname,"Colors" :self._colors,"Radii:":self._radii,"Window number(-1 for automatic):":self._output_window_number,"Animation mode(0,1):":self._animation_mode,"Xmin:" : self._xmin,"Xmax:" : self._xmax,"Ymin:" : self._ymin,"Ymax:" : self._ymax}
class Bounceball(Block):
    """The Bounceball Concrete Class which implements the IBlock interface"""


    def __init__(self, data):
            self._funcname = "BOUNCE"
            self._mass = data[0]
            self._radius = data[1]
            self._xmin_xmax_ymin_ymax = data[2]
            self._xpos = data[3]
            self._xdpos = data[4]
            self._ypos = data[5]
            self._ydpos = data[6]
            self._gravity = data[7]
            self._aero = data[8]


    def parameters(self):

        return {"Function Name:":self._funcname,"Mass:" :self._mass,"Radius:":self._radius,"[xmin,xmas,ymin,ymax]:":self._xmin_xmax_ymin_ymax,"xpos:":self._xpos,"xdpos:" : self._xdpos,"ypos:" : self._ypos,"ydpos:" : self._ydpos,"g(gravity):" : self._gravity,"C(aerodynamic coeff):" : self._aero}


class Ifthel(Block):
        """The Ifthel Concrete Class which implements the IBlock interface"""

        def __init__(self,data):
            self._funcname = "IFTHEL_f"
            self._inherit = data[0]
            self._zero_crossing = data[1]

        def parameters(self):

            return {"Function Name:":self._funcname,"Inherit(1:no , 0:yes):": self._inherit, "zero crossing(0:no , 1:yes):": self._zero_crossing}


#VanneReglante
class VanneReg(Block):
        """The VanneReglante Concrete Class which implements the IBlock interface"""

        def __init__(self,data):
            self._funcname = "VanneReglante"
            self._cvmax = data[0]
            self._p_rho = data[1]

        def parameters(self):

            return {"Function Name:":self._funcname," Cvmax": self._cvmax, "p_rho": self._p_rho}




class Gainblk(Block):
    """The Gainblk Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="GAINBLK"
        self._gain = data[0]
        self._do_on_overflow=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Gain:":self._gain,"Do on Overflow:":self._do_on_overflow}

class Mattran(Block):
    """The Mattran Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATTRAN"
        self._datatype= data[0]
        self._rule=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Rule:":self._rule}

class Matmul(Block):
    """The Matmul Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATMUL"
        self._datatype= data[0]
        self._multiplication=data[1]
        self._do_on_overflow = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Multiplication Rule:":self._multiplication,"Do on Overflow:":self._do_on_overflow}


class Summation(Block):
    """The Summation Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SUMMATION"
        self._datatype= data[0]
        self._number_of_input=data[1]
        self._do_on_overflow = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Number of Input or Sign Vector:":self._number_of_input,"Do on Overflow:":self._do_on_overflow}

class Mateig(Block):
    """The Mateig Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATEIG"
        self._datatype= data[0]
        self._decomposition_type=data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Decomposition Type:":self._decomposition_type}


class Rootcoef(Block):
    """The Rootcoef Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ROOTCOEF"
        self._datatype= data[0]
        self._input_size_row=data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Input Size of Row data:":self._input_size_row}

class Extract(Block):
    """The Extract Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EXTRACT"
        self._datatype= data[0]
        self._line_to_extract=data[1]
        self._columns_to_extract=data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Line to extract:":self._line_to_extract,"Columns to extract:":self._columns_to_extract}

class Integral_m(Block):
    """The Integral Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="INTEGRAL_m"
        self._initial_condition= data[0]
        self._with_re_initialization=data[1]
        self._with_saturation=data[2]
        self._upper_limit = data[3]
        self._lower_limit = data[4]


    def parameters(self):
        return {"Function Name:":self._funcname,"Initial Condition:":self._initial_condition,"With re-initialization:":self._with_re_initialization,"With Saturation:":self._with_saturation,"Upper Limit:":self._with_saturation,"Lower Limit:":self._lower_limit}


class Sci_func_block_m(Block):
    """The Sci_func_block_m Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="scifunc_block_m"
        self._input_port_sizes= data[0]
        self._output_port_sizes=data[1]
        self.__input_event_port_sizes=data[2]
        self._output_event_port_sizes=data[3]
        self._initial_continous_state=data[4]
        self.initial_discrete_state=data[5]
        self._system_parameter_vector=data[6]
        self._initial_firing_vector=data[7]
        self._is_block_always_active=data[8]


    def parameters(self):
        return {"Function Name:":self._funcname,"Input Port Sizes:":self._input_port_sizes,"Output Port Sizes:":self._output_port_sizes,"Output Event Port Sizes:":self._output_event_port_sizes,
                "Initial Continous state:":self._initial_continous_state,"Initial Discrete State":self.initial_discrete_state,"System Parameter Vector Data:":self._system_parameter_vector,
                "Initial Firing Vector:":self._initial_firing_vector,"Is block Always Active:":self._is_block_always_active}


class Matinv(Block):
    """The Matinv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATINV"
        self._datatype= data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}

class Mux(Block):
    """The Mux Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MUX"
        self._number_of_input_ports_or_vector_sizes= data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of Input Ports or Vector Sizes:":self._number_of_input_ports_or_vector_sizes}

class Gensqr(Block):
    """The Gen_sqr Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "GENSQR_f"
        self._amplitude = data[0]

    def parameters(self):
        return {"Function Name:": self._funcname, "Amplitude": self._amplitude}

class Sourcep(Block):
    """The Sourcep Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SourceP"
        self._pression= data[0]
        self._temperature=data[1]
        self._enthalpy=data[2]
        self._option=data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"Pression: P0 (Pa)":self._pression,"Temperature: T0(K)":self._temperature,"Enthalpie spécifique: H0(J/Kg)":self._enthalpy,"1:température fixée -2:enthalpie fixée: option temperature":self._option}

class Bacheb(Block):
    """The Sourcep Concrete Class which implements the Block interface"""
    def __init__(self, data):
            self._funcname = "BOUNCE"
            self._pression = data[0]
            self._section = data[1]
            self._ze1 = data[2]
            self._ze2 = data[3]
            self._zs1 = data[4]
            self._zs2 = data[5]
            self._fluid = data[6]
            self._temp = data[7]
            self._mass = data[8]


    def parameters(self):

        return {"Function Name:":self._funcname,"Pression dans le ciel de la bache : Patm (Pa):" :self._pression,"Section de la bache : A (m2)":self._section,"Altitude du piquage d entrée 1: ze1 (m):":self._ze1,"Altitude du piquage d entrée 2: ze2 (m):":self._ze2,"Altitude du piquage de sortie 1: zs1 (m):" : self._zs1,"Altitude du piquage de sortie 2: zs2 (m):" : self._zs2,"Altitude initiale du fluide : z0 (m):" : self._fluid,"Température initiale du fluide : T0 (K):" : self._temp,"Si 0, masse volumique imposée du fluide : p_rho (kg/m3):" : self._mass}


class PerteDp(Block):
    """The PerteDP Concrete Class which implements the IBlock interface"""


    def __init__(self, data):
        self._funcname = "PerteDP"
        self._long = data[0]
        self._diametre = data[1]
        self._coefficient = data[2]
        self._z1 = data[3]
        self._z2 = data[4]
        self._mass = data[5]

    def parameters(self):

        return {"Function Name:":self._funcname,"Longueur du tube : L (m):" :self._long,"Diamètre interne du tube : D (m):":self._diametre,"Coefficient de perte de charge-frottement(S.U) : lambda:":self._coefficient,"Altitude entrée tuyauterie : z1 (m):":self._z1,"Altitude sortie tuyauterie : z2 (m):" : self._z2,"Si 0, masse volumique imposée fu fluide : p_rho (kg/m3)" : self._mass}



class Satur(Block):
    """The Saturation Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATMUL"
        self._ulimit= data[0]
        self._llimit=data[1]
        self._zcross = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Upper Limit:":self._ulimit,"Lower Limit:":self._llimit,"zero crossing(0:no , 1:yes):":self._zcross}

class Clrf(Block):
    """The CLR_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="GAINBLK"
        self._numerator= data[0]
        self._denominator=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Numerator:":self._numerator,"Denominator:":self._denominator}


class Puits(Block):
    """The Puits Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SourceP"
        self._pression= data[0]
        self._temperature=data[1]
        self._enthalpy=data[2]
        self._option=data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"Pression de la source: P0 (Pa)":self._pression,"Temperature de la source: T0(K)":self._temperature,"Enthalpie spécifique de la source: H0(J/Kg)":self._enthalpy,"1:température fixée -2:enthalpie fixée: option temperature":self._option}



class Gainblkf(Block):
    """The Gainblk Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="GAINBLK_f"
        self._gain = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Gain:":self._gain}




class Cmscope(Block):
    """The CMScope Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CSCOPE"
        self._input_port_sizes=data[0]
        self._colorvector = data[1]
        self._output_window_number = data[2]
        self._output_window_position = data[3]
        self._output_window_sizes = data[4]
        self._ymin = data[5]
        self._ymax = data[6]
        self._refresh_period = data[7]
        self._buffer_size = data[8]
        self._accept_herited_events = data[9]
        self._scope_name = data[10]

    def parameters(self):
        return {"Function Name:":self._funcname,"Input port sizes:":self._input_port_sizes,"Color or mark vector:" :self._colorvector,"Output window number:":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Ymin:": self._ymin, "Ymax:": self._ymax,"Refresh period:" : self._refresh_period ,"Buffer Size:": self._buffer_size,"Accept herited events:": self._accept_herited_events,"Name of Scope:": self._scope_name}


class Voltagesensor(Block):
    """The Voltagesensor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="VoltageSensor"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Currentsensor(Block):
    """The Currentsensor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CurrentSensor"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Resist(Block):
    """The Resistor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Resistor"
        self._ohm=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"R(ohm):":self._ohm}



class Step_function(Block):
    """The Step function Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="STEP_FUNCTION"
        self._step_time=data[0]
        self._inital_value=data[1]
        self._final_value=data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Inital Value:":self._inital_value,"Final Value:":self._final_value}


class Ground(Block):
    """The Ground Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Ground"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Sum_f(Block):
    """The Ground Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SUM_f"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Postoneg_f(Block):
    """The Ground Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="POSTONEG_f"
        self._parameters="No parameters"

    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Negtopos_f(Block):
    """The Ground Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="NEGTOPOS_f"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Induct(Block):
    """The Inductor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Inductor"
        self._inductance = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"L(H):": self._inductance}


class SineV(Block):
    """The SineVoltage Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SourceP"
        self._amp= data[0]
        self._phase=data[1]
        self._freq=data[2]
        self._voltage=data[3]
        self._timeoff=data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"Amplitude(Volt):":self._amp,"phase(rad):":self._phase,"Frequency(Hz)":self._freq,"Voltageoffset(V)":self._voltage,"Timeoffset(s)":self._timeoff}

class SwitchB(Block):
    """The Switch Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Switch"
        self._resinon = data[0]
        self._resinoff = data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Resistance in On State(Ohm):": self._resinon,"Resistance in Off State(Ohm):": self._resinoff}
class CCSB(Block):
     """The Switch Concrete Class which implements the Block interface"""

     def __init__(self,data):
        self._funcname="CCS"
        self._parameters="No parameters"

     def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:": self._parameters}
