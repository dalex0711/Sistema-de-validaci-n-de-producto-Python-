
# SISTEMAS DE VALIDACIÓN DE PRODUCTOS.

print ("\n-------\033[1m¡BIENVENIDO A LA TIENDITA!\033[0m.------- \n")

nombre_producto = input("Ingresa el nombre del producto: ")
precio_unidad   = float(input("Ingresa el precio: "))
cantidad_productos = int(input("Ingresa cuantos productos de \033[1m{}\033[0m has adquirido: ".format(nombre_producto.capitalize())))


while True: # Validar los posible casos que el usuario puede responder.

    descuento = input("¿Tienes código de descuento? RESPONDA: (SI O NO): ")

    if (descuento.upper()) == "SI":

        while True:  # Validación cuando se introduce el porcentaje de descuento.
            try:
                porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (1% hasta 100%): "))
                if porcentaje_descuento < 0:
                    print("Error: El porcentaje de descuento no puede ser negativo. Por favor, ingresa un valor válido.")
                elif 1 <= porcentaje_descuento <= 100:
                    total = precio_unidad * cantidad_productos
                    total_descuento = total - (total * (porcentaje_descuento / 100))

                    factura = "\n".join([  # Crea una lista (join) y las une con un salto de linea
                        "\n---------\033[1m FACTURA \033[0m----------\n",
                        f"NOMBRE DEL PRODUCTO: {nombre_producto.capitalize()}",
                        f"CANTIDAD DE PRODUCTOS: {cantidad_productos:}",
                        f"SUBTOTAL: {total:.2f}",
                        f"DESCUENTO: {porcentaje_descuento.__round__()}%",
                        f"TOTAL: {total_descuento:.2f}\n"
                    ])
                    print(factura)

                    break  # Sale del bucle de descuento después de mostrar la factura.
                else:
                    print("El porcentaje de descuento debe estar entre 1% y 100%. Inténtalo nuevamente.")
                    
            except ValueError:
                print("Error: Por favor ingresa un número válido para el porcentaje de descuento.")
        break
             

    elif (descuento.upper()) == "NO":
            
            total = precio_unidad * cantidad_productos
            total_descuento = "No aplica" 

            factura = "\n".join([
            "\n---------\033[1m FACTURA \033[0m----------\n",
            f"NOMBRE DEL PRODUCTO: {nombre_producto.capitalize()}",
            f"CANTIDAD DE PRODUCTO: {cantidad_productos}",
            f"SUBTOTAL: {total:.2f}",
            f"DESCUENTO: {total_descuento}",
            f"TOTAL: {total:.2f}\n"
            ])
            print(factura)
            
            break   
        
        
    else:
        print ("-- El dato ingresado es invalido, por favor indique \033[1m(SI O NO)\033[0m")
        
