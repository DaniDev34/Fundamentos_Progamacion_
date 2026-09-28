# Entrega Final del Proyecto (Fase II) — Sistema de Cotización de Internet Empresarial IENTC

En esta rama se documenta la versión final del proyecto (Fase II) para la **Actividad 7** del curso *Solución de problemas con programación computacional* (Temas 17, 18, 19 y 20). La solución completa se encuentra en el archivo `cotizacion.py`.

---

## Introducción

Esta documentación describe el diseño, el análisis y la implementación de un sistema de **cotización de planes de internet empresarial** para la empresa de telecomunicaciones **IENTC**, desarrollado en el archivo `cotizacion.py`.

La versión final del sistema conserva la lógica de negocio de la Fase I (catálogo de planes, descuentos por tipo de cliente y por plazo de contrato, condonación de la instalación, IVA y primer pago) e incorpora los cuatro temas de la semana: **escritura de archivos de texto**, **lectura de archivos de texto**, **integración de lectura y escritura** y **control de excepciones**. Además, el sistema aplica la **identificación del usuario**, una **bienvenida dinámica** construida con operadores de cadenas, una **pantalla de carga**, un **menú estructurado como matriz**, el **control de inactividad** mediante un ciclo `for` y un hilo de ejecución, y la **captura estructurada de la fecha en una tupla** que se integra automáticamente en cada archivo creado o modificado.

El objetivo de esta entrega es dejar documentado el diseño lógico del sistema y justificar, bloque por bloque, el cumplimiento de los diez requerimientos técnicos obligatorios de la actividad, de manera que el código pueda ser mantenido por terceros.

## Análisis organizacional

**IENTC Telecomunicaciones** (Ientc S. de R.L. de C.V.) es una empresa mexicana de telecomunicaciones fundada en 2011, autorizada como Red Pública de Telecomunicaciones por el IFT. Cuenta con aproximadamente **300 colaboradores** y una infraestructura de más de **25,000 kilómetros de fibra óptica** a nivel nacional, con interconexiones internacionales en Europa y Asia, así como seis centros de datos distribuidos en el país.

Su oferta de servicios se enfoca principalmente en el mercado empresarial: **internet de alta velocidad por fibra óptica**, telefonía fija, conectividad corporativa, servicios *carrier* y soluciones en la nube. La empresa diseña paquetes personalizados para cada cliente y garantiza un nivel de disponibilidad del 99.9%.

El área de impacto seleccionada es el **área comercial y de ventas**, que atiende a clientes corporativos que solicitan cotizaciones de planes de internet. Las cotizaciones actualmente se elaboran de forma manual, lo que provoca errores en la aplicación de descuentos, en el cálculo de la instalación y del IVA, así como demoras en la atención al cliente. A esta carencia se suma la falta de un histórico centralizado: cada atención termina con un monto impreso que no queda registrado, por lo que el área depende de archivos dispersos y no puede dar seguimiento a las negociaciones en curso.

## Definición del problema

La empresa necesita agilizar la elaboración de cotizaciones y reducir errores de cálculo al ofrecer sus planes de internet empresarial. El problema técnico a resolver es la **ausencia de una herramienta que estandarice el proceso de cotización**: el precio mensual, el costo de instalación, los descuentos por tipo de cliente y por plazo de contrato, y el IVA se calculan de forma manual dentro del área comercial.

A esta carencia se suma la **falta de persistencia de la información**: no existe un mecanismo que registre y recupere las cotizaciones atendidas, lo que impide construir una bitácora, reutilizar los datos de clientes ya atendidos o generar reportes de proyección de ventas.

La solución propuesta es un **sistema de cotización en consola** que reciba el plan elegido por el cliente, el plazo del contrato y su condición de cliente nuevo, y que entregue por pantalla un desglose detallado del primer pago y de la mensualidad, acumulando además las cotizaciones realizadas durante la sesión para apoyar la proyección de ventas del área. El sistema respalda cada operación en **archivos de texto externos** de la carpeta `datos/`, integra de forma automática la **fecha de operación** y el **usuario** responsable en cada archivo generado o modificado, y **suspende el menú** cuando detecta diez minutos de inactividad para proteger la sesión.

## Reglas de negocio

El sistema se rige por las siguientes reglas de negocio, delimitadas a partir de la operación actual del área comercial:

- Existen **cuatro planes base** de internet empresarial (100, 200, 500 y 1000 Mbps), cada uno con un precio mensual estandarizado.
- La **instalación** tiene un costo único de $1500; este se **condona** cuando el cliente firma un contrato de 12 o 24 meses.
- Los **clientes nuevos** reciben un **10% de descuento** sobre el precio mensual durante el primer semestre.
- Los clientes con contrato de **24 meses** reciben un **5% adicional** de descuento, el cual se suma al descuento anterior.
- Sobre la mensualidad ya descontada se aplica el **IVA del 16%**.
- El **primer pago** está formado por la mensualidad descontada, más su IVA, más el costo de instalación (si aplica).
- El sistema permite elaborar **múltiples cotizaciones** en una misma sesión y acumula los montos para generar un resumen al final.
- La **fecha de operación** se captura en formato `dia/mes/año` y se almacena en una tupla; se integra automáticamente en todo archivo de texto creado o anexado.
- La **bitácora de cotizaciones** se persiste en el archivo `cotizaciones_bitacora.txt` mediante anexado, conservando el historial de la sesión.
- El **menú se suspende** tras diez minutos sin interacción y solo se reanuda cuando el usuario responde expresamente `si`.
- El sistema **nunca sobrescribe** un archivo de texto existente: la creación exige un nombre libre y la escritura posterior se realiza por anexado.

## Requisitos funcionales

Para garantizar el funcionamiento completo del sistema se definen los siguientes requisitos funcionales:

1. El sistema debe solicitar el nombre o *nickname* del usuario al iniciar y elaborar un mensaje de bienvenida formal con operadores de cadenas.
2. El sistema debe mostrar una pantalla de carga de duración máxima de cinco segundos antes de habilitar el menú.
3. El sistema debe presentar el menú principal a partir de una **matriz** de filas y columnas, recorriendo la longitud de cada celda para alinear las columnas.
4. El sistema debe capturar la fecha de operación en formato `dia/mes/año` y almacenarla estrictamente en una **tupla**.
5. El sistema debe integrar la fecha de la tupla y el nombre del usuario en cada archivo de texto creado o modificado.
6. El sistema debe contar con cuatro o más **archivos de texto (.txt) de prueba** en la carpeta `datos/` y listarlos en un **diccionario** numerado para su lectura. La carpeta se crea automáticamente en la primera ejecución y se va poblando con las opciones 5 y 6 y con la bitácora de la opción 2, por lo que el inventario se construye siempre en tiempo de ejecución.
7. El sistema debe permitir leer, crear y anexar información en archivos de texto de forma permanente.
8. El sistema debe calcular la cotización aplicando descuentos, condonación de instalación, IVA y primer pago, y debe mostrar el desglose completo.
9. El sistema debe registrar en la bitácora las cotizaciones que el usuario decida guardar.
10. El sistema debe controlar con `try-except` los errores de ejecución (archivo inexistente, permisos, nombres inválidos e interrupciones del usuario) sin detenerse de forma abrupta.

## Requisitos no funcionales

Asimismo, el sistema debe cumplir con los siguientes requisitos no funcionales:

1. El sistema debe ser fácil de usar, mediante un menú sencillo y opciones claras en consola.
2. El sistema debe validar los datos ingresados, rechazando planes, plazos de contrato, fechas y respuestas no válidas e indicando el error al usuario.
3. El sistema debe ser eficiente, permitiendo elaborar varias cotizaciones en una misma sesión sin reiniciar el proceso.
4. El sistema debe separar las responsabilidades en funciones cortas y cohesionadas, con una única función de entrada (`main`).
5. El sistema debe ser seguro con los datos del usuario: no borra ni sobrescribe archivos existentes.
6. El sistema debe ser portable, utilizando solo la biblioteca estándar de Python (`os`, `threading`, `time`) sin dependencias externas.
7. El sistema debe ser mantenible, con un diseño documentado que facilite la ampliación a nuevos planes, reportes o consultas.

---

## Modelo Entrada-Proceso-Salida (EPS)

El sistema sigue el modelo **Entrada-Proceso-Salida**:

