import xml.etree.ElementTree as ET
tree = ET.parse('sine_ex.xml')
root = tree.getroot()

functionNames=[]
for child in root.findall('child'):
   functionName= child.get('functionName')
   if not functionName is None:
      functionNames.append(functionName)

print(functionNames)
'''
genSin =  {'Magintude':'0','Frequency':'0','Phase':'0'}
genSinList=[]
cscope={}
cscopeList=[]
'''



for i in functionNames:
   if i == 'gensin':
      for data in root[functionNames.index(i)].iter('expression'):
         print(data.text)
      print("-------")
   if i == 'cscope':
      for data in root[functionNames.index(i)].iter('expression'):
         print(data.text)
      #for data in root[functionNames.index(i)].iter('ipar'):
         #print(data.text)
      print("-------")
   if i == 'csuper':
      for data in root[functionNames.index(i)].iter('expression'):
         print(data.text)
      print("-------")
