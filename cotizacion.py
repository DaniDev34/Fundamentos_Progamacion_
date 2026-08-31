costo_instalacion = 1500    
iva = 0.16                  
desc_bienvenida = 0.10      
desc_contrato_24 = 0.05     

velocidades = [100, 200, 500, 1000]
precios = [849, 1299, 2499, 3999]

total_primeros_pagos = 0
total_mensualidades = 0
num_cotizaciones = 0

while True:
    print("\n ----- IENTC - Cotizador de Internet  ----- ")
    print("1. Ver catálogo de planes")
    print("2. Realizar una cotización")
    print("3. Ver resumen de cotizaciones")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        print("\n--- Catálogo de planes ---")
        for i in range(len(velocidades)):
            print(f"  {i + 1}.- {velocidades[i]} Mbps  -  ${precios[i]} / mes")

    elif opcion == "2":
        print("\n--- Nueva cotización ---")
        for i in range(len(velocidades)):
            print(f"  {i + 1}. {velocidades[i]} Mbps  -  ${precios[i]} / mes")

        while True:
            clave = int(input("Elige el plan (1-4): "))
            if 1 <= clave <= 4:
                break
            print("Error, plan no válido, intenta de nuevo.")

        indice = clave - 1
        velocidad_plan = velocidades[indice]
        precio_plan = precios[indice]

        while True:
            meses = int(input("Meses de contrato (0, 12 o 24): "))
            if meses == 0 or meses == 12 or meses == 24:
                break
            print("Error, solo se aceptan contratos de 0, 12 o 24 meses.")

        nuevo = input("¿Es cliente nuevo? (s/n): ")

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

        print("\n---------- Detalles de cotización ----------")
        print(f"\nPlan seleccionado:     {velocidad_plan} Mbps")
        print(f"\nPrecio base mensual:  ${precio_plan}")
        print(f"\nDescuento:           -${descuento:.2f}")
        print(f"\nMensualidad:          ${mensualidad:.2f}")
        print(f"\nIVA (16%):            ${iva_aplicado:.2f}")
        print(f"\nInstalación:          ${instalacion:.2f}")
        print(f"\nPrimer pago total:    ${primer_pago:.2f}")
        if meses > 0:
            print(f"Contrato firmado por:     {meses} meses")

        total_primeros_pagos += primer_pago
        total_mensualidades += mensualidad
        num_cotizaciones += 1

    elif opcion == "3":

        print("\n---------- Resumen de cotizaciones ----------")
        print(f"Cotizaciones realizadas:  {num_cotizaciones}")
        print(f"Total de primeros pagos:  ${total_primeros_pagos:.2f}")
        print(f"Total de mensualidades:    ${total_mensualidades:.2f}")

    elif opcion == "4":
        print("Gracias por usar el programa.")
        break

    else:
        print("Opción no válida, intenta de nuevo.")