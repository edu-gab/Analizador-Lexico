import datetime
from sintactico import parser
from lexico import lexer

# Comienza aporte Robespierre Triviño
def generar_nombre_log(nombre):
    ahora = datetime.datetime.now()
    nombre_archivo = ahora.strftime(f"lexico-{nombre}-%d%m%Y-%Hh%M.txt")
    return nombre_archivo


def leer_algoritmo(nombre_archivo):
    try:
        with open("algoritmos/prueba_" + nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return ""


estudiante = "robtrivi"


data = leer_algoritmo(estudiante + ".txt")
# file = open("logs/" + generar_nombre_log(estudiante), "w")
# Termina aporte Robespierre Triviño
r = parser.parse(data)
print(r)

