
paises = {"España": "Español", "EEUU": "Ingles", "Italia": "Italiano"}

def buscar_diccionario(pais):
    try:
        paises[pais]
    except KeyError:
        print("No existe esa clave en el diccionario")
    else:
        print("Si se encuentra en el diccionario: {}".format(paises[pais]))

    return

print(buscar_diccionario("Qatar"))
print(buscar_diccionario("España"))