- **Entrada:** el nombre del usuario, la fecha de operación (`dia/mes/año`), la opción del menú, el número del plan (1-4), los meses de contrato (0, 12 o 24), la respuesta de si el cliente es nuevo (s/n), el nombre del archivo a leer, crear o anexar y su contenido.
- **Proceso:** validación cíclica de cada captura, selección del plan por índice, aplicación de descuentos acumulables, condonación de instalación, cálculo de la mensualidad, del IVA y del primer pago, acumulación de los totales de la sesión, recorrido de la matriz del menú y control de inactividad en un hilo paralelo.
- **Salida:** bienvenida dinámica, pantalla de carga, menú alineado, catálogo de planes, detalle de cada cotización, resumen de la sesión, listados de archivos y persistencia en archivos de texto con fecha y usuario.

## Clasificación de Datos

| Variable | Tipo de dato | Descripción |
| :--- | :--- | :--- |
| `usuario` | `str` | Nombre capturado al inicio, reimpreso en la bienvenida y en cada archivo generado. |
| `fecha` | `tuple[int, int, int]` | Fecha de operación `(dia, mes, anio)` obtenida de la captura validada. |
| `costo_instalacion` | `int` | Costo único de instalación en MXN (1500). |
| `iva` | `float` | Porcentaje de IVA (0.16). |
| `desc_bienvenida` | `float` | Descuento del 10% para clientes nuevos. |
| `desc_contrato_24` | `float` | Descuento adicional del 5% para contratos de 24 meses. |
| `velocidades` / `precios` | `list[int]` | Listas paralelas con la velocidad en Mbps y el precio mensual de cada plan. |
| `matriz_menu` | `list[list[str]]` | Matriz del menú: la primera fila son los encabezados y las siguientes las opciones. |
| `total_primeros_pagos` | `int` / `float` | Acumulador de primeros pagos; inicia en `0` y pasa a `float` al sumar. |
| `total_mensualidades` | `int` / `float` | Acumulador de mensualidades; inicia en `0` y pasa a `float` al sumar. |
| `num_cotizaciones` | `int` | Contador de cotizaciones realizadas en la sesión. |
| `segundos_inactividad` | `int` | Segundos máximos sin interacción antes de suspender (600). |
| `estado` | `dict[str, bool]` | Diccionario con las banderas `actividad` y `suspendido`. |
| `carpeta_datos` | `str` | Ruta de la carpeta de archivos de texto (`datos`). |
| `archivo_bitacora` | `str` | Nombre del archivo donde se anexa la bitácora de cotizaciones. |
| `pasos_carga` | `int` | Cantidad de pasos de la pantalla de carga (6). |
| `duracion_paso_carga` | `float` | Duración de cada paso de carga en segundos (0.5), para un total de 3 s. |
| `nombre`, `texto`, `seleccion`, `opcion`, `continuar`, `registro` | `str` | Cadenas capturadas del usuario mediante `input`. |
| `partes` | `list[str]` | Resultado de separar la fecha con `split("/")`. |
| `dia`, `mes`, `anio` | `int` | Componentes numéricos de la fecha de operación. |
| `titulo`, `borde` | `str` | Encabezado de la bienvenida y línea de separación calculada con multiplicación de cadenas. |
| `avance`, `paso`, `segundo`, `indice` | `int` | Contadores de los ciclos `for` y de la enumeración de archivos. |
| `ancho_opcion`, `ancho_descripcion` | `int` | Anchos de columna calculados recorriendo la matriz del menú. |
| `hilo` | `threading.Thread` | Hilo *daemon* que mide la inactividad mientras el menú espera la opción. |
| `clave`, `meses`, `numero` | `int` | Datos numéricos validados: plan, plazo e índice de archivo. |
| `velocidad_plan`, `precio_plan` | `int` | Datos del plan seleccionado mediante el índice `clave - 1`. |
| `nuevo` | `str` | Respuesta (s/n) de si el cliente es nuevo. |
| `descuento`, `instalacion`, `mensualidad`, `iva_aplicado`, `primer_pago` | `int` / `float` | Resultados del proceso de cobro; se muestran con `round(..., 2)`. |
| `disponibles` | `dict[int, str]` | Diccionario que numera los archivos `.txt` disponibles para lectura. |
| `nombres` | `list[str]` | Listado ordenado de los archivos contenidos en la carpeta de datos. |
| `nombre_archivo`, `contenido`, `detalle` | `str` | Nombre y texto a persistir en los archivos de texto. |
| `resultado` | `str` | Bandera de retorno del menú (`salir` o `inicio`) que decide el fin del programa. |
| `error` | `Exception` | Excepción capturada en el manejador general del programa. |

## Operadores del Lenguaje

**Operadores matemáticos:**
- `*` para calcular el monto del descuento y el IVA (`precio_plan * desc_bienvenida`, `mensualidad * iva`), el porcentaje de avance de la carga (`100 // pasos_carga` y `paso * avance`) y la duración total de la pantalla de carga.
- `-` para restar el descuento del precio base y obtener la mensualidad con descuento, y para decrementar el contador de la cuenta regresiva de inactividad.
- `+` para sumar mensualidad, IVA e instalación, para acumular los totales de la sesión, para concatenar cadenas en la bienvenida, en el detalle de la cotización y en la bitácora, y para sumar `1` al índice numerado de archivos.
- `//` para repartir el porcentaje de avance entre los pasos de carga sin decimales.

**Operadores relacionales:**
- `clave >= 1 and clave <= 4` para validar que el plan elegido exista dentro del catálogo.
- `meses == 0 or meses == 12 or meses == 24` para validar el plazo del contrato.
- `meses >= 12` para definir si la instalación queda condonada.
- `meses == 24` y `nuevo.lower() == "s"` para decidir qué descuentos se aplican.
- `segundo % 60 == 0 and segundo < segundos_inactividad` para avisar cada minuto restante de inactividad.
- `os.path.isdir(...) == False`, `os.path.exists(...) == True` y `nombre.lower().endswith(".txt") == True` para validar la carpeta, la existencia del archivo y su extensión.
- `dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1900 or anio > 2100` para validar los rangos de la fecha.

**Operadores lógicos:**
- `and` para exigir dos condiciones a la vez en la validación del plan y del aviso de inactividad.
- `or` para permitir varios valores válidos en la validación del plazo del contrato y en la reanudación de la sesión (`continuar == "si" or continuar == "no"`).
- `numero in disponibles` para resolver si la captura corresponde a un índice numerado de la lista de archivos.

**Operadores y métodos de cadena:**
- Concatenación con `+` y multiplicación con `*` (`"=" * len(titulo)` y `"-" * (ancho_opcion + ancho_descripcion + 3)`) para construir los bordes de la interfaz.
- `.strip()` para eliminar espacios, `.lower()` para comparar sin distinguir mayúsculas, `.upper()` para el perfil de atención, `.split("/")` para descomponer la fecha, `.ljust(ancho + 2)` para alinear las columnas de la matriz y `.endswith(".txt")` para filtrar los archivos válidos.
- Conversión de tipos con `str()`, `int()` y `len()`, y redondeo con `round(..., 2)` en cada importe mostrado.

## Estructuras de Control

**Estructuras condicionales:**
- `if/elif/else`: dirigen el menú principal, validan la clave del plan y el plazo del contrato, deciden la condonación de la instalación, aplican los descuentos según el cliente y el plazo, y controlan las siete opciones del menú.
- `if` con `raise ValueError`: rechazan la fecha cuando el formato es incorrecto o los rangos de día, mes y año no son válidos.
- `try/except`: capturan `ValueError` en las capturas numéricas, `OSError` y `UnicodeDecodeError` en la persistencia, y `KeyboardInterrupt`, `EOFError` y `Exception` en el bloque principal.

**Estructuras iterativas:**
- `while True` (menú principal): mantiene el programa activo hasta que el usuario selecciona la opción de salir o decide regresar a la pantalla de inicio.
- `while True` de validación: solicita repetidamente el nombre, la fecha, el plan, el plazo o la reanudación de la sesión hasta que el valor ingresado sea válido.
- `for` con `range` en `pantalla_carga`: recorre los seis pasos del indicador de progreso.
- `for` con `range` en `ver_catalogo` y `ver_cotizacion`: recorre la longitud de las listas de velocidades y precios.
- `for` con `range` en `imprimir_menu` y `listar_archivos`: recorren la matriz del menú y el listado ordenado de archivos.
- `for` con `range` en `inactividad`: es el ciclo `for` exigido por la actividad para medir los diez minutos de inactividad, verificados segundo a segundo con `time.sleep(1)`.
- `for nombre in nombres`: recorre los archivos existentes para numerarlos en el diccionario `disponibles`.

