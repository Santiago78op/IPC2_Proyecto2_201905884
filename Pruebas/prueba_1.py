# import os

# ruta = input("Inserta la ruta de la CARPETA: >> ")

# dia = os.path.exists(ruta)
# print(dia)

# if rutaFolder == True:

#         print("\nSe Cargo el Archivo con Exito!")
# else:
#         print('La ruta no Existe')

# import os

# ruta = input("Inserta la ruta de la CARPETA: >> ")
# path = r'{}'.format(ruta)

# os.chdir(path)


# def read_text_file(file_path):
#     with open(file_path, 'r') as f:
#         print(f.read())


# for file in os.listdir():


#     if file.endswith(".txt"):
#         file_path = f"{path}\{file}"
#         print(file_path)


#         read_text_file(file_path)

# file = open(f','r')
# for line in file:
#     print(line)
# file.close()

# import os

# path_name = ""

# if os.path.isfile(path_name):
#   print("File exists")
#   f = open(path_name)
#   #Execute other file operations here
#   f.close()
# else:
#   print("File does not exist! IOError has occured")

# import os

# f = open('Data/prueba.txt')
# stado = os.startfile('Menu\\prueba.xml')
from xml.dom.minidom import Element
import xml.etree.ElementTree as ET

# treeCatch = ET.parse('Data\Entrada_Ejemplo_1.xml')
# rootCatch = treeCatch.getroot()
#             for afterCitys in rootCatch:
#                 for afterCity in afterCitys.iter('ciudad'):
#                         for cityafter in afterCity.iter('nombre'):
#                             nameafter = cityafter.text.strip()
#                             if namebefore == nameafter:
#                                 print(namebefore)
#                                 print(nameafter)
# Archivo Anterior
tree = ET.parse('Data\contenedor.xml')
root = tree.getroot()


for ciudades in root:
    for ciudad in ciudades.iter('ciudad'):
        for nombre in ciudad.iter('nombre'):
            name = nombre.text.strip()
            filas = nombre.attrib['filas']
            columnas = nombre.attrib['columnas']
            print(name, filas, columnas)

        filasF = 1
        for rows in ciudad.iter('fila'):
            chart = rows.text
            chart = chart.replace('"', '')
            print(chart)

            chart = str(chart)
            cont = 0
            for f in range(int(filasF), int(filasF)+1):
                for c in range(1, int(columnas)+1):
                    k = chart[cont]
                    print(k, f, c)
                    cont += 1
            filasF += 1

        for unitMilitary in ciudad.iter('unidadMilitar'):
            unit = unitMilitary.text.strip()
            fila = unitMilitary.attrib['fila']
            columna = unitMilitary.attrib['columna']
            print(unit, fila, columna)

# for unitMilitary in ciudad.iter('unidadMilitar'):
#     unit = unitMilitary.text.strip()
#     unit = str(unit)
#     fila = unitMilitary.attrib['fila']
#     fila = int(fila)
#     columna = unitMilitary.attrib['columna']
#     columna = int(columna)
#     newUnit = UnitMilitary(unit, fila, columna)
#     newCity.list_row.append(newUnit)

# filasF = 1
# for rows in ciudad.iter('fila'):
#     chart = rows.text
#     chart = chart.replace('"', '')

#     chart = str(chart)
#     cont = 0
#     for f in range(int(filasF), int(filasF)+1):
#         for c in range(1, int(columnas)+1):
#             k = chart[cont]
#             cont += 1
#             newRow = Filas(k, f, c)
#             lista_filas.append(newRow)
#     filasF += 1
