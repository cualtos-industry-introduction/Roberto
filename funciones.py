lista = []
salida = "No"

def agregarContacto():
    nuevo_contacto = {}
    nuevo_contacto ['nombre'] = input ("Nombre: ")
    nuevo_contacto ['correo'] = input ("Correo: ")
    nuevo_contacto ['dirección'] = input ("Dirección: ")
    #añadir el valor de la lista
    lista.append(nuevo_contacto)

while(salida == "No"):
    entrada = input ("Escribe la acción a efectuar: nuevo,mostrar, salir ")
    if entrada == "nuevo":
        agregarContacto()
        print ("contacto agregado")
    elif entrada == "mostrar":
        print(lista[:])
    elif entrada == "salir":
        exit()
    else:
        print("Opción no válida")