**Otras estructuras:**
- Sentencia `with` en las operaciones de archivo de `leer_archivo`, `crear_archivo` y `anexar_datos`, que garantiza el cierre automático del archivo incluso si ocurre un error.
- `threading.Thread` con `daemon = True` y `join()`: ejecuta la medición de inactividad en paralelo y la sincroniza antes de decidir si la sesión fue suspendida.

---

## Arquitectura del programa

El archivo `cotizacion.py` está organizado en bloques funcionales que separan las responsabilidades del sistema:

| Bloque | Elementos | Responsabilidad |
| :--- | :--- | :--- |
| Configuración | Constantes, listas del catálogo, acumuladores, `estado`, rutas y parámetros de carga | Centralizar los valores del negocio y los parámetros de la interfaz. |
| Captura de sesión | `pedir_nombre`, `capturar_fecha`, `fecha_texto` | Identificar al usuario y registrar la fecha en una tupla. |
| Presentación | `bienvenida`, `pantalla_carga`, `imprimir_menu`, `ver_catalogo` | Generar la salida formal del sistema. |
| Control de inactividad | `inactividad`, `esperar_opcion` | Medir el tiempo sin interacción y suspender el menú. |
| Persistencia | `preparar_carpeta`, `listar_archivos`, `mostrar_archivos`, `leer_archivo`, `crear_archivo`, `anexar_datos`, `escribir_archivo`, `anexar_archivo` | Administrar los archivos de texto de la carpeta `datos/`. |
| Lógica de negocio | `ver_cotizacion`, `ver_resumen` | Calcular la cotización y acumular los totales de la sesión. |
| Navegación | `menu_principal`, `main` | Dirigir las opciones del menú y el ciclo de vida del programa. |
| Seguridad del programa | Bloque `try/except` del final del archivo | Cerrar el programa de forma controlada ante cualquier excepción. |

---

## Documentación del código - `cotizacion.py`

### 1. Configuración general del programa

El archivo comienza importando únicamente módulos de la **biblioteca estándar**, lo que cumple el requisito de portabilidad sin dependencias externas. `os` permite el manejo de carpetas y archivos, `threading` ejecuta la medición de inactividad en paralelo al menú y `time` controla las pausas de la pantalla de carga.

```python
import os
import threading
import time
```

A continuación se declaran las constantes del negocio (costo de instalación, IVA y porcentajes de descuento) y el catálogo de planes mediante dos listas paralelas que se recorren con `for`:

```python
costo_instalacion = 1500
iva = 0.16
desc_bienvenida = 0.10
desc_contrato_24 = 0.05

velocidades = [100, 200, 500, 1000]
precios = [849, 1299, 2499, 3999]
```

Los acumuladores de la sesión inician en cero y se actualizan con cada cotización realizada:

```python
total_primeros_pagos = 0
total_mensualidades = 0
num_cotizaciones = 0
```

El estado de la sesión se controla con un **diccionario de banderas** compartido entre el hilo del menú y el hilo de inactividad, junto con los parámetros de la cuenta regresiva:

```python
usuario = ""
fecha = (0, 0, 0)

segundos_inactividad = 600
estado = {"actividad": True, "suspendido": False}
```

Finalmente se definen la carpeta de trabajo, el nombre de la bitácora y los parámetros de la pantalla de carga. Con `pasos_carga = 6` y `duracion_paso_carga = 0.5` la pausa total es de **3 segundos**, dentro del máximo de 5 segundos exigido por la actividad:

```python
carpeta_datos = "datos"
archivo_bitacora = "cotizaciones_bitacora.txt"

pasos_carga = 6
duracion_paso_carga = 0.5
```

### 2. Menú principal como matriz

El menú se declara como una **matriz de dos columnas**: la primera fila contiene los encabezados `Opcion` y `Descripcion`, y cada fila siguiente es una opción del sistema. Esta representación cumple el requerimiento de presentar las opciones del menú en forma de matriz:

```python
matriz_menu = [
    ["Opcion", "Descripcion"],
    ["1", "Ver catalogo de planes"],
    ["2", "Realizar una cotizacion"],
    ["3", "Ver resumen de cotizaciones"],
    ["4", "Leer archivo de texto"],
    ["5", "Crear archivo de texto"],
    ["6", "Anexar datos a un archivo"],
    ["7", "Salir"],
]
```

### 3. Identificación del usuario

La función `pedir_nombre` solicita la identificación del usuario mediante `input`, aplica `.strip()` para descartar espacios y usa un `while True` de validación que solo termina cuando la cadena no está vacía:

```python
def pedir_nombre():
    while True:
        nombre = input("\n Ingresa tu nombre: ").strip()
        if nombre != "":
            return nombre
        print("El nombre no puede quedar vacio.")
```

### 4. Captura estructurada de la fecha en tupla

La función `capturar_fecha` es la implementación directa del requerimiento de fecha estructurada. Separa la captura con `split("/")`, exige **exactamente tres partes**, convierte cada componente con `int()` y valida los rangos permitidos (día de 1 a 31, mes de 1 a 12, año de 1900 a 2100). Cualquier falla lanza `ValueError`, que el `except` atrapa para volver a preguntar. El valor almacenado es la **tupla** `fecha = (dia, mes, anio)`, declarada con `global` para que las funciones de archivos puedan consultarla:

```python
def capturar_fecha():
    global fecha
    while True:
        try:
            texto = input("Ingresa la fecha de operacion (dia/mes/año, ej. 12/06/2026): ").strip()
            partes = texto.split("/")
            if len(partes) != 3:
                raise ValueError
            dia = int(partes[0])
            mes = int(partes[1])
            anio = int(partes[2])
            if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1900 or anio > 2100:
                raise ValueError
            fecha = (dia, mes, anio)
            print("Fecha de operacion registrada: fecha =", fecha)
            return
        except ValueError:
            print("La fecha debe tener el formato dia/mes/año, por ejemplo 12/06/2026.")
```

### 5. Formato de la fecha en texto

La función `fecha_texto` convierte la tupla en una cadena con formato `dia/mes/año`, completando con cero a la izquierda los componentes de un solo dígito. Es la forma en que la tupla se integra en la bienvenida y en los archivos de texto:

```python
def fecha_texto():
    dia = str(fecha[0])
    mes = str(fecha[1])
    anio = str(fecha[2])
    if len(dia) == 1:
        dia = "0" + dia
    if len(mes) == 1:
        mes = "0" + mes
    return dia + "/" + mes + "/" + anio
```

### 6. Bienvenida dinámica

La función `bienvenida` arma el encabezado del sistema calculando el borde con multiplicación de cadenas (`"=" * len(titulo)`) e incorpora el **nombre del usuario** mediante concatenación con `+`. También usa `.upper()` para el perfil de atención e inserta la fecha obtenida de la tupla con `fecha_texto()`, cumpliendo el requerimiento de bienvenida dinámica:

```python
def bienvenida():
    titulo = "IENTC - Sistema de cotización empresarial"
    borde = "=" * len(titulo)
    print("\n" + borde)
    print(titulo)
    print(borde)
    print("\nEstimado usuario " + usuario + ", le damos la bienvenida al sistema IENTC.")
    print("Su sesion quedo registrada en la fecha" + fecha_texto() + " por el area comercial de IENTC.")
    print("Perfil: " + usuario.upper() + " | Estatus: Activo")
    print("Aquí puede consultar el catalogo, generar cotizaciones y administrar sus archivos de texto.")
    print(borde)
```

### 7. Pantalla de carga

La función `pantalla_carga` es la **función dedicada** exigida por la actividad. Calcula el porcentaje de avance con división entera (`100 // pasos_carga`), imprime el aviso de inicio y recorre los seis pasos con `for`, actualizando la barra en la misma línea mediante `\r`, `end=""` y `flush=True`, y pausa `duracion_paso_carga` segundos en cada paso:

```python
def pantalla_carga():
    avance = 100 // pasos_carga
    print("\n --- Iniciando el sistema, por favor espere...")
    for paso in range(1, pasos_carga + 1):
        print("\rCargando modulos " + "." * paso + " " + str(paso * avance) + "%", end="", flush=True)
        time.sleep(duracion_paso_carga)
    print("\rSistema operativo al 100%. Carga completada en " + str(pasos_carga * duracion_paso_carga) + " segundos.      ")
```

