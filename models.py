class BasicBlock:
  def __init__(self, fname):
    self.funcname = fname


  def printname(self):
    print(self.funcname)


class GenSin(BasicBlock):
  def __init__(self, fname, magnitude,frequency , phase,):
    BasicBlock.__init__(self, fname)
    self.magnitude = magnitude
    self.frequency = frequency
    self.phase = phase

class CScope(BasicBlock):
  def __init__(self, fname,color_vector,ymin, ymax , refresh_period , buffer_size , accept_events , scope_name):
    BasicBlock.__init__(self, fname)
    self.color_vector=color_vector
    self.ymin=ymin
    self.ymax=ymax
    self.refresh_period=refresh_period
    self.buffer_size=buffer_size
    self.accept_events=accept_events
    self.scope_name=scope_name



class CSuper(BasicBlock):
  def __init__(self, fname,period,intime):
    BasicBlock.__init__(self, fname)
    self.period = period
    self.intime = intime
