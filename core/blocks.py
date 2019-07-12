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
    """The BACHE Concrete Class which implements the Block interface"""
    def __init__(self, data):
            self._funcname = "BACHE"
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


'''
class Satur(Block):
    """The Saturation Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATMUL"
        self._ulimit= data[0]
        self._llimit=data[1]
        self._zcross = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Upper Limit:":self._ulimit,"Lower Limit:":self._llimit,"zero crossing(0:no , 1:yes):":self._zcross}
'''
class Clrf(Block):
    """The CLR_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLR_f"
        self._numerator= data[0]
        self._denominator=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Numerator:":self._numerator,"Denominator:":self._denominator}


class Puits(Block):
    """The Puits Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="PUITS"
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
        self._funcname = "CMSCOPE"
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


class Voltagesen(Block):
    """The Voltagesensor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="VoltageSensor"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Currentsen(Block):
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


class Groundb(Block):
    """The Ground Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Ground"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Sum_f(Block):
    """The SUM_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SUM_f"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Postoneg_f(Block):
    """The POSTONEG_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="POSTONEG_f"
        self._parameters="No parameters"

    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Negtopos_f(Block):
    """The NEGTOPOS_f Concrete Class which implements the Block interface"""

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
        self._funcname="SineVoltage"
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
        return {"Function Name:":self._funcname,"Resistance in On State(Ohm):": self._resinon,"Resistance in Off State(Ohm):":self._resinoff}
class CCSB(Block):
     """The Ccsb Concrete Class which implements the Block interface"""

     def __init__(self,data):
        self._funcname="CCS"
        self._parameters="No parameters"

     def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:": self._parameters}
class BigSom(Block):
     """The BigSom Concrete Class which implements the Block interface"""

     def __init__(self,data):
        self._funcname="BIGSOM_f"
        self._inp=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Input ports signs/gain": self._inp}



class Generic_block(Block):
    """The Generic_block Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "generic_block3"
        self._sim_func=data[0]
        self._functype = data[1]
        self._input_port_size = data[2]
        self._input_port_type = data[3]
        self._output_port_size= data[4]
        self._output_port_type = data[5]
        self._input_event_port_size = data[6]
        self._output_event_port_size = data[7]
        self._initial_continuous = data[8]
        self._initial_discrete = data[9]
        self._initial_object = data[10]
        self._real_parameter = data[11]
        self._integer_parameter = data[12]
        self._object_parameter = data[13]
        self._number_of_modes = data[14]
        self._nzero = data[15]
        self._initial_firing_vector = data[16]
        self._direct_feedthrough = data[17]
        self._time_dependence = data[18]



    def parameters(self):
        return {"Function Name:":self._funcname,"Simulation function:":self._sim_func,"Function type:" :self._functype,"Input ports sizes:":self._input_port_size,"Input ports type:":self._input_port_type,"Output port sizes:":self._output_port_size, "Output ports type:": self._output_port_type, "Input event ports sizes:": self._input_event_port_size,"Output events ports sizes:" : self._output_event_port_size ,"Initial continuous state:": self._initial_continuous,"Initial discrete state:": self._initial_discrete,"Initial object state:": self._initial_object,"Real parameters vector:": self._real_parameter,"Integer parameters vector:": self._integer_parameter,"Object parameters list:": self._object_parameter,"Number of zero_crossings:": self._nzero,"Initial firing vector:": self._initial_firing_vector,"Direct feedthrough:": self._direct_feedthrough,"Time dependence:": self._time_dependence}


class Cblock(Block):
    """The Cblock Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="cblock"
        self._input_ports_sizes= data[0]
        self._output_ports_sizes=data[1]
        self._system_parameters_vectors=data[2]
        self._functionname=data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"input ports sizes:":self._input_ports_sizes,"output port sizes:":self._output_ports_sizes,"System parameters vector:":self._system_parameters_vectors,"function name:":self._functionname,}

class Debug(Block):
        """The Debug Concrete Class which implements the IBlock interface"""

        def __init__(self,data):
            self._funcname = "DEBUG"
            self._instruction = data[0]

        def parameters(self):

            return {"Function Name:":self._funcname," Enter scilab instructions for debugging.Inputs are block and flag,output is block:": self._instruction}

class Expression(Block):
    """The EXPRESSION Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._funcname="EXPRESSION"
        self._numinput = data[0]
        self._sciexpr = data[1]
        self._zeroc = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"number of inputs:": self._numinput,"scilab expression:": self._sciexpr,"use zero-crossing:": self._zeroc}



class Cblock4(Block):
    """The Cblock4 Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "generic_block3"
        self._sim_func=data[0]
        self._is_implicit=data[1]
        self._functype = data[2]
        self._input_port_size = data[3]
        self._input_port_type = data[4]
        self._output_port_size= data[5]
        self._output_port_type = data[6]
        self._input_event_port_size = data[7]
        self._output_event_port_size = data[8]
        self._initial_continuous = data[9]
        self._initial_discrete = data[10]
        self._initial_object = data[11]
        self._real_parameter = data[12]
        self._integer_parameter = data[13]
        self._object_parameter = data[14]
        self._number_of_modes = data[15]
        self._nzero = data[16]
        self._initial_firing_vector = data[17]
        self._direct_feedthrough = data[18]
        self._time_dependence = data[19]



    def parameters(self):
        return {"Function Name:":self._funcname,"Is block implicit(y/n):":self._is_implicit,"Simulation function:":self._sim_func,"Function type:" :self._functype,"Input ports sizes:":self._input_port_size,"Input ports type:":self._input_port_type,"Output port sizes:":self._output_port_size, "Output ports type:": self._output_port_type, "Input event ports sizes:": self._input_event_port_size,"Output events ports sizes:" : self._output_event_port_size ,"Initial continuous state:": self._initial_continuous,"Initial discrete state:": self._initial_discrete,"Initial object state:": self._initial_object,"Real parameters vector:": self._real_parameter,"Integer parameters vector:": self._integer_parameter,"Object parameters list:": self._object_parameter,"Number of zero_crossings:": self._nzero,"Initial firing vector:": self._initial_firing_vector,"Direct feedthrough:": self._direct_feedthrough,"Time dependence:": self._time_dependence}


