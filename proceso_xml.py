import urllib.request
import xml.etree.ElementTree as xml

# URL of the XML file
url = "https://www.w3schools.com/xml/simple.xml"

# Read the XML file
info = urllib.request.urlopen(url).read()
ivo = xml.fromstring(info.decode())

# Find all the food tags
query = ivo.findall(".//food")

# Show the number of records found
print("Cantidad de registros:", len(query))

# Show the information of each Record
for line in query:
    print("Nombre:", line.find('name').text)
    print("Precio:", line.find('price').text)
    print("Descripción:", line.find('description').text)
    print("Calorías:", line.find('calories').text)  
    print("*"*20)
