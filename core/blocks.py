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
        self._funcname="CLR"
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
        return {"Function Name:":self._funcname,"Step time:":self._step_time,"Inital Value:":self._inital_value,"Final Value:":self._final_value}


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
     """The CCSB Concrete Class which implements the Block interface"""

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
        self._funcname="CurrentSensor"
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
         self._funcname="PULSE_SC"
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
         self._funcname="Modulo_Count"
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
         self._funcname="FROMWSB"
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