class Fortran(Block):
    """The Cblock Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="fortran_block"
        self._input_ports_sizes= data[0]
        self._output_ports_sizes=data[1]
        self._system_parameters_vectors=data[2]
        self._functionname=data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"input ports sizes:":self._input_ports_sizes,"output port sizes:":self._output_ports_sizes,"System parameters vector:":self._system_parameters_vectors,"function name:":self._functionname,}

class Cblock2(Block):
    """The Cblock2 Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CBLOCK"
        self._sim_func=data[0]
        self._is_implicit=data[1]
        self._input_port_size = data[2]
        self._output_port_size= data[3]
        self._input_event_port_size = data[4]
        self._output_event_port_size = data[5]
        self._initial_continuous = data[6]
        self._nzero = data[7]
        self._initial_discrete = data[8]
        self._real_parameter = data[9]
        self._integer_parameter = data[10]
        self._initial_firing_vector = data[11]
        self._direct_feedthrough = data[12]
        self._time_dependence = data[13]



    def parameters(self):
        return {"Function Name:":self._funcname,"simulation function:":self._sim_func,"Is block implicit(y/n):":self._is_implicit,"Input ports sizes:":self._input_port_size,"Output port sizes:":self._output_port_size,"Input event ports sizes:": self._input_event_port_size,"Output events ports sizes:" : self._output_event_port_size ,"Initial continuous state:": self._initial_continuous,"number of zero crossing surfaces":self._nzero,"Initial discrete state:": self._initial_discrete,"Real parameters vector:": self._real_parameter,"Integer parameters vector:": self._integer_parameter,"Initial firing vector:": self._initial_firing_vector,"Direct feedthrough:": self._direct_feedthrough,"Time dependence:": self._time_dependence}


class MBlock(Block):
     def __init__(self,data):
        self._funcname="MBLOCK"
        self._input_variables= data[0]
        self._input_variables_types=data[1]
        self._output_variables= data[2]
        self._output_variables_types=data[3]
        self._parameters_modellica=data[4]
        self._parameters_properties=data[5]
        self._function_name=data[6]

     def parameters(self):
        return {"Function Name:":self._funcname,"Input variables:":self._input_variables,"Input variables types:":self._input_variables_types,"Output variables:":self._output_variables,"Output variables types:":self._output_variables_types,"Parameters in Modelica:":self._parameters_modellica,"Parameters properties:":self._parameters_properties,"Function name:":self._function_name}



class Bplatform(Block):
    """The BPLATFORM Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="BPLATFORM"
        self._pen_length= data[0]
        self._cart_size=data[1]
        self._slope=data[2]
        self._xmin=data[3]
        self._xmax=data[4]
        self._ymin=data[5]
        self._ymax=data[6]

    def parameters(self):
        return {"Function Name:":self._funcname,"Pendulum Length:":self._pen_length,"cart size:":self._cart_size,"Slope":self._slope,"Xmin":self._xmin,"Xmax":self._xmax,"Ymin":self._ymin,"Ymax":self._ymax}


class FlowMeter(Block):
    """The FlowMeter Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Flowmeter"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Clkinv(Block):
    """The CLKINV_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLKINV_f"
        self._port_number=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Input port number:":self._port_number}



class Timef(Block):
    """The TIME_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="TIME_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Ramp(Block):
    """The EXPRESSION Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._funcname="RAMP"
        self._slope = data[0]
        self._start_time = data[1]
        self._initial = data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Slope:": self._slope,"Start time:": self._start_time,"Initial Time:": self._initial}


class Curvf(Block):
    """The Currentsensor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CURV_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Const_f(Block):
    """The Const_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CONST_f"
        self._constant_value = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Constant Value:": self._constant_value}


class Const(Block):
    """The Const Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CONST"
        self._constant_value = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Constant:": self._constant_value}


class Sawtooth(Block):
     """The Sawtooth Concrete Class which implements the Block interface"""

     def __init__(self,data):
        self._funcname="SAWTOOTH_f"
        self._parameters="No parameters"

     def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:": self._parameters}


class Pulse(Block):
     """The PULSE_SC Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="PULSE_SC"
         self._phase=data[0]
         self._pulse_width=data[1]
         self._period=data[2]
         self._amplitude=data[3]


     def parameters(self):
        return {"Function Name:":self._funcname,"Phase delay(secs):": self._phase,"Pulse Width(% of period):": self._pulse_width,"Period(secs):": self._period,"Amplitude:": self._amplitude}

class SigBuild(Block):
     """The SigBuild Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="SIGBUILD"
         self._spline_method=data[0]
         self._x=data[1]
         self._y=data[2]
         self._periodic_signal=data[3]
         self._launch_graphic_window=data[4]


     def parameters(self):
        return {"Function Name:":self._funcname,"Spline Method(0..7):": self._spline_method,"x:": self._x,"y:": self._y,"Periodic signal(y/n)?:": self._periodic_signal,"Launch graphic window(y/n)?:": self._launch_graphic_window}

class ModCount(Block):
     """The ModCount Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="Modulo_Count"
         self._initstate=data[0]
         self._ulimit=data[1]


     def parameters(self):
        return {"Function Name:":self._funcname,"Initial State(zero or positive number):": self._initstate,"Upper Limit (positive number):": self._ulimit}

class Count(Block):
     """The Counter Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="Counter"
         self._min=data[0]
         self._max=data[1]
         self._rule=data[2]


     def parameters(self):
        return {"Function Name:":self._funcname,"Minimum:": self._min,"Maximum:": self._max,"Rule (1:Increment, 2:Decrement):": self._rule}


class TkScale(Block):
     """The TKSCALE Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="TKSCALE"
         self._min=data[0]
         self._max=data[1]
         self._normal=data[2]


     def parameters(self):
        return {"Function Name:":self._funcname,"Min value:": self._min,"Max value:": self._max,"Normalisation:": self._normal}


class FromWsb(Block):
     """The FROMWSB Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="FROMWSB"
         self._variable=data[0]
         self._interpolation=data[1]
         self._enable=data[2]
         self._output=data[3]


     def parameters(self):
        return {"Function Name:":self._funcname,"Variable name:": self._variable,"Interpolation method:": self._interpolation,"Enable zero crossing(0:No, 1:Yes)?:": self._enable,"Output at end(0:Zero, 1:Hold, 2:Repeat)":self._output}




class Readau_f(Block):
     """"The Readau_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="READAU_f"
         self._input_file_name=data[0]
         self._buffer_size=data[1]
         self._swap_mode=data[2]


     def parameters(self):
         return {"Function Name:":self._funcname,"Input file name:": self._input_file_name,"Buffer size:": self._buffer_size,"Swap mode 0/1:": self._swap_mode}


class Readc(Block):
     """The READC_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="READC_f"
         self._time_record_selection=data[0]
         self._outputs_record_selection=data[1]
         self._input_file_name=data[2]
         self._input_format=data[3]
         self._record_size=data[4]
         self._buffer_size=data[4]
         self._initial_record_index=data[4]
         self._swap_mode=data[4]


     def parameters(self):
        return {"Function Name:":self._funcname,"Time record selection:": self._time_record_selection,"Outputs record selection:": self._outputs_record_selection,"Input file name:": self._input_file_name,"Input Format:": self._input_format,"Record size:": self._record_size,"Buffer size:": self._buffer_size,"Initial Record Index:": self._initial_record_index,"Swap Mode(0:No, 1:Yes):": self._swap_mode}