### 8. Presentación alineada de la matriz del menú

La función `imprimir_menu` recorre la matriz **dos veces**: la primera con `for` determina el ancho de cada columna comparando `len()` de las celdas, y la segunda imprime cada fila usando `ljust(ancho + 2)` para alinear la columna de opciones. Finalmente dibuja una línea de separación con multiplicación de cadenas:

```python
def imprimir_menu():
    print("\n ----- IENTC - Cotizador de Internet  ----- ")
    ancho_opcion = 0
    ancho_descripcion = 0
    for fila in matriz_menu:
        if len(fila[0]) > ancho_opcion:
            ancho_opcion = len(fila[0])
        if len(fila[1]) > ancho_descripcion:
            ancho_descripcion = len(fila[1])
    for fila in matriz_menu:
        print(fila[0].ljust(ancho_opcion + 2) + fila[1])
    print("-" * (ancho_opcion + ancho_descripcion + 3))
```

### 9. Control de inactividad con ciclo `for`

La función `inactividad` es el **control de inactividad del usuario** solicitado con un ciclo `for`. Recorre los `segundos_inactividad` (600) en orden descendente y sale de inmediato (`return`) si la bandera `actividad` pasa a `False`, es decir, cuando el usuario ya eligió una opción. Cuando el contador llega a un minuto exacto, muestra un aviso; si el ciclo concluye sin interacción, marca `suspendido` en el diccionario `estado`:

```python
def inactividad():
    for segundo in range(segundos_inactividad, 0, -1):
        if estado["actividad"] == False:
            return
        if segundo % 60 == 0 and segundo < segundos_inactividad:
            print("\nSesion sin interaccion. El menu se suspendera en " + str(segundo // 60) + " minuto(s).")
        time.sleep(1)
    estado["actividad"] = False
    estado["suspendido"] = True
    print("\n*** Se detectaron 10 minutos de inactividad, el menu fue suspendido ***")
```

### 10. Integración del control de inactividad con el menú

La función `esperar_opcion` es el puente entre el menú y el hilo de inactividad: marca la sesión como activa, crea un `threading.Thread` con `target=inactividad`, lo declara `daemon` para que no bloquee el cierre del programa y lo inicia con `start()`. El `input` queda en el hilo principal, de modo que el reloj de inactividad avanza en paralelo. Al recibir la respuesta, marca `actividad = False` y ejecuta `hilo.join()` para **sincronizar** con el hilo antes de decidir el valor devuelto: si la sesión fue suspendida retorna `"suspendido"`, en caso contrario retorna la opción capturada:

```python
def esperar_opcion():
    estado["actividad"] = True
    estado["suspendido"] = False
    hilo = threading.Thread(target=inactividad)
    hilo.daemon = True
    hilo.start()
    opcion = input("Selecciona una opcion: ")
    estado["actividad"] = False
    hilo.join()
    if estado["suspendido"] == True:
        return "suspendido"
    return opcion.strip()
```

### 11. Catálogo de planes

La función `ver_catalogo` recorre las listas paralelas con `for` sobre `len(velocidades)` y muestra cada plan numerado, con su velocidad en Mbps y su precio mensual:

```python
def ver_catalogo():
    print("\n--- Catalogo de planes ---")
    for i in range(len(velocidades)):
        print("  " + str(i + 1) + ".- " + str(velocidades[i]) + " Mbps  -  $" + str(precios[i]) + " / mes")
```

### 12. Persistencia: preparación de la carpeta e inventario de archivos

La función `preparar_carpeta` garantiza que la carpeta `datos/` exista antes de cualquier operación, creándola con `os.makedirs` únicamente cuando `os.path.isdir` devuelve `False`:

```python
def preparar_carpeta():
    if os.path.isdir(carpeta_datos) == False:
        os.makedirs(carpeta_datos)
```

La función `listar_archivos` construye el **diccionario de archivos disponibles** exigido por el requerimiento de persistencia. Obtiene el listado con `os.listdir`, lo ordena con `sorted`, filtra únicamente los nombres terminados en `.txt` y asigna un índice numerado consecutivo a cada archivo. Todo el recorrido está protegido por `try/except OSError`:

```python
def listar_archivos():
    disponibles = {}
    try:
        preparar_carpeta()
        nombres = sorted(os.listdir(carpeta_datos))
        indice = 0
        for nombre in nombres:
            if nombre.lower().endswith(".txt") == True:
                indice = indice + 1
                disponibles[indice] = nombre
    except OSError:
        print("No fue posible revisar los archivos disponibles.")
    return disponibles
```

La función `mostrar_archivos` imprime el diccionario con el formato `indice.- nombre`, que es el formato que el usuario verá y que después podrá capturar para elegir un archivo:

```python
def mostrar_archivos(disponibles):
    print("\n--- Archivos de texto disponibles ---")
    for indice in disponibles:
        print("  " + str(indice) + ".- " + disponibles[indice])
```

### 13. Persistencia: lectura de archivos de texto

La función `leer_archivo` implementa la lectura de archivos. Si el diccionario llega vacío, informa que no hay archivos disponibles. Si no, muestra el listado y entra en un `while True` que acepta **el nombre del archivo o su índice numerado**: primero valida el nombre con `os.path.isfile`, y si no coincide intenta convertir la captura con `int()` para buscar la clave en el diccionario. Cuando el archivo está localizado, lo abre con la sentencia `with` en modo `"r"` y `encoding="utf-8"`, y controla `OSError` y `UnicodeDecodeError` con mensajes amigables que evitan que el programa se detenga:

```python
def leer_archivo():
    disponibles = listar_archivos()
    if len(disponibles) == 0:
        print("No hay archivos de texto disponibles para lectura.")
        return
    mostrar_archivos(disponibles)
    while True:
        seleccion = input("Ingresa el nombre del archivo que deseas abrir: ").strip()
        if seleccion == "":
            continue
        if os.path.isfile(os.path.join(carpeta_datos, seleccion)) == True:
            nombre_archivo = seleccion
            break
        try:
            numero = int(seleccion)
        except ValueError:
            numero = 0
        if numero in disponibles:
            nombre_archivo = disponibles[numero]
            break
        print("" + seleccion + "' no esta disponible. Revisa el nombre capturado.")
    try:
        with open(os.path.join(carpeta_datos, nombre_archivo), "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError:
        print("Ni se pudo leer '" + nombre_archivo + "', revisa que exista en la carpeta de datos.")
        return
    except UnicodeDecodeError:
        print("El archivo'" + nombre_archivo + "' contiene caracteres no compatibles con la lectura.")
        return
    print("\n--- Contenido de " + nombre_archivo + " ---")
    if contenido.strip() == "":
        print("El archivo no contiene informacion.")
    else:
        print(contenido)
```

### 14. Persistencia: creación de archivos de texto

La función `crear_archivo` es la base de la escritura. Si el nombre no termina en `.txt`, lo agrega; después verifica con `os.path.exists` que el archivo **no exista**, y en caso contrario rechaza la operación para proteger la información previa del usuario. Dentro del `try`, escribe con la sentencia `with` en modo `"w"` un encabezado con el nombre del archivo, la **fecha de la tupla** y el **usuario**, y devuelve `True` o `False` según el resultado:

```python
def crear_archivo(nombre_archivo, contenido):
    if nombre_archivo.lower().endswith(".txt") == False:
        nombre_archivo = nombre_archivo + ".txt"
    if os.path.exists(os.path.join(carpeta_datos, nombre_archivo)) == True:
        print("Error: '" + nombre_archivo + "' ya existe, elige otro nombre para no sobrescribirlo.")
        return False
    try:
        preparar_carpeta()
        with open(os.path.join(carpeta_datos, nombre_archivo), "w", encoding="utf-8") as archivo:
            archivo.write("=== IENTC - Cotizador de Internet ===\n")
            archivo.write("Archivo: " + nombre_archivo + "\n")
            archivo.write("Fecha de operacion: " + fecha_texto() + "\n")
            archivo.write("Usuario: " + usuario + "\n")
            archivo.write("--------------------------------------\n")
            archivo.write(contenido + "\n")
        print("Archivo creado correctamente: " + nombre_archivo)
        return True
    except OSError:
        print("Falló la creacion de '" + nombre_archivo + "', prueba de nuevo.")
        return False
```

