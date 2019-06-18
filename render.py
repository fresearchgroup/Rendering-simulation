
from abc import ABCMeta, abstractstaticmethod

from pylatex import Document, Section, Itemize, Enumerate, Description, \
    Command,Document,TikZ,TikZCoordinate,TikZNode,TikZDraw,TikZUserPath,TikZOptions,Figure
from blockfactory import *
import os
import sys
xml_filepath=sys.argv[1]
img_dir=sys.argv[2]
img_name=sys.argv[3]
pdf_name=sys.argv[4]

if __name__ == '__main__':
   output(sys.argv[1])
   image_filename = os.path.join(sys.argv[2],sys.argv[3])
   geometry_options = {"tmargin": "1cm","lmargin":"1cm" }
   doc = Document(geometry_options=geometry_options)

   with doc.create(Section("Xcos")):
       with doc.create(Figure(position='h!')) as abs_pic:
           abs_pic.add_image(image_filename, width='120px')
       with doc.create(Description()) as desc:
           for i in output_list:
               for key,value in i.parameters().items():
                   desc.add_item(key,value)





   doc.generate_pdf(sys.argv[4],clean_tex=False)

