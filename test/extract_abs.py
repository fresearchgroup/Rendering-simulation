import xml.etree.ElementTree as ET
import os
from pylatex import Document,Section,Subsection,Tabular,TikZ,TikZCoordinate,TikZNode,TikZDraw,TikZUserPath,TikZOptions,Figure

tree = ET.parse('abs.xml')
root = tree.getroot()
if __name__ == '__main__':
    #image_filename = os.path.join(os.path.dirname(__file__),'/home/kyoya2212/fossee_2019/Rendering-simulation/images/ABS_VALUE.png')
     image_filename = os.path.join('/home/kyoya2212/fossee_2019/Rendering-simulation/images/','ABS_VALUE.png')
     geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
     doc = Document(geometry_options=geometry_options)



listA = []
listB = []
listC = []
listD = []
for i in root.iter('XcosDiagram'):
    listB=(list(i.attrib.values()))
    listA=(list(i.attrib.keys()))
for child in root.findall("./mxGraphModel/root/BasicBlock"):
    listC=(list(child.attrib))
    listD=(list(child.attrib.values()))


with doc.create(Section('XcosDiagram')):
    with doc.create(Tabular('|c|c|')) as table:
        table.add_hline()
        table.add_row('Name','Value')
        table.add_hline()
        table.add_row([listA[0],listB[0]])
        table.add_hline()
        table.add_row([listA[1], listB[1]])
        table.add_hline()
        table.add_row([listA[2], listB[2]])
        table.add_hline()
        table.add_row([listA[3], listB[3]])
        table.add_hline()
        table.add_row([listA[4], listB[5]])
        table.add_hline()
        table.add_row([listA[6], listB[6]])
        table.add_hline()
        table.add_row([listA[7], listB[7]])
        table.add_hline()
        table.add_row([listA[8], listB[8]])
        table.add_hline()
        table.add_row([listA[9], listB[9]])
        table.add_hline()
        table.add_row([listA[10], listB[10]])
        table.add_hline()
        table.add_row([listA[11],listB[11]])
        table.add_hline()
with doc.create(Section('Basic info')):
    with doc.create(Tabular('|c|c|')) as table:
        table.add_hline()
        table.add_row('Name','Value')
        table.add_hline()
        table.add_row([listC[0],listD[0]])
        table.add_hline()
        table.add_row([listC[1], listD[1]])
        table.add_hline()
        table.add_row([listC[2], listD[2]])
        table.add_hline()
        table.add_row([listC[3], listD[3]])
        table.add_hline()
        table.add_row([listC[4], listD[5]])
        table.add_hline()
        table.add_row([listC[6], listD[6]])
        table.add_hline()
        table.add_row([listC[7], listD[7]])
        table.add_hline()
        table.add_row([listC[8], listD[8]])
        table.add_hline()
with doc.create(Section('Absolute Value')):
    with doc.create(Figure(position='h!')) as abs_pic:
        abs_pic.add_image(image_filename, width='500px')
        abs_pic.add_caption('Absolute Value Block')
doc.generate_pdf('example_abs', clean_tex=False)