### 15. Persistencia: anexado de datos

La función `anexar_datos` opera en modo `"a"`, por lo que nunca destruye el contenido previo. Calcula `nuevo` con `os.path.exists` para saber si el archivo se crea en este momento; si es así, escribe primero el encabezado del sistema. Toda la escritura está protegida por `try/except OSError` e incluye la fecha de operación y el usuario en cada bloque anexado:

```python
def anexar_datos(nombre_archivo, contenido):
    if nombre_archivo.lower().endswith(".txt") == False:
        nombre_archivo = nombre_archivo + ".txt"
    try:
        preparar_carpeta()
        nuevo = os.path.exists(os.path.join(carpeta_datos, nombre_archivo)) == False
        with open(os.path.join(carpeta_datos, nombre_archivo), "a", encoding="utf-8") as archivo:
            if nuevo == True:
                archivo.write("----- IENTC - Cotizador de Internet -----\n")
            archivo.write("\nFecha de operacion: " + fecha_texto() + "\n")
            archivo.write("Usuario: " + usuario + "\n")
            archivo.write(contenido + "\n")
        print("Datos anexados en: " + nombre_archivo)
        return True
    except OSError:
        print("Falló el anexado en '" + nombre_archivo + "', prueba de nuevo.")
        return False
```

### 16. Opciones de menú para crear y anexar archivos

La función `escribir_archivo` es la opción 5 del menú: lista los archivos existentes para que el usuario vea el contexto, pide el nombre del archivo nuevo (**cancela la operación** si queda vacío), solicita el contenido y delega la escritura en `crear_archivo`:

```python
def escribir_archivo():
    disponibles = listar_archivos()
    if len(disponibles) > 0:
        mostrar_archivos(disponibles)
    nombre_archivo = input("Nombre del archivo nuevo (se agregara la extension .txt): ").strip()
    if nombre_archivo == "":
        print("Operacion cancelada.")
        return
    contenido = input("Contenido que se guardara en el archivo: ")
    crear_archivo(nombre_archivo, contenido)
```

La función `anexar_archivo` es la opción 6: exige que exista al menos un archivo, muestra el listado numerado, permite capturar el nombre o el índice (`numero in disponibles`) y anexa los datos mediante `anexar_datos`:

```python
def anexar_archivo():
    disponibles = listar_archivos()
    if len(disponibles) == 0:
        print("No hay archivos de texto disponibles para anexar datos.")
        return
    mostrar_archivos(disponibles)
    nombre_archivo = input("Nombre del archivo al que se anexaran los datos: ").strip()
    if nombre_archivo == "":
        print("Operacion cancelada.")
        return
    try:
        numero = int(nombre_archivo)
    except ValueError:
        numero = 0
    if numero in disponibles:
        nombre_archivo = disponibles[numero]
    contenido = input("Datos que se anexaran al archivo: ")
    anexar_datos(nombre_archivo, contenido)
```

### 17. Cotización de un plan

La función `ver_cotizacion` concentra el modelo EPS del sistema. Primero **imprime** el catálogo y después captura con `while True` y `try/except ValueError` el plan (1 a 4) y los meses de contrato (0, 12 o 24), de modo que cualquier dato no numérico o fuera de rango provoque un nuevo intento. El índice del catálogo se obtiene con `clave - 1` sobre las listas paralelas.

El núcleo del cálculo aplica las reglas de negocio: descuento del 10% a clientes nuevos, 5% adicional para contratos de 24 meses (acumulables), condonación de la instalación desde 12 meses, IVA sobre la mensualidad ya descontada y primer pago como suma de los tres conceptos:

```python
    descuento = 0
    if nuevo.lower() == "s":
        descuento = precio_plan * desc_bienvenida

    if meses == 24:
        descuento = descuento + precio_plan * desc_contrato_24

    instalacion = costo_instalacion
    if meses >= 12:
        instalacion = 0

    mensualidad = precio_plan - descuento
    iva_aplicado = mensualidad * iva
    primer_pago = mensualidad + iva_aplicado + instalacion
```

Al terminar el detalle en pantalla, la función actualiza los **acumuladores de la sesión** mediante `global`:

```python
    total_primeros_pagos = total_primeros_pagos + primer_pago
    total_mensualidades = total_mensualidades + mensualidad
    num_cotizaciones = num_cotizaciones + 1
```

Por último, si el usuario responde `si`, la cotización se resume en la cadena `detalle` y se persiste en la **bitácora** mediante `anexar_datos`, lo que satisface el requerimiento de archivo de texto generado automáticamente:

```python
    registro = input("\nDeseas registrar esta cotizacion? (si/no): ").strip().lower()
    if registro == "si":
        detalle = (
            "Cotizacion #" + str(num_cotizaciones)
            + " | Plan: " + str(velocidad_plan) + " Mbps"
            + " | Precio base: $" + str(precio_plan)
            + " | Descuento: -$" + str(round(descuento, 2))
            + " | Mensualidad: $" + str(round(mensualidad, 2))
            + " | IVA: $" + str(round(iva_aplicado, 2))
            + " | Instalacion: $" + str(round(instalacion, 2))
            + " | Primer pago: $" + str(round(primer_pago, 2))
            + " | Contrato: " + str(meses) + " meses\n"
        )
        anexar_datos(archivo_bitacora, detalle)
```

La función completa es:

```python
def ver_cotizacion():
    global total_primeros_pagos
    global total_mensualidades
    global num_cotizaciones
    print("\n--- Nueva cotizacion ---")
    for i in range(len(velocidades)):
        print("  " + str(i + 1) + ". " + str(velocidades[i]) + " Mbps  -  $" + str(precios[i]) + " / mes")

    while True:
        try:
            clave = int(input("Elige el plan (1-4): "))
        except ValueError:
            print("Error, debes ingresar un numero entero, intenta de nuevo.")
            continue
        if clave >= 1 and clave <= 4:
            break
        print("Error, plan no valido, intenta de nuevo.")

    indice = clave - 1
    velocidad_plan = velocidades[indice]
    precio_plan = precios[indice]

    while True:
        try:
            meses = int(input("Meses de contrato (0, 12 o 24): "))
        except ValueError:
            print("Error: solo se aceptan numeros enteros.")
            continue
        if meses == 0 or meses == 12 or meses == 24:
            break
        print("Error: solo se aceptan contratos de 0, 12 o 24 meses.")

    nuevo = input("Es cliente nuevo? (s/n): ")

    descuento = 0
    if nuevo.lower() == "s":
        descuento = precio_plan * desc_bienvenida

    if meses == 24:
        descuento = descuento + precio_plan * desc_contrato_24

    instalacion = costo_instalacion
    if meses >= 12:
        instalacion = 0

    mensualidad = precio_plan - descuento
    iva_aplicado = mensualidad * iva
    primer_pago = mensualidad + iva_aplicado + instalacion

    print("\n---------- Detalles de cotizacion ----------")
    print("Plan seleccionado:     " + str(velocidad_plan) + " Mbps")
    print("Precio base mensual:  $" + str(precio_plan))
    print("Descuento:           -$" + str(round(descuento, 2)))
    print("Mensualidad:          $" + str(round(mensualidad, 2)))
    print("IVA (16%):            $" + str(round(iva_aplicado, 2)))
    print("Instalacion:          $" + str(round(instalacion, 2)))
    print("Primer pago total:    $" + str(round(primer_pago, 2)))
    if meses > 0:
        print("Contrato firmado por:     " + str(meses) + " meses")

    total_primeros_pagos = total_primeros_pagos + primer_pago
    total_mensualidades = total_mensualidades + mensualidad
    num_cotizaciones = num_cotizaciones + 1

    registro = input("\nDeseas registrar esta cotizacion? (si/no): ").strip().lower()
    if registro == "si":
        detalle = (
            "Cotizacion #" + str(num_cotizaciones)
            + " | Plan: " + str(velocidad_plan) + " Mbps"
            + " | Precio base: $" + str(precio_plan)
            + " | Descuento: -$" + str(round(descuento, 2))
            + " | Mensualidad: $" + str(round(mensualidad, 2))
            + " | IVA: $" + str(round(iva_aplicado, 2))
            + " | Instalacion: $" + str(round(instalacion, 2))
            + " | Primer pago: $" + str(round(primer_pago, 2))
            + " | Contrato: " + str(meses) + " meses\n"
        )
        anexar_datos(archivo_bitacora, detalle)
```

