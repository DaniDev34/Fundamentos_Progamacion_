# Actividad 4 — Menú Modular (Tuplas, Diccionarios, Excepciones y Strings)

---

## Introducción

## Descripción de la actividad

Desarrollar una **aplicación interactiva en Python** que demuestre el uso integral de **tuplas**, **diccionarios**, **manipulación de cadenas de texto (strings)** y **manejo robusto de excepciones**, estructurada a través de un **menú principal modular** controlado por un ciclo. El usuario selecciona por número qué sección desea ejecutar (Tuplas, Diccionarios, Excepciones, Strings o Finalizar) y el programa delega cada tarea a funciones modulares.

---

## Definiciones

Se definen las funciones de apoyo que **regresan valor** (con `return`) y se reutilizan en varios módulos:

- `suma_elementos(tupla)` **regresa valor**: recorre con un ciclo `for` todos los elementos de la tupla, acumulando su suma en un acumulador, y retorna el total.
- `buscar_telefono(contactos, nombre)` **regresa valor**: si el nombre se encuentra como clave en el diccionario, retorna el teléfono asociado; en caso contrario retorna `None`.
- `contar_palabras(cadena)` **regresa valor**: aplica el método de strings `split()` para separar el texto en palabras y retorna la cantidad obtenida con `len()`.

```python
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
```

---

## Módulo de tuplas

La función `modulo_tuplas()` **no regresa valor**: crea la tupla `numeros` con siete elementos, imprime el **tercer elemento** con `numeros[2]`, captura **dos números adicionales** mediante `input()` y los anexa con el operador `+` para crear una **nueva tupla**. Convierte la tupla en **lista** con `list()`, le aplica un **ordenamiento** con `sorted()` y muestra el resultado llamando a `suma_elementos()` para retornar la **suma** de todos sus elementos.

```python
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
```

---

## Módulo de diccionarios

La función `modulo_diccionarios()` **no regresa valor**: crea el diccionario `contactos` con **tres registros iniciales** (clave: nombre, valor: teléfono), permite la **captura y adición** de un nuevo contacto con `contactos[nombre] = telefono`, **itera sobre las claves** con un ciclo `for` para imprimir exclusivamente los **nombres** de los contactos y, con la función `buscar_telefono()`, busca el teléfono del nombre ingresado y lo muestra en consola si se localiza.

```python
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
```

---

## Módulo de excepciones

La función `modulo_excepciones()` **no regresa valor**: solicita al usuario ingresar **dos números enteros** y los protege con un bloque **`try-except`**. Si el usuario ingresa caracteres no numéricos o vacíos se captura el error `ValueError` desplegando un **mensaje de error controlado**. Si el segundo número es cero se lanza y captura `ZeroDivisionError` de forma específica con un **mensaje amigable**. En caso exitoso se imprime la **suma** de ambos y el resultado de la **división**.

```python
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
```

---

## Módulo de strings

La función `modulo_strings()` **no regresa valor**: crea la variable `mensaje`, imprime su **longitud** con `len()`, transforma la totalidad del texto a **mayúsculas** con el método `upper()`, **busca y reemplaza** una palabra clave con `replace()` y muestra la **cantidad de palabras** llamando a `contar_palabras()`, que retorna el conteo.

```python
def modulo_strings():
    mensaje = "Python es un lenguaje poderoso"
    print("Mensaje original:", mensaje)
    print("Longitud del mensaje:", len(mensaje))
    print("En mayúsculas:", mensaje.upper())
    mensaje_reemplazado = mensaje.replace("Python", "programación")
    print("Texto reemplazado:", mensaje_reemplazado)
    total_palabras = contar_palabras(mensaje)
    print("Palabras totales:", total_palabras)
```

---

## Menú principal

La función `main()` **no regresa valor**: construye una interfaz de consola con un **ciclo controlado** y un menú de **opciones numéricas** (Tuplas, Diccionarios, Excepciones, Strings o Finalizar). Al seleccionar una opción se **llama de forma modular** a la función correspondiente mediante `if/elif`. El ciclo permite regresar al menú tras cada ejecución y **finaliza** únicamente al seleccionar la opción 5. Al final del archivo se invoca la función con `main()`.

```python
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
            print("Opción no válida. Prueba de nuevo.")


main()
```
---

# Ejercicios Extras — Semana 5

Resolución de los 4 ejercicios extras evaluables de la actividad **Menú Modular**. Cada ejercicio documenta el procedimiento y la lógica aplicada, seguido del código correspondiente.

## Extra 1: Sistema de calificaciones con tuplas

