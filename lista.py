if __name__== "__main__":

    alumnos={'nombre':''}
    lista = [alumnos] 
    
    for registro in lista:
        registro['nombre'] = input("ingresa el codigo de alumno")

        print(lista[:])