from ast import Try
import os
from symbol import try_stmt
CARPETA = 'contactos/' #carpeta de contactos
EXTENSION = '.txt' #extensión de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe
    crear_directorio()
    #muesta el menú de opciones
    mostrar_menu()
    #preguntar al usuario la acción
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1: #El switch no existe en Python
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print('Ver contacto')
            mostrar_contactos()
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto
            preguntar = False
        else:
            print('Opción no valida, intenta de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el archivo a eleminar \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Eliminado correctamente \r\n')
    except expression as identifier:
        print('No existe el archivo')
    app()

def buscar_contacto():
    nombre = input('Seleccione el nombre a buscar: \r\n')

    try: 
            with open(CARPETA + nombre + EXTENSION) as contacto:
                print('\r\n Información del Contacto')
                for linea in contacto:
                    print(linea.rstrip())
                print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre a editar')
    nombre_anterior = input('Nombre a editar: \r\n')

    #Revisa si el archivo existe para editarlo
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el nuevo Nombre del contacto: \r\n')
            telefono_contacto = input('Agrega el nuevo número telefónico:\r\n')
            categoria_contacto = input('Agrega la nueva Categoría del contacto:\r\n')
            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION,
            CARPETA + nombre_contacto + EXTENSION)
            print('\r\n Contacto editado correctamente \r\n')
    else:
        print('Ese contacto no existe')
    
    app()

def agregar_contacto():
    print('Agregar el nuevo ')
    nombre_contacto = input('Nombre del contacto: \r\n') #\r\n son saltos de linea
    
    #Revisa si el archivo existe
    existe = existe_contacto(nombre_anterior)

    if not existe:
        with open(CARPETA + nombre_contacto+ EXTENSION, 'w') as archivo:
            telefono_contacto = input('Ingresa el número telefónico:\r\n')
            categoria_contacto = input('Categoría del contacto:\r\n')
            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
            print('\r\n Contacto agregado correctamente \r\n')
    else:
        print('Ya existe ese contacto')
    app()

def mostrar_menu():
    print('Seleccione la opción que desea realizar')
    print('1 Agregar Nuevo Contacto')
    print('2 Edidat Contacto')
    print('3 Ver Contactos')
    print('4 Buscar Contacto')
    print('5 Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear carpeta
        os.makedirs(CARPETA)
    else:
        print('La carpeta ya existe')   

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()    