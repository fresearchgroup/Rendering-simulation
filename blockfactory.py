from abc import ABCMeta, abstractstaticmethod
import xml.etree.ElementTree as ET
<<<<<<< HEAD

output_list=[]
=======
output_list=[]

>>>>>>> decd253b6c0d7f1fb51ee2022a8437d747f15491
class IBlockFactory(metaclass=ABCMeta):
    """The Block Interface"""
    @abstractstaticmethod
    def parameters():
        """A static interface method"""


class GenSin(IBlockFactory):
    """The GenSin Concrete Class which implements the IBlock interface"""
    data=[]
    def process_data(self,block_root):

        for y in block_root.findall("./ScilabString/data"):
              self.data.append(y.get('value'))


    def __init__(self,block_root):
        self._funcname="GENSIN_f"
        self.process_data(block_root)
        self._magnitude = self.data[0]
        self._frequency =self.data[1]
        self._phase = self.data[2]

    def parameters(self):
<<<<<<< HEAD
        return {"Function Name:":self._funcname,"magnitude:": self._magnitude, "frequency:": self._frequency, "phase:": self._phase}
=======
        return {"Function Name":self._funcname,"magnitude": self._magnitude, "frequency": self._frequency, "phase": self._phase}
>>>>>>> decd253b6c0d7f1fb51ee2022a8437d747f15491

class CScope(IBlockFactory):
    """The CScope Concrete Class which implements the IBlock interface"""

    data=[]
    def process_data(self,block_root):
        for y in block_root.findall("./ScilabString/data"):
              self.data.append(y.get('value'))


    def __init__(self,block_root):
        self._funcname="CSCOPE"
        self.process_data(block_root)
        self._colorvector = self.data[0]
        self._output_window_number= self.data[1]
        self._output_window_position=self.data[2]
        self._output_window_sizes= self.data[3]
        self._ymin = self.data[4]
        self._ymax = self.data[5]
        self._refresh_period = self.data[6]
        self._buffer_size = self.data[7]
        self._accept_herited_events = self.data[8]
        self._scope_name = self.data[9]


    def parameters(self):
<<<<<<< HEAD
        return {"Function Name:":self._funcname,"Color or mark vector:" :self._colorvector,"Output window number:":self._output_window_number,"Output window position:":self._output_window_position,"Output window sizes:":self._output_window_sizes, "Ymin:": self._ymin, "Ymax:": self._ymax,"Refresh period:" : self._refresh_period ,"Buffer Size": self._buffer_size,"Accept herited events:": self._accept_herited_events,"Name of Scope:": self._scope_name}
=======
        return {"Function Name":self._funcname,"Color or mark vector:" :self._colorvector,"Output window number":self._output_window_number,"Output window position":self._output_window_position,"Output window sizes":self._output_window_sizes, "Ymin": self._ymin, "Ymax": self._ymax,"Refresh period" : self._refresh_period ,"Buffer Size": self._buffer_size,"Accept herited events": self._accept_herited_events,"Name of Scope": self._scope_name}
>>>>>>> decd253b6c0d7f1fb51ee2022a8437d747f15491


class CSuper(IBlockFactory):
    """The CSuper Concrete Class which implements the IBlock interface"""

    data=[]
    def process_data(self,block_root):

        for y in block_root.findall("./SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"):
              self.data.append(y.get('value'))

    def __init__(self,block_root):
        self._funcname="CLOCK_c"
        self.process_data(block_root)
        self._period = self.data[0]
        self._intime = self.data[1]

    def parameters(self):
<<<<<<< HEAD
        return {"Function Name:":self._funcname,"Period:": self._period, "Initialisation Time:": self._intime}
=======
        return {"Function Name":self._funcname,"Period": self._period, "Initialisation Time": self._intime}
>>>>>>> decd253b6c0d7f1fb51ee2022a8437d747f15491



class BlockFactory:
    """Tha Factory Class"""

    @staticmethod
    def get_block(funcname,block_root):
        """A static method to get a block"""
        try:
            if funcname == "GENSIN_f":
                return GenSin(block_root)

            if funcname == "CSCOPE":
                return CScope(block_root)

            if funcname == "CLOCK_c":
                return CSuper(block_root)

            raise AssertionError("Block Not Found")
        except AssertionError as _e:
            print(_e)
        return None


<<<<<<< HEAD
def output(xml_filepath):

    tree = ET.parse(xml_filepath)
=======
def output():

    tree = ET.parse('sine.xml')
>>>>>>> decd253b6c0d7f1fb51ee2022a8437d747f15491
    root = tree.getroot()
    for x in root.findall('./mxGraphModel/root/'):
        if(x.tag == "BasicBlock"):
           BLOCK_FACTORY= BlockFactory().get_block(x.get('interfaceFunctionName'),x)
<<<<<<< HEAD

           output_list.append(BLOCK_FACTORY)
    return output_list
=======
           #print(f"{BLOCK_FACTORY.__class__}: {BLOCK_FACTORY.parameters()}")
           output_list.append(BLOCK_FACTORY)







>>>>>>> decd253b6c0d7f1fb51ee2022a8437d747f15491