### 18. Resumen de cotizaciones

La función `ver_resumen` (opción 3) muestra los tres acumuladores de la sesión con dos decimales gracias a `round(..., 2)`:

```python
def ver_resumen():
    print("\n---------- Resumen de cotizaciones ----------")
    print("Cotizaciones realizadas:  " + str(num_cotizaciones))
    print("Total de primeros pagos:  $" + str(round(total_primeros_pagos, 2)))
    print("Total de mensualidades:    $" + str(round(total_mensualidades, 2)))
```

### 19. Menú principal con ciclo `while`

La función `menu_principal` es el ciclo `while True` exigido por la actividad. Imprime la matriz, obtiene la opción mediante `esperar_opcion` y primero resuelve el caso de inactividad: si la opción es `"suspendido"`, exige una respuesta exacta de `si` o `no`; con `si` el menú se reanuda mediante `continue` y con `no` se retorna `"inicio"` para regresar a la pantalla de inicio. Después, la cadena `if/elif/else` dirige las siete opciones del sistema:

```python
def menu_principal():
    while True:
        imprimir_menu()
        opcion = esperar_opcion()
        if opcion == "suspendido":
            while True:
                continuar = input("Deseas continuar en el menu? (si/no): ").strip().lower()
                if continuar == "si" or continuar == "no":
                    break
                print("Error, responde exactamente usando 'si' o 'no'.")
            if continuar == "si":
                print("Sesion reanudada, regresarás al menu principal.")
                continue
            print("Regresando a la pantalla de inicio del programa.")
            return "inicio"
        if opcion == "1":
            ver_catalogo()
        elif opcion == "2":
            ver_cotizacion()
        elif opcion == "3":
            ver_resumen()
        elif opcion == "4":
            leer_archivo()
        elif opcion == "5":
            escribir_archivo()
        elif opcion == "6":
            anexar_archivo()
        elif opcion == "7":
            return "salir"
        else:
            print("Opcion no valida, intenta de nuevo.")
```

### 20. Función principal y control de excepciones

La función `main` declara `global usuario` y ejecuta el **ciclo de vida de la sesión**: pide el nombre, captura la fecha, muestra la bienvenida, lanza la pantalla de carga y entra al menú. Si el menú devuelve `"salir"` el programa agradece y termina con `return`; cualquier otro retorno (por ejemplo `"inicio"`) reinicia el ciclo de sesión:

```python
def main():
    global usuario
    while True:
        usuario = pedir_nombre()
        capturar_fecha()
        bienvenida()
        pantalla_carga()
        resultado = menu_principal()
        if resultado == "salir":
            print("Gracias por usar el programa.")
            return
```

Finalmente, el bloque `try/except` a nivel de módulo cumple el requerimiento de control de excepciones del sistema. `KeyboardInterrupt` y `EOFError` cierran el programa de forma segura cuando el usuario interrumpe o termina la entrada, y `Exception` como excepción genérica captura cualquier falla inesperada informando el mensaje del error:

```python
try:
    main()
except KeyboardInterrupt:
    print("\n\n Iterrupción del usuario, se cerrará el programa.")
except EOFError:
    print("\n\n Fin de la entrada de datos, el programa se cerrará.")
except Exception as error:
    print("\nError inesperado:", error)
    print("El programa se cerrará, revise los archivos e intentelo de nuevo.")
```

---

## Mapa de funciones

| Función | Parámetros | Retorno | Propósito |
| :--- | :--- | :--- | :--- |
| `pedir_nombre` | Ninguno | `str` | Solicita y valida la identificación del usuario. |
| `fecha_texto` | Ninguno | `str` | Convierte la tupla `fecha` en texto `dia/mes/año`. |
| `capturar_fecha` | Ninguno | `None` | Captura y valida la fecha, almacenándola en la tupla `fecha`. |
| `bienvenida` | Ninguno | `None` | Genera el mensaje formal con el usuario y la fecha. |
| `pantalla_carga` | Ninguno | `None` | Muestra la barra de progreso de la carga del sistema. |
| `imprimir_menu` | Ninguno | `None` | Calcula los anchos de columna e imprime la matriz del menú. |
| `inactividad` | Ninguno | `None` | Ciclo `for` que mide los 600 segundos de inactividad. |
| `esperar_opcion` | Ninguno | `str` | Captura la opción en paralelo al hilo de inactividad. |
| `ver_catalogo` | Ninguno | `None` | Lista los cuatro planes disponibles. |
| `preparar_carpeta` | Ninguno | `None` | Crea la carpeta `datos/` si no existe. |
| `listar_archivos` | Ninguno | `dict[int, str]` | Arma el diccionario numerado de archivos `.txt`. |
| `mostrar_archivos` | `disponibles` | `None` | Imprime el listado de archivos disponibles. |
| `leer_archivo` | Ninguno | `None` | Localiza y muestra el contenido de un archivo de texto. |
| `crear_archivo` | `nombre_archivo`, `contenido` | `bool` | Crea un archivo `.txt` nuevo con encabezado, fecha y usuario. |
| `anexar_datos` | `nombre_archivo`, `contenido` | `bool` | Anexa datos al final de un archivo, creándolo si hace falta. |
| `escribir_archivo` | Ninguno | `None` | Opción 5: solicita nombre y contenido, y crea el archivo. |
| `anexar_archivo` | Ninguno | `None` | Opción 6: solicita archivo e información a anexar. |
| `ver_cotizacion` | Ninguno | `None` | Opción 2: ejecuta el proceso EPS completo de la cotización. |
| `ver_resumen` | Ninguno | `None` | Opción 3: muestra los acumuladores de la sesión. |
| `menu_principal` | Ninguno | `str` | Ciclo `while` que dirige las opciones y la reanudación por inactividad. |
| `main` | Ninguno | `None` | Ciclo de vida de la sesión y punto de entrada al programa. |

## Carpeta de datos y archivos de texto

La persistencia trabaja sobre la carpeta `datos/`, cuya ruta se define en la constante `carpeta_datos`. **La carpeta no forma parte del repositorio**: el sistema la crea automáticamente la primera vez que se necesita, porque las funciones `preparar_carpeta`, `listar_archivos`, `crear_archivo` y `anexar_datos` invocan `os.makedirs` cuando `os.path.isdir` devuelve `False`. Por lo tanto, los archivos `.txt` se producen durante la ejecución, no se entregan con el código.

El inventario de archivos se arma en tiempo de ejecución y está compuesto por los archivos que el propio usuario genera durante la sesión:

| Origen | Archivo | Contenido |
| :--- | :--- | :--- |
| Opción 5 | nombre elegido por el usuario | Archivo nuevo con el contenido capturado, encabezado por los datos de la sesión. |
| Opción 6 | nombre o índice elegido por el usuario | Datos anexados al final de un archivo existente, sin alterar su contenido previo. |
| Opción 2 | `cotizaciones_bitacora.txt` | Bitácora que el sistema anexa automáticamente por cada cotización registrada con `si`. |

Una vez que la carpeta contiene archivos `.txt`, la opción 4 los numera mediante el diccionario `disponibles` y permite abrir cualquiera de ellos por nombre o por índice.

Los archivos se escriben en modo `utf-8` y llevan siempre la **fecha de operación** obtenida de la tupla y el **usuario** de la sesión, con dos formatos de encabezado según la operación:

- `crear_archivo` escribe `=== IENTC - Cotizador de Internet ===`, el nombre del archivo, la fecha, el usuario y una línea separadora.
- `anexar_datos` escribe `----- IENTC - Cotizador de Internet -----` únicamente cuando el archivo se crea en ese momento, y anexa fecha, usuario y contenido en cada bloque.

## Depuración técnica con PDB

Durante el desarrollo se utilizó el módulo estándar **PDB** (`import pdb` y `pdb.set_trace()`) para localizar fallas de lógica de control directamente en la consola. Las correcciones resultantes ya están incorporadas en el código documentado en este README:

