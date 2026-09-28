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
