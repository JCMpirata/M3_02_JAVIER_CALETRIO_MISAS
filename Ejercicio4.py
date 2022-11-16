
def nueva_operacion(numero):
    try:
        resultado = numero + 10
    except TypeError:
        print("Los datos introducidos son incorrectos")
    else:
        print("El resultado es: ", resultado)
        
    return

nueva_operacion("2")
nueva_operacion(2)