- `suma_calificaciones(calificaciones)` **regresa valor** (con `return`): acumula con un ciclo `for` la suma de todos los elementos de la tupla.
- Se crea la tupla `calificaciones = (7.5, 9.0, 8.0, 6.5, 10.0)`, se imprime la **tercera calificación** con `calificaciones[2]` y se capturan **dos calificaciones nuevas** con `input()`.
- Las nuevas calificaciones se **anexan** con el operador `+` en una **nueva tupla**; esta se convierte en **lista** con `list()` y se ordena **de mayor a menor** con `sorted(..., reverse=True)`.
- Se muestra la **suma total** mediante la función que retorna el valor.
- Se elige la tupla porque sus elementos no deben modificarse; la lista permite el ordenamiento y la función permite reutilizar el cálculo.

```python
def suma_calificaciones(calificaciones):
    total = 0
    for c in calificaciones:
        total += c
    return total

calificaciones = (7.5, 9.0, 8.0, 6.5, 10.0)
print("Tercera calificación:", calificaciones[2])
nueva1 = float(input("Nueva calificación 1: "))
nueva2 = float(input("Nueva calificación 2: "))
nueva_tupla = calificaciones + (nueva1, nueva2)
print("Nueva tupla:", nueva_tupla)
lista_ordenada = sorted(list(nueva_tupla), reverse=True)
print("Lista ordenada (mayor a menor):", lista_ordenada)
print("Suma total:", suma_calificaciones(nueva_tupla))
```
---

## Extra 2: Agenda de contactos con búsqueda

- `buscar_telefono(agenda, nombre)` **regresa valor** (con `return`): usa `agenda.get(nombre)` para retornar el teléfono asociado a la clave.
- Se crea el diccionario `agenda` con **tres contactos iniciales** y se captura un **nuevo contacto** (nombre y teléfono) con `input()` para agregarlo con `agenda[nombre] = teléfono`.
- Con `keys()` se imprimen **todos los nombres** en una sola línea usando `", ".join(...)`.
- Se busca el **teléfono del nuevo contacto** mediante la función que retorna el valor y se muestra el resultado.
- Se elige el diccionario porque la clave (nombre) está asociada directamente al valor (teléfono) y permite una búsqueda eficiente.

```python
def buscar_telefono(agenda, nombre):
    return agenda.get(nombre)

agenda = {
    "Montserrat": "4411676121",
    "Dulce": "5561524514",
    "Carolina": "3312456789"
}
nombre_nuevo = input("Nombre del nuevo contacto: ")
telefono_nuevo = input("Teléfono del nuevo contacto: ")
agenda[nombre_nuevo] = telefono_nuevo
print("Contactos registrados:", ", ".join(agenda.keys()))
busqueda = input("Nombre a buscar: ")
telefono = buscar_telefono(agenda, busqueda)
print("El teléfono de", busqueda, "es:", telefono)
```
---

## Extra 3: Calculadora segura con manejo de excepciones

- El programa pide **dos números enteros** con `input()` y realiza la **división** del primero entre el segundo.
- Un bloque **`try-except`** captura `ValueError` (caracteres no numéricos o vacíos) mostrando un **mensaje controlado**.
- Un bloque específico **`except ZeroDivisionError`** muestra un **mensaje amigable** si el segundo número es cero.
- El bloque `try-except` garantiza que el programa no se detenga de forma abrupta ante errores de entrada o de cálculo. En caso exitoso se muestra el resultado de la división.

```python
try:
    num1 = int(input("Primer número entero: "))
    num2 = int(input("Segundo número entero: "))
    resultado = num1 / num2
    print(num1, "dividido entre", num2, "es:", resultado)
except ValueError:
    print("Error: Debes ingresar caracteres numéricos. No se aceptan valores vacíos ni no numéricos.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero. Ingresa un divisor distinto de 0.")
```
---

## Extra 4: Analizador de mensajes con strings

- `contar_palabras(mensaje)` **regresa valor** (con `return`): aplica `mensaje.split()` para separar las palabras y retorna la cantidad con `len()`.
- Se crea la variable `mensaje = "Mi canción favorita es Flamewall, es también mi nivel favorito de Geometry Dash"`.
- Se imprime la **longitud** con `len()`, se transforma a **mayúsculas** con `upper()` y se **reemplaza** la palabra `"Flamewall"` por `"Fairy Knife Hell"` con `replace()`.
- Se muestra la **cantidad de palabras** del mensaje original mediante la función que retorna el conteo.
- Se utilizan los métodos de strings (`upper`, `replace`, `split`) porque simplifican la transformación del texto y el conteo de palabras.

```python
def contar_palabras(mensaje):
    return len(mensaje.split())

mensaje = "Mi canción favorita es Flamewall, es también mi nivel favorito de Geometry Dash"
print("Longitud del mensaje:", len(mensaje))
print("En mayúsculas:", mensaje.upper())
print("Texto reemplazado:", mensaje.replace("Flamewall", "Fairy Knife Hell"))
print("Palabras totales:", contar_palabras(mensaje))
```
---