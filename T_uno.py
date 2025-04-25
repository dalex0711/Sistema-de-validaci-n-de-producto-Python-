# SISTEMAS DE VALIDACIÓN DE PRODUCTOS.


import sys #Importando librerias que me serviran posteriormente para salir del programa y limpiar la terminal.
import os

os.system("cls" if os.name == "nt" else "clear") #Ejecutando comando para limpiar la terminal (dependiento del SO) con ayuda de la libreria os
    
def proceso(): # En está función encontraremos todo el proceso:

    print ("\n-------\033[1m¡BIENVENIDO A LA TIENDITA!\033[0m.------- \n")

    nombre_producto = input("Ingresa el nombre del producto: ") #Inicialmente solicitamos el nombre del producto.
    
    while True: # En este bloque validaremos que el precio del producto ingresado posteriormente sea un número flotante.
        try:
            precio_unidad   = float(input("Ingresa el precio: "))
            if precio_unidad <= 0:
                print("Ingresa un número positivo real")
                continue
            
        except ValueError:
            print("Error:  Por favor ingresa un valor valido.")
            continue
        
        break

    while True:# En este bloque validaremos que el precio del producto ingresado posteriormente sea un número entero.
        try: 
            cantidad_productos = int(input("Ingresa cuantos productos de \033[1m{}\033[0m has adquirido: ".format(nombre_producto.capitalize())))
            if cantidad_productos <= 0:
                print("Ingresa un número positivo real")
                continue
        except ValueError:
            print("Error: Por favor ingresa un valor valido")
            continue
            
        break    
            

    while True: # Aquí Validaremos si el usuario cuenta con codigo de descuento. 

        descuento = input("¿Tienes código de descuento? RESPONDA: (SI O NO): ").upper().strip()

        if descuento == "SI": 

            while True:  # Una vez sabiendo que si tiene codigo, validaremos que introduzca un porcentaje valido
                try:
                    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (1% hasta 100%): "))
                    if porcentaje_descuento < 0:
                        print("Error: El porcentaje de descuento no puede ser negativo. Por favor, ingresa un valor válido.")
                    elif 1 <= porcentaje_descuento <= 100:
                        total = precio_unidad * cantidad_productos
                        total_descuento = total - (total * (porcentaje_descuento / 100))
                        
                        os.system('clear') 
                        print("\n---------\033[1m FACTURA \033[0m----------\n"),
                        print (f"NOMBRE DEL PRODUCTO: {nombre_producto.capitalize()}"),
                        print(f"PRECIO UNITARIO: {precio_unidad:.2f}")
                        print(f"CANTIDAD DE PRODUCTOS: {cantidad_productos:}"),
                        print(f"SUBTOTAL: {total:.2f}"),
                        print(f"DESCUENTO: {porcentaje_descuento.__round__()}%"),
                        print(f"TOTAL: {total_descuento:.2f}\n")
                        break  

                    else:
                        print("El porcentaje de descuento debe estar entre 1% y 100%. Inténtalo nuevamente.") 
                        
                except ValueError:
                    print("Error: Por favor ingresa un número válido para el porcentaje de descuento.")
            break
                

        elif (descuento.upper()) == "NO": #En caso de indicar que no lo tiene, se hacen las operaciones definidas para posteriomente imprimir la factura.
                
                total = precio_unidad * cantidad_productos
                total_descuento = "No aplica" 
                
                os.system('clear') 
                print("\n---------\033[1m FACTURA \033[0m----------\n"),
                print(f"NOMBRE DEL PRODUCTO: {nombre_producto.capitalize()}"),
                print(f"PRECIO UNITARIO: {precio_unidad:.2f}")
                print(f"CANTIDAD DE PRODUCTO: {cantidad_productos}"),
                print(f"SUBTOTAL: {total:.2f}"),
                print(f"DESCUENTO: {total_descuento}"),
                print(f"TOTAL: {total:.2f}\n")
                break   
            
            
        else:
            print ("-- El dato ingresado es invalido, por favor indique \033[1m(SI O NO)\033[0m")
            
            
def limpiar (): # En está funcion limpio la pantalla en tiempo de ejecucion dependiendo del sistema operativo siendo nt Windows.
    os.system("cls" if os.name == "nt" else "clear")
    

def salir():# Está funcion fue hecha para llamar a la libreria previamente importada para salir del prograna.
    limpiar()
    print ("\n-------\033[1mGRACIAS POR TU COMPRA\033[0m.-------")
    print("*   Vuelve pronto a ¡LA TIENDITA!   *")

    sys.exit()
           
def funcion_p(): # Cree está función para llamar a def "proceso()" cuantas veces el usuario desee volver a ingresar productos:
    while True:
        limpiar()
        proceso()
            
        while True:
            continuar = input("¿Te gustaría hacer otra compra? (SI/NO)").lower().strip()# Contando con la opción si desea llamarla o no.
            
            if continuar == "si":
                break  
            elif continuar == "no":
                salir()
                return 
            else:
                print("-- El dato ingresado es invalido, por favor indique \033[1m(SI O NO)\033[0m")
                
funcion_p()