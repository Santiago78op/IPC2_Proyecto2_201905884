#directorios internos
from Constructor.Folders import Files
from Lista.SimpleFile import FileListaSimple
from Lista.MatrizDispersa import MatrizDispersa

#librerias externas
import xml.etree.ElementTree as ET
import os
from colorama import Fore
import ntpath


class Menu():
    
       def __init__(self):
              self.upload = 1
              self.findfile=2
              self.salir = 0
              

       def mostrarMenu(self)-> None:
              """
              Función que limpia la pantalla y muestra nuevamente el menu
              """  
              os.system('cls')
              print(Fore.CYAN,f'''\t<-- Menu Principal Chapín Warriors, S.A. -->\n
Seleccione una Opción:\n
       \t{self.upload}) -> Cargar Archivo
       \t{self.findfile}) -> Buscar Archivo
       \t{self.salir}) -> Salir\n''')

       def menu(self) -> bool:
              
              while True:
                     
                     self.mostrarMenu()
                     
                     opcionMenu = input("Insetar el numero de la opción: >> ")

                     
                     try:
                            opcionMenu = int(opcionMenu)  
                            
                            if opcionMenu == self.upload:
                                   ruta = input("Inserta la ruta de la CARPETA: >> ") 

                                   rutaFolder = os.path.exists(ruta)
                                   
                                   if rutaFolder == True:
       
                                          print(Fore.LIGHTWHITE_EX + "\nSe Cargo el Archivo con Exito!") 
                                                                 
                                          stado = os.startfile('Menu\\prueba.xml')    
                                          lista_files = self.readFolder(ruta)
                                          lista_files.bubbleSortFiles()
                                          lista_files.recorrerFile()
                                          stado = os.startfile('Menu\\prueba.xml')     
                                                 
                                   else:
                                          print(Fore.RED,'La ruta no Existe')   
                                          
                            elif opcionMenu == self.findfile:
                                   lista_files = self.readFolder(ruta)
                                   lista_files.recorrerFile()
                                   nameFile = input("\nInserta el nombre del Archivo: >> ") 
                                   dataFile = lista_files.busquedaFile(nameFile)
                                   
                                   if dataFile is None:
                                          print(Fore.RED,"No Existe el File Error!")  
                                   else:
                                          print(Fore.LIGHTWHITE_EX,"El File fue encontrado con Exito!!!!!")
                                          print("Nombre: ", dataFile.nombre, " Ruta: ", dataFile.ruta)
 
                                          listaMatrixes = self.readXML(dataFile.ruta)
                                                
                            elif opcionMenu == self.salir:
                                   print(Fore.GREEN,"\nEsto no es un adios sino un asta pronto!!!!!!\n")
                                   False
                                   break
                            else:
                                   print(Fore.YELLOW,'Opcion no válida...') 
                            input('\nPresiona enter para Ingresar al Menú...')
                                        
                     except ValueError as error:
                            print(Fore.RED,f'Error: {error}')
                            print(Fore.RED,'El programa no permite carateres tipo alpha')
                            input('Presione la tecla Enter para continuar@')
       
       
       
       def readFolder(self,rutaFolder):
              lista_files = FileListaSimple()
              print(rutaFolder)
              path = r'{}'.format(rutaFolder)
              os.chdir(path) 
              
              for file in os.listdir():
                     if file.endswith(".xml"):
                            file_path = f"{path}\{file}"
                            name = ntpath.basename(f"{file_path}")
                            newFile = Files(name,file_path)
                            lista_files.append(newFile)

              return lista_files
                            


       def readXML(self,ruta):
              entrada = ''
              file = open(ruta,'r')
              for line in file:
                     entrada+=line
              file.close()
              self.clonFile(entrada)
              
       def clonFile(self,contenido):
              path = r'C:\Users\santi\PyCharmProyect\IPC2\Proyecto[2]_IPC2\Data\contenedor.xml'
              with open(path, 'w') as f:
                     for line in contenido:         
                            f.write(line)



              
              # tree = ET.parse(nuevaRuta)
              # root = tree.getroot()
              
              
              
              
           
              

              

                                    