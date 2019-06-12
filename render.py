import xml.etree.ElementTree as ET
from pylatex import Document , Section, Subsection, Tabular
from models import GenSin, CScope ,CSuper




output=[]
x = GenSin("gensin", 6.5 , 1 , 0)
y=CScope("cscope",[1,3,5,7,9,11,13,15],-15,15,30,20,0,None)
z= CSuper("csuper",0.1,0.1)
output.append(x)
output.append(y)
output.append(z)

import os

if __name__ == '__main__':
   image_filename=os.path.join(os.path.dirname(__file__))
   geometry_options = {"tmargin": "1cm","lmargin":"1cm" }
   doc = Document(geometry_options=geometry_options)
   for i in output:
     if(i.funcname == "gensin"):
         with doc.create(Section('Sine Wave Generator')):
                with doc.create(Tabular('|c|c|c|c|')) as table:
                   table.add_hline()
                   table.add_row(['Function Name','Magnitude','Frequency','Phase'])
                   table.add_hline()
                   table.add_row([i.funcname,i.magnitude,i.frequency,i.phase])
                   table.add_hline()
     if(i.funcname == "cscope"):
         with doc.create(Section('CScope')):
                with doc.create(Tabular('|c|c|c|c|c|c|c|c|')) as table:
                   table.add_hline()
                   table.add_row(['Function Name','Color Vector','Ymin','Ymax','Refresh Period','Buffer Size','Accept Herited Events',' Name of Scope'])
                   table.add_hline()
                   table.add_row([i.funcname,i.color_vector,i.ymin,i.ymax,i.refresh_period,i.buffer_size,i.accept_events,i.scope_name])
                   table.add_hline()
     if(i.funcname == "csuper"):
         with doc.create(Section('Clock')):
                with doc.create(Tabular('|c|c|c|')) as table:
                   table.add_hline()
                   table.add_row(['Function Name','Period','Initialisation Time'])
                   table.add_hline()
                   table.add_row([i.funcname,i.period,i.intime])
                   table.add_hline()

         doc.generate_pdf('example',clean_tex=False)