1. **IVA calculado sobre el precio base sin descuento.** En una versión previa el IVA se aplicaba sobre `precio_plan`, por lo que el cargo fiscal resultaba mayor al real. Al inspeccionar `precio_plan`, `descuento` y `mensualidad` con PDB se confirmó que el IVA debe calcularse sobre la **mensualidad ya descontada**, es decir, primero `mensualidad = precio_plan - descuento` y después `iva_aplicado = mensualidad * iva`.
2. **Descuadre entre el número de opción del menú y las listas del catálogo.** La selección se resolvía con el número capturado directamente, lo que desplazaba el plan una posición. PDB permitió observar el valor de `indice` y se corrigió a `clave - 1` para alinear la opción con las listas paralelas.
3. **Bloqueo permanente del menú durante la espera de la opción.** Al medir el tiempo con `time.sleep` en el hilo principal nunca se alcanzaba el `input`. Se movió la cuenta regresiva a un `threading.Thread` con `join()` y banderas compartidas en el diccionario `estado`, con lo que el menú respondió correctamente y la suspensión por inactividad quedó habilitada.
4. **Cierre de archivos y errores no controlados.** Con PDB sobre el manejador se confirmó que las operaciones de lectura y escritura necesitaban `try/except OSError` y `UnicodeDecodeError`; al agregar la sentencia `with` y los manejadores, los archivos inexistentes o con permisos restringidos ya no detienen el programa.

## Conclusión

En esta entrega final se presentó el diseño lógico y la implementación de un sistema de **cotización de planes de internet empresarial** para IENTC Telecomunicaciones, partiendo de la identificación del problema del área comercial y de la delimitación de las reglas de negocio. La solución aplica de forma completa el modelo Entrada-Proceso-Salida, la clasificación de datos, los operadores y las estructuras de control del lenguaje Python, e incorpora los diez requerimientos de la actividad: identificación de usuario, bienvenida dinámica, pantalla de carga, menú como matriz controlado por `while`, control de inactividad con `for`, captura de la fecha en tupla, persistencia en archivos de texto de lectura, escritura y anexado, control de excepciones con `try-except`, depuración con `PDB` y documentación extensa del código.

La separación del programa en funciones cohesgadas, el uso de la sentencia `with` para la persistencia y la devolución de valores booleanos en `crear_archivo` y `anexar_datos` hacen que el código sea mantenible por terceros. El diseño queda preparado para incorporar nuevos planes, reportes de ventas y consultas al histórico de cotizaciones en fases posteriores del proyecto.

---

## Código completo del archivo `cotizacion.py`

