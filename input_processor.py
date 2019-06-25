import os
import sys
import subprocess
from core.generators import *
from pylatex import Document, Section, Itemize, Enumerate, Description, \
    Command,Document,TikZ,TikZCoordinate,TikZNode,TikZDraw,TikZUserPath,TikZOptions,Figure
import xml.etree.ElementTree as ET

def process_file(xml_filepath):
    output_list=[]
    '''
    path_to_upgraded_file=xml_filepath.split('/')[-1].split('.')[0]+'_updated.xcos'
    command='scs_m = xcosDiagramToScilab('+'\''+xml_filepath+'\''+');xcosDiagramToScilab("'+path_to_upgraded_file+'", scs_m); quit();'
    subprocess.call(['scilab-adv-cli', '-e', command])
    '''
    #reading the xml file
    tree = ET.parse(xml_filepath)
    root = tree.getroot()
    block_types=['BasicBlock','Summation','SuperBlock']
    #generate objects one by one store it in a output list
    try:
        for data in root.findall('./mxGraphModel/root/'):
          if data.tag in block_types:
            classname=eval(str(data.get('interfaceFunctionName')))
            #print(classname)
            if classname:
                #print(classname)
                obj = classname(data)
                output_list.append(obj.block)

        return output_list
        #return 0
    except NameError:
        print("Block not found:", classname.__name__)

    except IndexError:
        print("All parameters should be entered for the block:",classname.__name__)
        exit()





def render(img_dir, img_name, pdf_name , output_list):
    image_filename = os.path.join(img_dir,img_name)
    geometry_options = {"tmargin": "1cm","lmargin":"1cm" }
    doc = Document(geometry_options=geometry_options)
    print(output_list)
    with doc.create(Section("Xcos")):
        with doc.create(Figure(position='h!')) as abs_pic:
            abs_pic.add_image(image_filename, width='120px')
        with doc.create(Description()) as desc:
            for i in output_list:
                if i is not None:
                    for key,value in i.parameters().items():
                        desc.add_item(key,value)

    doc.generate_pdf(pdf_name, clean_tex=False)

if __name__ == '__main__':
    output_list=process_file(sys.argv[1])
    render(sys.argv[2], sys.argv[3],sys.argv[4], output_list)

