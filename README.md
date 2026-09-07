# Actividad 4 — Tabla de Pitágoras en Matriz

---

## Introducción

## Descripción de la actividad

Desarrollar una **aplicación en Python** que muestre una **tabla de Pitágoras interactiva** para facilitar la multiplicación de dos factores ingresados por el usuario. El programa debe almacenar la tabla en una **lista de listas (matriz)**, imprimirla en pantalla de forma ordenada y permitir que el usuario capture dos factores (renglón y columna) para obtener su producto consultando directamente la información almacenada en la matriz.

---

## Definiciones

Se define la función `construir_tabla(tamaño)` que genera la tabla de Pitágoras como una lista de listas. El ciclo `for` externo recorre los renglones y el ciclo `for` interno construye cada fila, agregándola a la matriz con `append()`.

```python
def construir_tabla(tamaño=10):
    tabla = []
    for renglon in range(1, tamaño + 1):
        fila = []
        for columna in range(1, tamaño + 1):
            fila.append(renglon * columna)
        tabla.append(fila)
    return tabla
```

---

## Función sin retorno de valor

La función `imprimir_tabla(tabla)` recorre la matriz y muestra cada fila con los números tabulados (`\t`). Al no usar `return`, la función solo imprime la tabla en pantalla.

```python
def imprimir_tabla(tabla):
    for fila in tabla:
        print("\t".join(str(numero) for numero in fila))
        
```
---

## Consultar factores

```python
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

```

---

## Programa principal

Se construye la matriz y se llama a la función sin valor para imprimir la tabla completa:

```python
tabla = construir_tabla()
print("Tabla de Pitagoras 10x10")
imprimir_tabla(tabla)
```

---

## Salidas esperadas

La siguiente salida muestra la tabla de Pitágoras sin corchetes ni comas, con cada número separado por tabulaciones:

![tabla](semana4/assets/cap1.png)

---

# Ejercicios Extras — Semana 4

Resolución de los 4 ejercicios extras evaluables de la actividad **Tabla de Pitágoras en Matriz**. Cada ejercicio documenta el procedimiento y la lógica aplicada, seguido del código correspondiente.

## Extra 1: Suma de todos los elementos de una matriz


- `suma_matriz(matriz)` **regresa valor** (con `return`): recorre cada fila con un ciclo `for` externo y cada elemento con un ciclo `for` anidado, acumulando la suma en una variable.
- `imprimir_matriz(matriz)` **no regresa valor**: imprime la matriz sin corchetes ni comas, mostrando cada elemento con `end=" "` para no saltar de línea y un `print()` vacío al final de cada fila.
- Se aplican ambas funciones a la matriz `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`.

```python 
def suma_matriz(matriz):
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total


def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
imprimir_matriz(matriz)
print(f"La suma de todos los elementos de la matriz es: {suma_matriz(matriz)}")
```

---

## Extra 2: Matriz con suma por fila


- `suma_fila(fila)` **regresa valor** (con `return`): acumula con un ciclo `for` la suma de los elementos de una lista.
- `mostrar_tabla(matriz)` **no regresa valor**: imprime la matriz sin corchetes ni comas.
- Con un ciclo `for` sobre los índices se imprime cada fila de la matriz y se llama a `suma_fila` para mostrar su total.

```python
def suma_fila(fila):
    total = 0
    for elemento in fila:
        total += elemento
    return total


def mostrar_tabla(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()


matriz = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
mostrar_tabla(matriz)
for i in range(len(matriz)):
    print(f"Suma de la fila {i}: {suma_fila(matriz[i])}")
```

---

## Extra 3: Producto de una columna sin usar el operador *


- `multiplicar_columna(matriz, columna)` **regresa valor** (con `return`).
- **Restricción:** dentro de la función está prohibido usar el operador `*`; el producto se calcula con **sumas repetidas**: por cada elemento de la columna se repite un ciclo que suma el resultado acumulado tantas veces como indique el elemento.
- Se pide al usuario el número de columna (`0`, `1` o `2`) y se muestra el resultado.

Elementos de la columna 1: `2`, `5`, `8` y `4` → producto `320`.

```python

def multiplicar_columna(matriz, columna):
    producto = 1
    for fila in matriz:
        suma = 0
        for i in range(fila[columna]):
            suma += producto
        producto = suma
    return producto


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 4, 6]]
columna = int(input("Numero de columna: "))
print(f"El producto de la columna {columna} es: {multiplicar_columna(matriz, columna)}")
```

---

## Extra 4: Tabla de Pitágoras de tamaño variable

- `generar_tabla(tamaño)` **regresa valor** (con `return`) una lista de listas `tamaño x tamaño`. Por cada renglón se usa un acumulador que se incrementa con el número del renglón (**sumas repetidas**), evitando el operador `*` dentro de la función de generación.
- `imprimir_tabla(tabla)` **no regresa valor**: imprime la tabla con los números tabulados (`\t`), sin corchetes ni comas.
- Se valida que el tamaño esté entre 2 y 5; si está fuera del rango, se muestra un mensaje de error.
- Se capturan un renglón y una columna y el producto se obtiene consultando `tabla[renglon - 1][columna - 1]`, sin usar `*`.

```python
def generar_tabla(tamano):
    tabla = []
    for renglon in range(1, tamano + 1):
        fila = []
        producto = 0
        for columna in range(1, tamano + 1):
            producto += renglon
            fila.append(producto)
        tabla.append(fila)
    return tabla


def imprimir_tabla(tabla):
    for fila in tabla:
        print("\t".join(str(numero) for numero in fila))


tamano = int(input("Tamaño de la tabla: "))
if 2 <= tamano <= 5:
    tabla = generar_tabla(tamano)
    imprimir_tabla(tabla)
    renglon = int(input("Renglon (factor): "))
    columna = int(input("Columna (factor): "))
    print(f"El producto de {renglon} x {columna} es: {tabla[renglon - 1][columna - 1]}")
else:
    print("Error, el tamaño debe estar entre 2 y 5.")
```
