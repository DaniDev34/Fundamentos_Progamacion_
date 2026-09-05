def construir_tabla(tamaño=10):
    tabla = []
    for renglon in range(1, tamaño + 1):
        fila = []
        producto = 0
        for columna in range(1, tamaño + 1):
            producto += renglon
            fila.append(producto)
        tabla.append(fila)
    return tabla


def imprimir_tabla(tabla):
    
    for fila in tabla:
        print("\t".join(str(numero) for numero in fila))

def main():
    tabla = construir_tabla()

    print("Tabla de Pitagoras 10x10")
    imprimir_tabla(tabla)

main()