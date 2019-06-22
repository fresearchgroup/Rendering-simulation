from abc import ABC, abstractmethod

class Block(ABC):
    """
    Abstract class for blocks
    """

    @abstractmethod
    def parameters(self):
        pass


class GenSin(Block):
    """The GenSin Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._funcname = "GENSIN_f"
        self._magnitude = data[0]
        self._frequency = data[1]
        self._phase = data[2]

    def parameters(self):

        return {"Function Name:":self._funcname,"magnitude:": self._magnitude, "frequency:": self._frequency, "phase:": self._phase}

class CScope(Block):
    """The CScope Concrete Class which implements the IBlock interface"""


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
    """The CSuper Concrete Class which implements the IBlock interface"""

    def __init__(self,data):
        self._funcname = "CLOCK_c"
        self._period = data[0]
        self._intime = data[1]

    def parameters(self):

        return {"Function Name:":self._funcname,"Period:": self._period, "Initialisation Time:": self._intime}



#csslti
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