class Rfile(Block):
     """"The RFILE_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="RFILE_f"
         self._time_record_selection=data[0]
         self._output_record_selection=data[1]
         self._input_file_name=data[2]
         self._input_format=data[3]
         self._buffer_size=data[4]


     def parameters(self):
         return {"Function Name:":self._funcname,"Time record selection:": self._time_record_selection,"Outputs record selection:": self._output_record_selection,"Input file name:": self._input_file_name,"Input format:": self._input_format,"Buffer size:":self._buffer_size}


class Inimpl(Block):
     """The Inimpl Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="INIMPL_f"
         self._port_num=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Port Number:": self._port_num}
class In_f(Block):
     """The IN_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="IN_f"
         self._port_num=data[0]
         self._output_size=data[1]
         self._output_type=data[2]

     def parameters(self):
        return {"Function Name:":self._funcname,"Port Number:": self._port_num,"Output port size:": self._output_size,"Output port type:": self._output_type}

class Constraint_c(Block):
     """The Constraint_c Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="CONSTRAINT_c"
         self._initial_guess=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Initial Guess Value:": self._initial_guess}


class Diff_f(Block):
     """The DIFF_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="DIFF_f"
         self._initial_state=data[0]
         self._initial_derivative=data[1]
     def parameters(self):
        return {"Function Name:":self._funcname,"Initial State:": self._initial_state,"Initial Derivative:": self._initial_derivative}


class GenF(Block):
     """The GENERAL_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="GENERAL_f"
         self._input_size=data[0]
         self._number_of_event_output=data[1]
     def parameters(self):
        return {"Function Name:":self._funcname,"Input Size:": self._input_size,"Number of Event Output:": self._number_of_event_output}

class Zcrossf(Block):
     """The ZCROSS_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="ZCROSS_f"
         self._input_size=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Input Size:": self._input_size}

class Affichm(Block):
     """The AFFICH_m Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="AFFICH_m"
         self._input_size=data[0]
         self._font_number=data[1]
         self._font_size=data[2]
         self._color=data[3]
         self._total_number_digits=data[4]
         self._rational_part=data[5]
         self._block_inherits=data[6]

     def parameters(self):
        return {"Function Name:":self._funcname,"Input Size:": self._input_size,"Font Number:": self._font_number,"Font Size:": self._font_size,"Color:": self._color,"Number of rational part digits:": self._rational_part,"Block inherits(1) or not(0):": self._block_inherits}

class Barxy(Block):
     """The BARXY Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="BARXY"
         self._xmin=data[0]
         self._xmax=data[1]
         self._ymin=data[2]
         self._ymax=data[3]
         self._seg=data[4]

     def parameters(self):
        return {"Function Name:":self._funcname,"Xmin:": self._xmin,"Xmax:": self._xmax,"Ymin:": self._ymin,"Ymax:": self._ymax,"Seg Thickness":self._seg}

class Cscopxy3d(Block):
    """The CSCOPXY3D Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CSCOPXY3D"
        self._curves = data[0]
        self._colorvector = data[1]
        self._line_mark = data[2]
        self._output_window_number = data[3]
        self._output_window_position = data[4]
        self._output_window_sizes = data[5]
        self._xmin_xmax = data[6]
        self._ymin_ymax = data[7]
        self._zmin_zmax = data[8]
        self._alpha_theta = data[9]
        self._buffer_size = data[10]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of Curves:" :self._curves,"Color(>0) or mark(<0) :" :self._colorvector,"Line or Mark Size:" :self._line_mark,"Output window number(-1 for automatic):":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Xmin and Xmax:": self._xmin_xmax, "Ymin and Ymax:": self._ymin_ymax,"Zmin and Zmax:" : self._zmin_zmax ,"Alpha and Theta:": self._alpha_theta,"Buffer size:": self._buffer_size}

class Writeauf(Block):
     """The WRITEAU_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="WRITEAU_f"
         self._buffer_size=data[0]
         self._swap_mode=data[1]
     def parameters(self):
        return {"Function Name:":self._funcname,"Buffer Size:": self._buffer_size,"Swap Mode(0:No,1:Yes):": self._swap_mode}

class Canimxy(Block):
    """The CANIMXY Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CANIMXY"
        self._curves = data[0]
        self._colorvector = data[1]
        self._line_mark = data[2]
        self._output_window_number = data[3]
        self._output_window_position = data[4]
        self._output_window_sizes = data[5]
        self._xmin = data[6]
        self._xmax = data[7]
        self._ymin = data[8]
        self._ymax = data[9]
        self._buffer_size = data[10]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of Curves:" :self._curves,"Color(>0) or mark(<0) :" :self._colorvector,"Line or Mark Size:" :self._line_mark,"Output window number(-1 for automatic):":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Xmin:": self._xmin, "Xmax:": self._xmax,"Ymin:" : self._ymin ,"Ymax:": self._ymax,"Buffer size:": self._buffer_size}

class Cmat3d(Block):
     """The CMAT3D Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="CMAT3D"
         self._bvectorx=data[0]
         self._bvectory=data[1]
         self._color_map=data[2]
         self._zmin=data[3]
         self._zmax=data[4]

     def parameters(self):
        return {"Function Name:":self._funcname,"Bounds Vector X:": self._bvectorx,"Bounds Vector Y:": self._bvectory,"ColorMap:": self._color_map,"Zmin:": self._zmin,"Zmax:": self._zmax}

class Writecf(Block):
     """The WRITEC_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="WRITEC_f"
         self._input_size=data[0]
         self._output_file_name=data[1]
         self._output_format=data[2]
         self._buffer_size=data[3]
         self._swap_mode=data[4]

     def parameters(self):
        return {"Function Name:":self._funcname,"Input Size:": self._input_size,"Output File Name:": self._output_file_name,"Output Format:": self._output_format,"Buffer Size:": self._buffer_size,"Swap Mode(0:No, 1:Yes):": self._swap_mode}

