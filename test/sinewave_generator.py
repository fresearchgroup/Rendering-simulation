import xml.etree.ElementTree as ET
import os
from pylatex import Document,Section,Subsection,Tabular,TikZ,TikZCoordinate,TikZNode,TikZDraw,TikZUserPath,TikZOptions,Figure

tree = ET.parse('/home/kyoya2212/Test_files/sinewave_generator.xml')
root = tree.getroot()

if __name__ == '__main__':
    image_filename = os.path.join('/home/kyoya2212/Test_files/','sinewave_generator.png')
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
    doc = Document(geometry_options=geometry_options)
listA = []
listB = []
listC = []
listD = []
for i in root.findall("./mxGraphModel/root/BasicBlock/ScilabString/data"):
    listA.append(list(i.attrib.values())[2])

for i in root.findall("./mxGraphModel/root/BasicBlock/SuperBlockDiagram/mxGraphModel/root/BasicBlock/ScilabString/data"):
    listB.append(list(i.attrib.values())[2])

with doc.create(Section('Sinewave Generator')):

        with doc.create(Figure(position='h!')) as abs_pic:
            abs_pic.add_image(image_filename, width='120px')
            abs_pic.add_caption('SineWave Generator')
        with doc.create(Subsection('GenSin')):
            with doc.create(Tabular('|c|c|')) as table:
                table.add_hline()
                table.add_row('Name','Value')
                table.add_hline()
                table.add_row(['magnitude',listA[0]])
                table.add_hline()
                table.add_row(['frequency', listA[1]])
                table.add_hline()
                table.add_row(['pulse', listA[2]])
                table.add_hline()
        with doc.create(Subsection('Cscope')):
            with doc.create(Tabular('|c|c|')) as table:
                table.add_hline()
                table.add_row('Name','Value')
                table.add_hline()
                table.add_row(['Color Vector',listA[3]])
                table.add_hline()
                table.add_row(['Output window number', listA[4]])
                table.add_hline()
                table.add_row(['Output window position', listA[5]])
                table.add_hline()
                table.add_row(['Output window sizes',listA[6]])
                table.add_hline()
                table.add_row(['Ymin', listA[7]])
                table.add_hline()
                table.add_row(['Ymax', listA[8]])
                table.add_hline()
                table.add_row(['Refresh period',listA[9]])
                table.add_hline()
                table.add_row(['Buffer Size', listA[10]])
                table.add_hline()
                table.add_row(['Accept Herited Events', listA[11]])
                table.add_hline()
                table.add_row(['Name of Scope', listA[12]])
                table.add_hline()
        with doc.create(Subsection('Clock')):
            with doc.create(Tabular('|c|c|')) as table:
                table.add_hline()
                table.add_row('Name','Value')
                table.add_hline()
                table.add_row(['Period',listB[0]])
                table.add_hline()
                table.add_row(['Initialisation Time',listB[1]])
                table.add_hline()



doc.generate_pdf('sinewave_generator', clean_tex=False)


