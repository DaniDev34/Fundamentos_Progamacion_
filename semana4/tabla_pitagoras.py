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


def consultar_producto(tabla, renglon, columna):

    return tabla[renglon - 1][columna - 1]

def imprimir_tabla(tabla):
    
    for fila in tabla:
        print("\t".join(str(numero) for numero in fila))

def main():
    tabla = construir_tabla()

    print("Tabla de Pitagoras 10x10")
    imprimir_tabla(tabla)
    while True:
        try:
            renglon = int(input("\nRenglón del 1 al 10: "))
            columna = int(input("Columna del 1 al 10: "))
        except ValueError:
            print("Error, debes ingresar números enteros.")
            continue

        if 1 <= renglon <= 10 and 1 <= columna <= 10:
            break
        print("Error: los factores deben estar entre 1 y 10.")
    producto = consultar_producto(tabla, renglon, columna)
    print(f"\nEl producto de {renglon} x {columna} es: {producto}")

main()