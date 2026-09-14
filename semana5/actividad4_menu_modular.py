def suma_elementos(tupla):
    total = 0
    for num in tupla:
        total += num
    return total


def buscar_telefono(contactos, nombre):
    if nombre in contactos:
        return contactos[nombre]
    return None


def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)


def modulo_tuplas():
    numeros = (10, 25, 33, 47, 52, 68, 71)
    print("Tupla original:", numeros)
    print("Tercer elemento:", numeros[2])
    num1 = float(input("Ingresa el primer número adicional: "))
    num2 = float(input("Ingresa el segundo número adicional: "))
    nueva_tupla = numeros + (num1, num2)
    print("Nueva tupla:", nueva_tupla)
    lista_ordenada = sorted(list(nueva_tupla))
    print("Lista ordenada:", lista_ordenada)
    total = suma_elementos(nueva_tupla)
    print("Suma de todos los elementos:", total)


def modulo_diccionarios():
    contactos = {
        "Ana": "555-0101",
        "Luis": "555-0102",
        "Mía": "555-0103"
    }
    print("Contactos iniciales:", contactos)
    nombre = input("Nombre del nuevo contacto: ")
    telefono = input("Teléfono del nuevo contacto: ")
    contactos[nombre] = telefono
    print("Contacto agregado.")
    print("Nombres de contactos registrados:")
    for clave in contactos:
        print(" -", clave)
    busqueda = input("Nombre a buscar para obtener su teléfono: ")
    resultado = buscar_telefono(contactos, busqueda)
    if resultado:
        print("El teléfono de", busqueda, "es:", resultado)
    else:
        print("Contacto no encontrado.")


def modulo_excepciones():
    try:
        num1 = int(input("Primer número entero: "))
        num2 = int(input("Segundo número entero: "))
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 / num2
        print("La suma de ambos es:", num1 + num2)
        print(num1, "dividido entre", num2, "es:", resultado)
    except ValueError:
        print("Error: Debes ingresar valores numéricos enteros. No se aceptan caracteres ni valores vacíos.")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero. Ingresa un divisor distinto de 0.")


def modulo_strings():
    return len(mensaje.split())
mensaje = "Mi canción favorita es Flamewall, es también mi nivel favorito de Geometry Dash"
print("Longitud del mensaje:", len(mensaje))
print("En mayúsculas:", mensaje.upper())
print("Texto reemplazado:", mensaje.replace("Flamewall", "Fairy Knife Hell"))
print("Palabras totales:", contar_palabras(mensaje))

def main():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Tuplas")
        print("2. Diccionarios")
        print("3. Excepciones")
        print("4. Strings")
        print("5. Finalizar")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            modulo_tuplas()
        elif opcion == "2":
            modulo_diccionarios()
        elif opcion == "3":
            modulo_excepciones()
        elif opcion == "4":
            modulo_strings()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


main()