class Canimxy3d(Block):
    """The CANIMXY3D Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CANIMXY3D"
        self._curves = data[0]
        self._colorvector = data[1]
        self._line_mark = data[2]
        self._output_window_number = data[3]
        self._output_window_position = data[4]
        self._output_window_sizes = data[5]
        self._xmin_xmax = data[6]
        self._ymin_ymax = data[7]
        self._zmin_zmax = data[8]
        self._alpha_theta = data[9]
        self._buffer_size = data[10]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of Curves:" :self._curves,"Color(>0) or mark(<0) :" :self._colorvector,"Line or Mark Size:" :self._line_mark,"Output window number(-1 for automatic):":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Xmin and Xmax:": self._xmin_xmax, "Ymin and Ymax:": self._ymin_ymax,"Zmin and Zmax:" : self._zmin_zmax ,"Alpha and Theta:": self._alpha_theta,"Buffer size:": self._buffer_size}

class Cfscope(Block):
    """The CFSCOPE Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CFSCOPE"
        self._colorvector = data[0]
        self._output_window_number = data[1]
        self._output_window_position = data[2]
        self._output_window_sizes = data[3]
        self._ymin = data[4]
        self._ymax = data[5]
        self._refresh_period = data[6]
        self._buffer_size = data[7]
        self._links_view = data[8]

    def parameters(self):
        return {"Function Name:":self._funcname,"Color or mark vector:" :self._colorvector,"Output window number:":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Ymin:": self._ymin, "Ymax:": self._ymax,"Refresh period:" : self._refresh_period ,"Buffer Size:": self._buffer_size,"Links to view:": self._links_view}



class Cscopxy(Block):
    """The CSCOPXY Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "CSCOPXY"
        self._curves = data[0]
        self._colorvector = data[1]
        self._line_mark = data[2]
        self._output_window_number = data[3]
        self._output_window_position = data[4]
        self._output_window_sizes = data[5]
        self._xmin = data[6]
        self._xmax = data[7]
        self._ymin = data[8]
        self._ymax = data[9]
        self._buffer_size = data[10]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of Curves:" :self._curves,"Color(>0) or mark(<0) :" :self._colorvector,"Line or Mark Size:" :self._line_mark,"Output window number(-1 for automatic):":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Xmin:": self._xmin, "Xmax:": self._xmax,"Ymin:" : self._ymin ,"Ymax:": self._ymax,"Buffer size:": self._buffer_size}
class Cmatview(Block):
     """The CMATVIEW Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="CMATVIEW"
         self._color_map=data[0]
         self._minimum_level_range=data[1]
         self._maximum_level_range=data[2]

     def parameters(self):
        return {"Function Name:":self._funcname,"ColorMap:": self._color_map,"Minimum level range:": self._minimum_level_range,"Maximum level range:": self._maximum_level_range}

class Trashf(Block):
    """The TRASH_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="TRASH_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class TOWS_c(Block):
     """The TOWS_c Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="TOWS_c"
         self._size_buffer=data[0]
         self._scilab_variable_name=data[1]
         self._inherit=data[2]

     def parameters(self):
        return {"Function Name:":self._funcname,"Size of buffer:": self._size_buffer,"Scilab variable name:": self._scilab_variable_name,"Inherit(no:0, yes:1):": self._inherit}

class Outimpf(Block):
     """The OUTIMPL_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="OUTIMPL_f"
         self._port_num=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Port Number:": self._port_num,"Output port size:": self._output_size,"Output port type:": self._output_type}

class Outf(Block):
     """The OUT_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="OUT_f"
         self._port_num=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Port Number:": self._port_num,"Output port size:": self._output_size,"Output port type:": self._output_type}

class Demux(Block):
     """The DEMUX Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="DEMUX"
         self._number_output=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of output ports or vector of sizes:": self._number_output}

class Demuxf(Block):
     """The DEMUX_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="DEMUX_f"
         self._number_output=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of output ports or vector of sizes:": self._number_output}


class Extractor(Block):
     """The EXTRACTOR Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="EXTRACTOR"
         self._number_indices=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Indices to extract:": self._number_indices}



class Self_switch(Block):
    """The SELF_SWITCH Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SELF_SWITCH"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Iselectm(Block):
     """The ISELECT_m Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="ISELECT_m"
         self._datatype=data[0]
         self._number_outputs=data[1]
         self._initial_connected_output=data[2]

     def parameters(self):
        return {"Function Name:":self._funcname,"Datatype(1 = real double 2=Complex 3=int32..):": self._datatype,"number of outputs:": self._number_outputs,"initial connected output:": self._initial_connected_output}

class Scalar2Vec(Block):
     """The SCALAR2VECTOR Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="SCALAR2VECTOR"
         self._size_output=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Size of output(-1: if don't know):": self._size_output}

class Muxf(Block):
     """The MUX_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="MUX_f"
         self._size_input=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of output ports or vector of sizes:": self._size_input}

class Mswitch(Block):
     """The M_SWITCH Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="M_SWITCH"
         self._num_inputs=data[0]
         self._zero_base_indexing=data[1]
         self._rounding_rule=data[2]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of inputs:": self._num_inputs,"zero base indexing(0),otherwise 1:": self._zero_base_indexing,"rounding rule:int(0),round(1),ceil(2),floor(3):": self._rounding_rule}

class From(Block):
     """The FROM Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="FROM"
         self._tag=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Tag:": self._tag}
class FromMo(Block):
     """The FROMMO Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="FROMMO"
         self._tag=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Tag:": self._tag}

class Nrmsomf(Block):
     """The NRMSOM_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="NRMSOM_f"
         self._num_inputs=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of inputs:": self._num_inputs}

class Relayf(Block):
     """The RELAY_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="RELAY_f"
         self._num_inputs=data[0]
         self._initial_connected_input=data[1]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of inputs:": self._num_inputs,"initial connected input:": self._initial_connected_input}
class Gototagvis(Block):
     """The GotoTagVisibility Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="GotoTagVisibility"
         self._gototag=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"GotoTag:": self._gototag}

class GototagvisMO(Block):
     """The GotoTagVisibilityMO Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="GotoTagVisibilityMO"
         self._gototag=data[0]

     def parameters(self):
        return {"Function Name:":self._funcname,"GotoTag:": self._gototag}

class Selectm(Block):
     """The SELECT_m Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="SELECT_m"
         self._datatype=data[0]
         self._num_inputs=data[1]
         self._initial_connected_input=data[2]

     def parameters(self):
        return {"Function Name:":self._funcname,"Datatype (1=real Double  2=Complex 3=int32..)":self._datatype,"Number of inputs:": self._num_inputs,"initial connected input:": self._initial_connected_input}
class Switchf(Block):
     """The SWITCH_f Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="SWITCH_f"
         self._num_inputs=data[0]
         self._connected_input=data[1]

     def parameters(self):
        return {"Function Name:":self._funcname,"Number of inputs:": self._num_inputs,"connected input:": self._connected_input}

class Switch2m(Block):
     """The SWITCH2_m Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="SWITCH2_m"
         self._datatype=data[0]
         self.pass_first_input=data[1]
         self._threshold=data[2]
         self._usez=data[3]

     def parameters(self):
        return {"Function Name:":self._funcname,"Datatype (1=real Double  2=Complex 3=int32..)":self._datatype,"Pass first input if: u2 ≥ a:": self.pass_first_input,"Threshold a": self._threshold,"Use zero crossing: yes:":self._usez}

class CvsB(Block):
    """The CVS Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CVS"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Capacit(Block):
    """The Capacitor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Capacitor"
        self._cap = data[0]
        self._initial = data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"C(F):": self._cap, "Initial Voltage": self._initial}

class ConstVolt(Block):
    """The ConstantVoltage Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ConstantVoltage"
        self._volt = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Voltage(V)": self._volt}

class Diodeb(Block):
     """The Diode Concrete Class which implements the Block interface"""

     def __init__(self,data):
         self._funcname="Diode"
         self._sat_current=data[0]
         self._voltage_equi=data[1]
         self._max_exp=data[2]
         self._R_ohm=data[3]

     def parameters(self):
        return {"Function Name:":self._funcname,"Saturation current(A":self._sat_current,"Voltage equivalent to temperature(Volt):": self._voltage_equi,"Max exponent for linear continuation": self._max_exp,"R(ohm):":self._R_ohm}

class Opamp(Block):
    """The Opamp Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="OpAmp"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class IdealTrans(Block):
    """The IdealTransformer Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="IdealTransformer"
        self._turns = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Turns Ratio(N)": self._turns}

class Gyrat(Block):
    """The Gyrator Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Gyrator"
        self._g1 = data[0]
        self._g2 = data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"G1": self._g1,"G2": self._g2}

class PotSensor(Block):
    """The PotentialSensor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="PotentialSensor"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class VSource(Block):
    """The VsourceAC Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="VsourceAC"
        self._amp = data[0]
        self._freq = data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Amplitude(Volt)": self._amp,"Frequency(Hz)": self._freq}

class VVSource(Block):
    """The VVsourceAC Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="VVsourceAC"
        self._freq = data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Frequency(Hz)": self._freq}

class VarResist(Block):
    """The VariableResistor Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="VariableResistor"
        self._parameters="No parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Nmos(Block):
    """The NMOS Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "NMOS"
        self._width = data[0]
        self._length= data[1]
        self._trans_par = data[2]
        self._zero_bias= data[3]
        self._bulk_threshold = data[4]
        self._reduction = data[5]
        self._narrowing = data[6]
        self._shortenin = data[7]
        self._drain = data[8]


    def parameters(self):
        return {"Function Name:":self._funcname,"Width [m]:" :self._width,"Length [m] :" :self._length,"Transconductance parameter [A/(V*V)]:" :self._trans_par,"Zero bias threshold voltage [V]:":self._zero_bias,"Bulk threshold parameter:":self._bulk_threshold,"Reduction of pinch-off region:":self._reduction, "Narrowing of channel[m]:": self._narrowing, "Shortening of channel[m]:": self._shortenin,"Drain-Source-Resistance[Ohm]:" : self._drain}

class Pmos(Block):
    """The PMOS Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "PMOS"
        self._width = data[0]
        self._length= data[1]
        self._trans_par = data[2]
        self._zero_bias= data[3]
        self._bulk_threshold = data[4]
        self._reduction = data[5]
        self._narrowing = data[6]
        self._shortenin = data[7]
        self._drain = data[8]


    def parameters(self):
        return {"Function Name:":self._funcname,"Width [m]:" :self._width,"Length [m] :" :self._length,"Transconductance parameter [A/(V*V)]:" :self._trans_par,"Zero bias threshold voltage [V]:":self._zero_bias,"Bulk threshold parameter:":self._bulk_threshold,"Reduction of pinch-off region:":self._reduction, "Narrowing of channel[m]:": self._narrowing, "Shortening of channel[m]:": self._shortenin,"Drain-Source-Resistance[Ohm]:" : self._drain}

class Pnpb(Block):
    """The PNP Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "PNP"
        self._forward = data[0]
        self._reverse= data[1]
        self._transport = data[2]
        self._early_voltage= data[3]
        self._ideal_forward = data[4]
        self._ideal_reverse = data[5]
        self._collector = data[6]
        self._cje = data[7]
        self._cjc = data[8]
        self._phie = data[9]
        self._me= data[10]
        self._phic = data[11]
        self._mc= data[12]
        self._gbc = data[13]
        self._gbe = data[14]
        self._vt = data[15]
        self._emin = data[16]


    def parameters(self):
        return {"Function Name:":self._funcname,"Forward beta:" :self._forward,"Reverse beta:" :self._reverse,"Transport saturation current [A]:" :self._transport,"Early voltage (inverse), 1/Volt [1/V]:":self._early_voltage,"Ideal forward transit time [s]:":self._ideal_forward,"Ideal reverse transit time [s]:":self._ideal_reverse, "Collector-substrat(ground) cap. [F]:": self._collector, "Base-emitter zero bias depletion cap. [F]:": self._cje,"Base-coll. zero bias depletion cap. [F]:" : self._cjc,"Base-emitter diffusion voltage [V]":self._phie,"Base-emitter gradation exponent":self._me,"Base-collector diffusion voltage [V]":self._phic,"Base-collector gradation exponent":self._mc,"Base-collector conductance [S]":self._gbc,"Base-emitter conductance [S]":self._gbe,"Voltage equivalent of temperature [V]":self._vt,"if x > EMinMac, the exp(x) function is linearized":self._emin}

class Npnb(Block):
    """The NPN Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "NPN"
        self._forward = data[0]
        self._reverse= data[1]
        self._transport = data[2]
        self._early_voltage= data[3]
        self._ideal_forward = data[4]
        self._ideal_reverse = data[5]
        self._collector = data[6]
        self._cje = data[7]
        self._cjc = data[8]
        self._phie = data[9]
        self._me= data[10]
        self._phic = data[11]
        self._mc= data[12]
        self._gbc = data[13]
        self._gbe = data[14]
        self._vt = data[15]
        self._emin = data[16]


    def parameters(self):
        return {"Function Name:":self._funcname,"Forward beta:" :self._forward,"Reverse beta:" :self._reverse,"Transport saturation current [A]:" :self._transport,"Early voltage (inverse), 1/Volt [1/V]:":self._early_voltage,"Ideal forward transit time [s]:":self._ideal_forward,"Ideal reverse transit time [s]:":self._ideal_reverse, "Collector-substrat(ground) cap. [F]:": self._collector, "Base-emitter zero bias depletion cap. [F]:": self._cje,"Base-coll. zero bias depletion cap. [F]:" : self._cjc,"Base-emitter diffusion voltage [V]":self._phie,"Base-emitter gradation exponent":self._me,"Base-collector diffusion voltage [V]":self._phic,"Base-collector gradation exponent":self._mc,"Base-collector conductance [S]":self._gbc,"Base-emitter conductance [S]":self._gbe,"Voltage equivalent of temperature [V]":self._vt,"if x > EMinMac, the exp(x) function is linearized":self._emin}



class Backlash(Block):
    """The Backlash Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="BACKLASH"
        self._initial_output = data[0]
        self._gap = data[1]
        self._use_zero_crossing=data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Inital Output:": self._initial_output,"Gap:":self._gap,"Use Zero crossing:":self._use_zero_crossing}


class Deadband(Block):
    """The Deadband Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="DEADBAND"
        self._end_of_dead_band = data[0]
        self._start_of_dead_band= data[1]
        self._use_zero_crossing=data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"End of Dead Band": self._end_of_dead_band,"Start of dead band:":self._start_of_dead_band,"Use Zero crossing:":self._use_zero_crossing}


class Delayv_f(Block):
    """The Delayv_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="DELAYV_f"
        self._number_of_inputs = data[0]
        self._register_initial_condition= data[1]
        self._max_delay=data[2]

    def parameters(self):
        return {"Function Name:":self._funcname,"Number of input": self._number_of_inputs,"Register Initial Condition":self._register_initial_condition,"Max Delay":self._max_delay}


class Hystheresis(Block):
    """The Hystheresis Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="HYSTHERESIS"
        self._switch_on_at = data[0]
        self._switch_off_at= data[1]
        self._output_when_on=data[2]
        self._output_when_off=data[3]
        self._use_zero_crossing = data[4]


    def parameters(self):
        return {"Function Name:":self._funcname,"Switch on at:": self._switch_on_at,"Switch off at:":self._switch_off_at,"Output when on:":self._output_when_on,"Output when off:":self._output_when_off,"Use Zero crossing:":self._use_zero_crossing}


class Ratelimiter(Block):
    """The Ratelimiter Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "RATELIMITER"
        self._max_slope= data[0]
        self._min_slope=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Max slope:": self._max_slope,"Min slope:":self._min_slope}

class Quant_f(Block):
    """The Quant_f Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "QUANT_f"
        self._step= data[0]
        self._quantization=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Step": self._step,"Quantization:":self._quantization}

class Saturation(Block):
    """The Saturation Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "SATURATION"
        self._upper_limit= data[0]
        self._lower_limit=data[1]
        self._use_zero_crossing = data[2]


    def parameters(self):
        return {"Function Name:": self._funcname, "Upper Limit": self._upper_limit,"Lower Limit:":self._lower_limit,"Use Zero crossing:":self._use_zero_crossing}


class Automat(Block):
    """The Automat Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "AUTOMAT"
        self._number_modes= data[0]
        self._inital_mode=data[1]
        self._number_of_continous_time_state=data[2]
        self._properties_of_continous_time_state_in_each_mode=data[3]
        self._jump_from_mode_1=data[4]
        self._jump_from_mode_2=data[5]

    def parameters(self):
        return {"Function Name:": self._funcname, "Number modes": self._number_modes,"Initial mode:":self._inital_mode,
                "Number of continous time state:":self._number_of_continous_time_state,"Properties of continous time state in each mode:":self._properties_of_continous_time_state_in_each_mode,
                "Jump from mode 1:":self._jump_from_mode_1,"Jump from mode 2:":self._jump_from_mode_2}

class Dollar_f(Block):
    """The Dollar_f Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DOLLAR_f"
        self._initial_condition= data[0]
        self._inherit=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Initial Condition:": self._initial_condition,"Inherit:":self._inherit}

class Dollar(Block):
    """The Dollar Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DOLLAR"
        self._initial_condition= data[0]
        self._inherit=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Initial Condition:": self._initial_condition,"Inherit:":self._inherit}

class Dollar_m(Block):
    """The Dollar_m Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DOLLAR_m"
        self._initial_condition= data[0]
        self._inherit=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Initial Condition:": self._initial_condition,"Inherit:":self._inherit}

class Delay_f(Block):
    """The Delay_f Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DELAY_f"
        self._discretization_time_step= data[0]
        self._register_initial_step=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Discretization time step:": self._discretization_time_step,"Register Initial step:":self._register_initial_step}



class Dlss(Block):
    """The Dlss Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DLSS"
        self._A_matrix= data[0]
        self._B_matrix=data[1]
        self._C_matrix = data[2]
        self._D_matrix = data[3]
        self._inital_state=data[4]

    def parameters(self):
        return {"Function Name:": self._funcname, "A matrix:": self._A_matrix,"B Matrix:":self._B_matrix,
                "C Matrix:":self._C_matrix,"D Matrix:":self._D_matrix}

class Tclss(Block):
    """The Tclss Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "TCLSS"
        self._A_matrix= data[0]
        self._B_matrix=data[1]
        self._C_matrix = data[2]
        self._D_matrix = data[3]
        self._inital_state=data[4]

    def parameters(self):
        return {"Function Name:": self._funcname, "A matrix:": self._A_matrix,"B Matrix:":self._B_matrix,
                "C Matrix:":self._C_matrix,"D Matrix:":self._D_matrix}

class Dlr(Block):
    """The Dlr Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DLR"
        self._numerator= data[0]
        self._denominator=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Numerator:": self._numerator,"Denominator:":self._denominator}

class Register(Block):
    """The Register Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "REGISTER"
        self._register_initial_condition= data[0]
        self._datatype=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "Register:": self._register_initial_condition,"Datatype:":self._datatype}

class Samphold_m(Block):
    """The Samphold_m Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "SAMPHOLD_m"

        self._datatype=data[0]

    def parameters(self):
        return {"Function Name:": self._funcname,"Datatype:":self._datatype}

class Dlradapt_f(Block):
    """The Dlradapt_f Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "DLRADAPT_f"


        self._vector_of_p_mesh_point=data[0]
        self._numerator_roots=data[1]
        self._denominator_roots=data[2]
        self._vector_of_gain_at_mesh_point = data[3]
        self._past_input=data[4]
        self._past_output=data[5]

    def parameters(self):
        return {"Function Name:": self._funcname,"Vector of P mesh point:":self._vector_of_p_mesh_point,
                "Numerator roots:":self._numerator_roots,"Denominator roots:":self._denominator_roots,
                "Vector of gain at mesh point:":self._vector_of_gain_at_mesh_point,"Past input:":self._past_input,
                "Past output:":self._past_output}


class Interp(Block):
    """The Interp Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "INTRPLBLK_f"
        self._x_coord= data[0]
        self._y_coord=data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "X coord:": self._x_coord,"Y ccord:":self._y_coord}


class Interp2(Block):
    """The Interp2 Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "INTRP2BLK_f"
        self._x_coord= data[0]
        self._y_coord=data[1]
        self._z_coord=data[2]

    def parameters(self):
        return {"Function Name:": self._funcname, "X coord:": self._x_coord,"Y ccord:":self._y_coord,"Z coord:":self._z_coord}

class Lookup_f(Block):
    """The Lookup Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="LOOKUP_f"
        self._parameters="Graphic Representation"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Andlog_f(Block):
    """The Andlog_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ANDLOG_f"
        self._parameters="No Parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Evtvardly(Block):
    """The EVTVARDLY Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EVTVARDLY"
        self._initial_event_firing_time=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Initial event firing time:":self._initial_event_firing_time}

class Evtgen_f(Block):
    """The Evtgen_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EVTGEN_f"
        self._event_time=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Event time:":self._event_time
                }

class Virtualclock0(Block):
    """VirtualCLK0 Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="VirtualCLK0"
        self._parameters="No Parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Andblk(Block):
    """The ANDBLK Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ANDBLK"
        self._parameters="No Parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Extract_activation(Block):
    """The Extract_Activation Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="Extract_Activation"
        self._parameters="No Parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Clkoutv_f(Block):
    """The Clkoutv_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLKOUTV_f"
        self._parameters="No Parameters"



    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Clkgoto(Block):
    """The Clkgoto Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLKGOTO"
        self._tag=data[0]
        self._tag_visiblity=data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Tag:":self._tag,"Tag Visiblity:":self._tag_visiblity}


class Mfreq(Block):
    """The Mfreq Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="M_freq"
        self._sample_time=data[0]
        self._offset=data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Sample time:":self._sample_time,"Offset:":self._offset}


class End(Block):
    """The End Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="END_c"
        self._final_simulation_time=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Final Simulation time:":self._final_simulation_time}


class Endblk(Block):
    """The Endblk Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ENDBLK"
        self._final_simulation_time=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Final Simulation time:":self._final_simulation_time}


class freqdiv(Block):
    """The freqdiv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="freq_div"
        self._phase=data[0]
        self._division_factor=data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Phase:":self._phase,"Division factor:":self._division_factor}


class Mclock_f(Block):
    """The Mclock_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MCLOCK_f"
        self._basic_period=data[0]
        self._multiply_by=data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Basic Period:":self._basic_period,"Multiply By:":self._multiply_by}


class Halt_f(Block):
    """The Halt_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="HALT_f"
        self._state_on_halt=data[0]




    def parameters(self):
        return {"Function Name:":self._funcname,"State on halt:":self._state_on_halt}


class Mfclck_f(Block):
    """The Mfclck_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MFCLCK_f"
        self._basic_period=data[0]
        self._multiply_by=data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Basic Period:":self._basic_period,"Multiply By:":self._multiply_by}


class Eselect_f(Block):
    """The Eselect_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ESELECT_f"
        self._number_of_output_event_port=data[0]
        self._inherit=data[1]
        self._use_zero_crossing = data[2]



    def parameters(self):
        return {"Function Name:":self._funcname,"Number of output event port:":self._number_of_output_event_port,"Inherit:":self._inherit,"Use Zero Crossing:":self._use_zero_crossing}



class Clkfrom (Block):
    """The Clkfrom Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLKFROM"
        self._tag=data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Tag:":self._tag}

'''
class Clkoutv_f(Block):
    """The Clkoutv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLKOUTV_f"
        self._port_number=data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Port number:":self._port_number}
'''

class Clkgototagvisiblity(Block):
    """The ClkGotoTagVisiblity Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CLKGotoTagVisibility"
        self._go_to_tag=data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Go to tag:":self._go_to_tag}


class Edge_trigger(Block):
    """The EDGE_TRIGGER Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EDGE_TRIGGER"
        self._edge_trigger=data[0]

    def parameters(self):
        return {"Function Name:":self._funcname,"Edge Trigger:":self._edge_trigger}

class Evtdly_c(Block):
    """The Evtdly_c Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EVTDLY_c"
        self._delay=data[0]
        self._date_of_initial_output_event=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Delay:":self._delay,"Date of initial output event:":self._date_of_initial_output_event}

class Sinblk_f(Block):
    """The Sinblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SINBLK_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Cosblk_f(Block):
    """The Cosblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="COSBLK_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Prod_f(Block):
    """The Prod_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="PROD_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Max_f(Block):
    """The Maxblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MAX_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Min_f(Block):
    """The Min_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MIN_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Tanblk_f(Block):
    """The Tanblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="TANBLK_f"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

'''
class Gainblk(Block):
    """The GainblkConcrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="GAINBLK"
        self._gain = data[0]
        self._do_on_overflow=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Gain:":self._gain,"Do on Overflow:":self._do_on_overflow}
'''
class Gain_f(Block):
    """The Gain_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="GAIN_f"
        self._gain = data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Gain:":self._gain}

class Product(Block):
    """The Product Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="PRODUCT"
        self._number_of_input_or_sign_vector= data[0]
        self._error_on_dividing_by_zero=data[1]

    def parameters(self):
        return {"Function Name:":self._funcname,"Number of input or sign vector:":self._number_of_input_or_sign_vector,"Error on Dividing by Zero":self._error_on_dividing_by_zero}


class Signum(Block):
    """The Signum Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SIGNUM"
        self._use_zero_crossing = data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Use Zero Crossing":self._use_zero_crossing}

class Absvalue(Block):
    """The Absvalue Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="ABS_VALUE"
        self._use_zero_crossing = data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Use Zero Crossing":self._use_zero_crossing}

class Invblk(Block):
    """The Invblk Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="INVBLK"
        self._error_on_dividing_by_zero=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Error on Dividing by Zero:":self._error_on_dividing_by_zero}

'''
class Tanblk_f(Block):
    """The Tanblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="TANBLK_f"
        self._function=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Function:":self._function}
'''

class Logblk_f(Block):
    """The Logblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="LOGBLK_f"
        self._basic=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Basic(>1):":self._basic}

class Maxmin(Block):
    """The Maxmin Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MAXMIN"
        self._min_or_max=data[0]
        self._number_of_input_vector=data[1]
        self._use_zero_crossing = data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of Input Vector:":self._number_of_input_vector,"Use Zero Crossing":self._use_zero_crossing}


class Matmagphi(Block):
    """The Matmagphi Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATMAGPHI"
        self._decomposition=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Decomposition:":self._decomposition}

class Matzreim(Block):
    """The Matzreim Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATZREIM"
        self._decomposition=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Decomposition:":self._decomposition}

class Sqrt(Block):
    """The Sqrt Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SQRT"
        self._datatype=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}

class Relationalop(Block):
    """The Relationalop Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="RELATIONALOP"
        self._operator=data[0]
        self._datatype = data[1]
        self._use_zero_crossing = data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Operator:":self._operator,"Datatype:":self._datatype,"Use Zero Crossing":self._use_zero_crossing}

class Powblk_f(Block):
    """The Powblk_f Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="POWBLK_f"
        self._to_the_power_of=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"to the power of:":self._to_the_power_of}

class Expblk_m(Block):
    """The Expblk_m Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EXPBLK_m"
        self._a=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"a:":self._a}