```python
import os
import threading
import time

costo_instalacion = 1500
iva = 0.16
desc_bienvenida = 0.10
desc_contrato_24 = 0.05

velocidades = [100, 200, 500, 1000]
precios = [849, 1299, 2499, 3999]

total_primeros_pagos = 0
total_mensualidades = 0
num_cotizaciones = 0

usuario = ""
fecha = (0, 0, 0)

segundos_inactividad = 600
estado = {"actividad": True, "suspendido": False}

carpeta_datos = "datos"
archivo_bitacora = "cotizaciones_bitacora.txt"

pasos_carga = 6
duracion_paso_carga = 0.5

matriz_menu = [
    ["Opcion", "Descripcion"],
    ["1", "Ver catalogo de planes"],
    ["2", "Realizar una cotizacion"],
    ["3", "Ver resumen de cotizaciones"],
    ["4", "Leer archivo de texto"],
    ["5", "Crear archivo de texto"],
    ["6", "Anexar datos a un archivo"],
    ["7", "Salir"],
]


def pedir_nombre():
    while True:
        nombre = input("\n Ingresa tu nombre: ").strip()
        if nombre != "":
            return nombre
        print("El nombre no puede quedar vacio.")


def fecha_texto():
    dia = str(fecha[0])
    mes = str(fecha[1])
    anio = str(fecha[2])
    if len(dia) == 1:
        dia = "0" + dia
    if len(mes) == 1:
        mes = "0" + mes
    return dia + "/" + mes + "/" + anio


def capturar_fecha():
    global fecha
    while True:
        try:
            texto = input("Ingresa la fecha de operacion (dia/mes/año, ej. 12/06/2026): ").strip()
            partes = texto.split("/")
            if len(partes) != 3:
                raise ValueError
            dia = int(partes[0])
            mes = int(partes[1])
            anio = int(partes[2])
            if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1900 or anio > 2100:
                raise ValueError
            fecha = (dia, mes, anio)
            print("Fecha de operacion registrada: fecha =", fecha)
            return
        except ValueError:
            print("La fecha debe tener el formato dia/mes/año, por ejemplo 12/06/2026.")


def bienvenida():
    titulo = "IENTC - Sistema de cotización empresarial"
    borde = "=" * len(titulo)
    print("\n" + borde)
    print(titulo)
    print(borde)
    print("\nEstimado usuario " + usuario + ", le damos la bienvenida al sistema IENTC.")
    print("Su sesion quedo registrada en la fecha" + fecha_texto() + " por el area comercial de IENTC.")
    print("Perfil: " + usuario.upper() + " | Estatus: Activo")
    print("Aquí puede consultar el catalogo, generar cotizaciones y administrar sus archivos de texto.")
    print(borde)


def pantalla_carga():
    avance = 100 // pasos_carga
    print("\n --- Iniciando el sistema, por favor espere...")
    for paso in range(1, pasos_carga + 1):
        print("\rCargando modulos " + "." * paso + " " + str(paso * avance) + "%", end="", flush=True)
        time.sleep(duracion_paso_carga)
    print("\rSistema operativo al 100%. Carga completada en " + str(pasos_carga * duracion_paso_carga) + " segundos.      ")


def imprimir_menu():
    print("\n ----- IENTC - Cotizador de Internet  ----- ")
    ancho_opcion = 0
    ancho_descripcion = 0
    for fila in matriz_menu:
        if len(fila[0]) > ancho_opcion:
            ancho_opcion = len(fila[0])
        if len(fila[1]) > ancho_descripcion:
            ancho_descripcion = len(fila[1])
    for fila in matriz_menu:
        print(fila[0].ljust(ancho_opcion + 2) + fila[1])
    print("-" * (ancho_opcion + ancho_descripcion + 3))


def inactividad():
    for segundo in range(segundos_inactividad, 0, -1):
        if estado["actividad"] == False:
            return
        if segundo % 60 == 0 and segundo < segundos_inactividad:
            print("\nSesion sin interaccion. El menu se suspendera en " + str(segundo // 60) + " minuto(s).")
        time.sleep(1)
    estado["actividad"] = False
    estado["suspendido"] = True
    print("\n*** Se detectaron 10 minutos de inactividad, el menu fue suspendido ***")


def esperar_opcion():
    estado["actividad"] = True
    estado["suspendido"] = False
    hilo = threading.Thread(target=inactividad)
    hilo.daemon = True
    hilo.start()
    opcion = input("Selecciona una opcion: ")
    estado["actividad"] = False
    hilo.join()
    if estado["suspendido"] == True:
        return "suspendido"
    return opcion.strip()


def ver_catalogo():
    print("\n--- Catalogo de planes ---")
    for i in range(len(velocidades)):
        print("  " + str(i + 1) + ".- " + str(velocidades[i]) + " Mbps  -  $" + str(precios[i]) + " / mes")


def preparar_carpeta():
    if os.path.isdir(carpeta_datos) == False:
        os.makedirs(carpeta_datos)


def listar_archivos():
    disponibles = {}
    try:
        preparar_carpeta()
        nombres = sorted(os.listdir(carpeta_datos))
        indice = 0
        for nombre in nombres:
            if nombre.lower().endswith(".txt") == True:
                indice = indice + 1
                disponibles[indice] = nombre
    except OSError:
        print("No fue posible revisar los archivos disponibles.")
    return disponibles


def mostrar_archivos(disponibles):
    print("\n--- Archivos de texto disponibles ---")
    for indice in disponibles:
        print("  " + str(indice) + ".- " + disponibles[indice])


def leer_archivo():
    disponibles = listar_archivos()
    if len(disponibles) == 0:
        print("No hay archivos de texto disponibles para lectura.")
        return
    mostrar_archivos(disponibles)
    while True:
        seleccion = input("Ingresa el nombre del archivo que deseas abrir: ").strip()
        if seleccion == "":
            continue
        if os.path.isfile(os.path.join(carpeta_datos, seleccion)) == True:
            nombre_archivo = seleccion
            break
        try:
            numero = int(seleccion)
        except ValueError:
            numero = 0
        if numero in disponibles:
            nombre_archivo = disponibles[numero]
            break
        print("" + seleccion + "' no esta disponible. Revisa el nombre capturado.")
    try:
        with open(os.path.join(carpeta_datos, nombre_archivo), "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError:
        print("Ni se pudo leer '" + nombre_archivo + "', revisa que exista en la carpeta de datos.")
        return
    except UnicodeDecodeError:
        print("El archivo'" + nombre_archivo + "' contiene caracteres no compatibles con la lectura.")
        return
    print("\n--- Contenido de " + nombre_archivo + " ---")
    if contenido.strip() == "":
        print("El archivo no contiene informacion.")
    else:
        print(contenido)


def crear_archivo(nombre_archivo, contenido):
    if nombre_archivo.lower().endswith(".txt") == False:
        nombre_archivo = nombre_archivo + ".txt"
    if os.path.exists(os.path.join(carpeta_datos, nombre_archivo)) == True:
        print("Error: '" + nombre_archivo + "' ya existe, elige otro nombre para no sobrescribirlo.")
        return False
    try:
        preparar_carpeta()
        with open(os.path.join(carpeta_datos, nombre_archivo), "w", encoding="utf-8") as archivo:
            archivo.write("=== IENTC - Cotizador de Internet ===\n")
            archivo.write("Archivo: " + nombre_archivo + "\n")
            archivo.write("Fecha de operacion: " + fecha_texto() + "\n")
            archivo.write("Usuario: " + usuario + "\n")
            archivo.write("--------------------------------------\n")
            archivo.write(contenido + "\n")
        print("Archivo creado correctamente: " + nombre_archivo)
        return True
    except OSError:
        print("Falló la creacion de '" + nombre_archivo + "', prueba de nuevo.")
        return False


def anexar_datos(nombre_archivo, contenido):
    if nombre_archivo.lower().endswith(".txt") == False:
        nombre_archivo = nombre_archivo + ".txt"
    try:
        preparar_carpeta()
        nuevo = os.path.exists(os.path.join(carpeta_datos, nombre_archivo)) == False
        with open(os.path.join(carpeta_datos, nombre_archivo), "a", encoding="utf-8") as archivo:
            if nuevo == True:
                archivo.write("----- IENTC - Cotizador de Internet -----\n")
            archivo.write("\nFecha de operacion: " + fecha_texto() + "\n")
            archivo.write("Usuario: " + usuario + "\n")
            archivo.write(contenido + "\n")
        print("Datos anexados en: " + nombre_archivo)
        return True
    except OSError:
        print("Falló el anexado en '" + nombre_archivo + "', prueba de nuevo.")
        return False


def escribir_archivo():
    disponibles = listar_archivos()
    if len(disponibles) > 0:
        mostrar_archivos(disponibles)
    nombre_archivo = input("Nombre del archivo nuevo (se agregara la extension .txt): ").strip()
    if nombre_archivo == "":
        print("Operacion cancelada.")
        return
    contenido = input("Contenido que se guardara en el archivo: ")
    crear_archivo(nombre_archivo, contenido)


def anexar_archivo():
    disponibles = listar_archivos()
    if len(disponibles) == 0:
        print("No hay archivos de texto disponibles para anexar datos.")
        return
    mostrar_archivos(disponibles)
    nombre_archivo = input("Nombre del archivo al que se anexaran los datos: ").strip()
    if nombre_archivo == "":
        print("Operacion cancelada.")
        return
    try:
        numero = int(nombre_archivo)
    except ValueError:
        numero = 0
    if numero in disponibles:
        nombre_archivo = disponibles[numero]
    contenido = input("Datos que se anexaran al archivo: ")
    anexar_datos(nombre_archivo, contenido)


def ver_cotizacion():
    global total_primeros_pagos
    global total_mensualidades
    global num_cotizaciones
    print("\n--- Nueva cotizacion ---")
    for i in range(len(velocidades)):
        print("  " + str(i + 1) + ". " + str(velocidades[i]) + " Mbps  -  $" + str(precios[i]) + " / mes")

    while True:
        try:
            clave = int(input("Elige el plan (1-4): "))
        except ValueError:
            print("Error, debes ingresar un numero entero, intenta de nuevo.")
            continue
        if clave >= 1 and clave <= 4:
            break
        print("Error, plan no valido, intenta de nuevo.")

    indice = clave - 1
    velocidad_plan = velocidades[indice]
    precio_plan = precios[indice]

    while True:
        try:
            meses = int(input("Meses de contrato (0, 12 o 24): "))
        except ValueError:
            print("Error: solo se aceptan numeros enteros.")
            continue
        if meses == 0 or meses == 12 or meses == 24:
            break
        print("Error: solo se aceptan contratos de 0, 12 o 24 meses.")

    nuevo = input("Es cliente nuevo? (s/n): ")

    descuento = 0
    if nuevo.lower() == "s":
        descuento = precio_plan * desc_bienvenida

    if meses == 24:
        descuento = descuento + precio_plan * desc_contrato_24

    instalacion = costo_instalacion
    if meses >= 12:
        instalacion = 0

    mensualidad = precio_plan - descuento
    iva_aplicado = mensualidad * iva
    primer_pago = mensualidad + iva_aplicado + instalacion

    print("\n---------- Detalles de cotizacion ----------")
    print("Plan seleccionado:     " + str(velocidad_plan) + " Mbps")
    print("Precio base mensual:  $" + str(precio_plan))
    print("Descuento:           -$" + str(round(descuento, 2)))
    print("Mensualidad:          $" + str(round(mensualidad, 2)))
    print("IVA (16%):            $" + str(round(iva_aplicado, 2)))
    print("Instalacion:          $" + str(round(instalacion, 2)))
    print("Primer pago total:    $" + str(round(primer_pago, 2)))
    if meses > 0:
        print("Contrato firmado por:     " + str(meses) + " meses")

    total_primeros_pagos = total_primeros_pagos + primer_pago
    total_mensualidades = total_mensualidades + mensualidad
    num_cotizaciones = num_cotizaciones + 1

    registro = input("\nDeseas registrar esta cotizacion? (si/no): ").strip().lower()
    if registro == "si":
        detalle = (
            "Cotizacion #" + str(num_cotizaciones)
            + " | Plan: " + str(velocidad_plan) + " Mbps"
            + " | Precio base: $" + str(precio_plan)
            + " | Descuento: -$" + str(round(descuento, 2))
            + " | Mensualidad: $" + str(round(mensualidad, 2))
            + " | IVA: $" + str(round(iva_aplicado, 2))
            + " | Instalacion: $" + str(round(instalacion, 2))
            + " | Primer pago: $" + str(round(primer_pago, 2))
            + " | Contrato: " + str(meses) + " meses\n"
        )
        anexar_datos(archivo_bitacora, detalle)


def ver_resumen():
    print("\n---------- Resumen de cotizaciones ----------")
    print("Cotizaciones realizadas:  " + str(num_cotizaciones))
    print("Total de primeros pagos:  $" + str(round(total_primeros_pagos, 2)))
    print("Total de mensualidades:    $" + str(round(total_mensualidades, 2)))


def menu_principal():
    while True:
        imprimir_menu()
        opcion = esperar_opcion()
        if opcion == "suspendido":
            while True:
                continuar = input("Deseas continuar en el menu? (si/no): ").strip().lower()
                if continuar == "si" or continuar == "no":
                    break
                print("Error, responde exactamente usando 'si' o 'no'.")
            if continuar == "si":
                print("Sesion reanudada, regresarás al menu principal.")
                continue
            print("Regresando a la pantalla de inicio del programa.")
            return "inicio"
        if opcion == "1":
            ver_catalogo()
        elif opcion == "2":
            ver_cotizacion()
        elif opcion == "3":
            ver_resumen()
        elif opcion == "4":
            leer_archivo()
        elif opcion == "5":
            escribir_archivo()
        elif opcion == "6":
            anexar_archivo()
        elif opcion == "7":
            return "salir"
        else:
            print("Opcion no valida, intenta de nuevo.")


def main():
    global usuario
    while True:
        usuario = pedir_nombre()
        capturar_fecha()
        bienvenida()
        pantalla_carga()
        resultado = menu_principal()
        if resultado == "salir":
            print("Gracias por usar el programa.")
            return


try:
    main()
except KeyboardInterrupt:
    print("\n\n Iterrupción del usuario, se cerrará el programa.")
except EOFError:
    print("\n\n Fin de la entrada de datos, el programa se cerrará.")
except Exception as error:
    print("\nError inesperado:", error)
    print("El programa se cerrará, revise los archivos e intentelo de nuevo.")
```
