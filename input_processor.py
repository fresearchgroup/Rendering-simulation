import os
import sys
import subprocess
from core.generators import *
from pylatex import Document, Section,Subsection, Itemize,Tabular,Figure
import xml.etree.ElementTree as ET

def process_file(xml_filepath):
    block_list= []
    context= []
    try:
        my_file = open(xml_filepath)
    except IOError:
        # file couldn't be opened, perhaps you need to create it
        print("Couldn't open file.Please check if the file path is correct.")
        exit()

    #opening the file in Scilab 6.0 to port xml schema to the latest version.
    path_to_upgraded_file=xml_filepath.split('/')[-1].split('.')[0]+'_updated.xcos'
    command='scs_m = xcosDiagramToScilab('+'\''+xml_filepath+'\''+');xcosDiagramToScilab("'+path_to_upgraded_file+'", scs_m); quit();'
    subprocess.call(['scilab-adv-cli', '-e', command])

    #reading the xml file
    tree = ET.parse(xml_filepath)
    root = tree.getroot()
    funcname=''
    #types of blocks to be extracted from the xcos file
    block_types=['BasicBlock','Summation','SuperBlock','EventOutBlock','Product','GroundBlock','VoltageSensorBlock']
    #generate objects one by one store it in a output list
    try:
        for data in root.findall('./mxGraphModel/root/'):
            if data.tag in block_types:

                    funcname=data.get('interfaceFunctionName')
                    classname=eval(str(funcname))

                    if classname:
                        obj = classname(data)
                        block_list.append(obj.block)
        for data in root.findall('./Array/add'):
            context.append(data.get('value'))

        return [block_list,context]

    except NameError:
        print("Block not found:", funcname)
        exit()

    except IndexError:
        print("All parameters should be entered for the block:",funcname)
        exit()






def render(img_dir, img_name, pdf_name , output_list):
    image_filename = os.path.join(img_dir,img_name)
    geometry_options = {"tmargin": "1cm","lmargin":"1cm" }
    doc = Document(geometry_options=geometry_options)
    #creates image section in LaTeX
    with doc.create(Section("Xcos")):
        with doc.create(Figure(position='h!')) as abs_pic:
            abs_pic.add_image(image_filename, width='450px')
            doc.append('\n')
            doc.append('\n')
            doc.append('\n')
    #creates Context section in LaTeX if context exists
    if output_list[1]:
        with doc.create(Subsection("Context")):
            with doc.create(Itemize()) as itemize:
                for data in output_list[1]:
                    itemize.add_item(data)
    #creates Block section in LaTeX
    with doc.create(Subsection("Blocks")):
        for i in output_list[0]:
            if i is not None:
                doc.append('\n')
                doc.append('\n')
                doc.append('\n')
                with doc.create(Tabular('|c|c|')) as table:
                    table.add_hline()
                    for key, value in i.parameters().items():
                        table.add_row(key,value)
                        table.add_hline()



    doc.generate_pdf(pdf_name, clean_tex=False)

if __name__ == '__main__':
    output_list=process_file(sys.argv[1])
    render(sys.argv[2], sys.argv[3],sys.argv[4], output_list)