class Trigfun(Block):
    """The Trigfun Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="TrigFun"
        self._function=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Function:":self._function}

class Dlatch(Block):
    """The Dlatch Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="DLATCH"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}

class Matresh(Block):
    """The Matresh Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATRESH"
        self._datatype=data[0]
        self._input_size=data[1]
        self._output_size_desired = data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype":self._datatype,"Input size ":self._input_size,"Output Size desired:":self._output_size_desired}


class Matsing(Block):
    """The Matsing Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATSING"
        self._datatype= data[0]
        self._decomposition_type=data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Decomposition Type:":self._decomposition_type}

class Dflipflop(Block):
    """The Dflipflop Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="DFLIPFLOP"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Matpinv(Block):
    """The Matpinv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATPINV"
        self._datatype=data[0]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}


class Bitclear(Block):
    """The Bitclear Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="BITCLEAR"
        self._datatype=data[0]
        self._index_of_bit = data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Index of Bit:":self._index_of_bit}


class Bitset(Block):
    """The Bitset Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="BITSET"
        self._datatype=data[0]
        self._index_of_bit = data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Index of Bit:":self._index_of_bit}


class Exttri(Block):
    """The Exttri Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EXTTRI"
        self._datatype=data[0]
        self._extraction_type = data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Extration Type:":self._extraction_type}


class Cumsum(Block):
    """The Cumsum Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CUMSUM"
        self._datatype=data[0]
        self._sum_along = data[1]


    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Sum along:":self._sum_along}


