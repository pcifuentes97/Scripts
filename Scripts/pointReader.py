import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
file = '/home/lambdaworkstation/Documents/Pathogen_slides/Cancer/Korea/Training/Training_phase_1_001/01_01_0083.xml'
tree = ET.parse(file)
root = tree.getroot()
text = open('values2.txt', 'a')
xMax = 0
yMax = 0
lstX = []
lstY = []

for Annotation in root.iter('Annotation'):
    if(int(Annotation.attrib['Id']) == 2):
        for Region in Annotation.iter('Region'):
            if(float(Region.attrib['Zoom']) == 0.036983):
                for Vertex in Region.iter('Vertex'):
                    if(int(Vertex.attrib['Y']) > yMax):
                        yMax = int(Vertex.attrib['Y'])
                    if(int(Vertex.attrib['X']) > xMax):
                        xMax = int(Vertex.attrib['X'])
                    if(int(Vertex.attrib['Y']) >= 0):
                        line = Vertex.attrib['X'] + ', ' + Vertex.attrib['Y'] + '\n'
                    text.write(line)
                    lstX.append(Vertex.attrib['X'])
                    lstY.append(Vertex.attrib['Y'])


print(xMax , ' ' , yMax)
plt.plot(text, 'k')
plt.savefig('test2.png')
plt.show()
plt.draw()
text.close()

    