class Matbksl(Block):
    """The Matbksl Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATBKSL"
        self._datatype=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}


class Logical_op(Block):
    """The Logical_op Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="LOGICAL_OP"
        self._number_of_inputs=data[0]
        self._operator=data[1]
        self._datatype=data[2]
        self._bitwise_rule=data[3]



    def parameters(self):
        return {"Function Name:":self._funcname,"Number of inputs:":self._number_of_inputs,"Datatype:":self._datatype,"Bitwise rule:":self._bitwise_rule}



class Matzconj(Block):
    """The Matzconj Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATZCONJ"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}


class Matdiag(Block):
    """The Matdiag Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATDIAG"
        self._datatype=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}


class Matdiv(Block):
    """The Matdiv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATDIV"
        self._datatype=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}

class Matdet(Block):
    """The Matdet Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATDET"
        self._datatype=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}

class Matlu(Block):
    """The Matlu Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATLU"
        self._datatype=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}


class Matexpm(Block):
    """The Matexpm Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="MATEXPM"
        self._datatype=data[0]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype}


class Intmul(Block):
    """The Intmul Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="INTMUL"
        self._datatype=data[0]
        self._use_zero_crossing = data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Use of Zero Crossing:":self._use_zero_crossing}

class Ricc(Block):
    """The Ricc Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="RICC"
        self._type=data[0]
        self._model = data[1]



    def parameters(self):
        return {"Function Name:":self._funcname,"Type:":self._type,"Model:":self._model}


class Shift(Block):
    """The Shift Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SHIFT"
        self._datatype=data[0]
        self._number_of_bits_to_shift = data[1]
        self._shift_type = data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Number of bits to shift:":self._number_of_bits_to_shift,"Shift Type:":self._shift_type}


class Convert(Block):
    """The Convert Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="CONVERT"
        self._input_type=data[0]
        self._output_type = data[1]
        self._do_not_overflow = data[2]


    def parameters(self):
        return {"Function Name:":self._funcname,"Input Type:":self._input_type,"Output Type:":self._output_type,"Do not overflow:":self._do_not_overflow}


class Submat(Block):
    """The Submat Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="SUBMAT"
        self._datatype=data[0]
        self._starting_row_index = data[1]
        self._ending_row_index = data[2]
        self._starting_column_index = data[3]
        self._ending_column_index = data[4]
        self._input_dimensions=data[5]



    def parameters(self):
        return {"Function Name:":self._funcname,"Starting Row index:":self._starting_row_index,"Ending row index:":self._ending_row_index,
                "Starting Column index:": self._starting_column_index, "Ending column index:": self._ending_column_index,
                "Input Dimensions:":self._input_dimensions}


class Extractbits(Block):
    """The Extractbits Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="EXTRACTBITS"
        self._datatype=data[0]
        self._bits_to_extract = data[1]
        self._index_of_bit = data[2]
        self._treat_bit_field_as_integer = data[3]

    def parameters(self):
        return {"Function Name:":self._funcname,"Datatype:":self._datatype,"Bits to extract:":self._bits_to_extract,"Index of bit:":self._index_of_bit,"Treat bit field as integer:":self._treat_bit_field_as_integer}

class Matsum(Block):
    """The Matsum Concrete Class which implements the Block interface"""

    def __init__(self, data):
        self._funcname = "MATSUM"
        self._datatype = data[0]
        self._sum_along = data[1]

    def parameters(self):
        return {"Function Name:": self._funcname, "DataType:": self._datatype, "Sum Along": self._sum_along}

class Deriv(Block):
    """The Deriv Concrete Class which implements the Block interface"""

    def __init__(self,data):
        self._funcname="DERIV"
        self._parameters="No Parameters"


    def parameters(self):
        return {"Function Name:":self._funcname,"Parameters:":self._parameters}
