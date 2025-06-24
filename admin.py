import csv
import os
# def login():
    
#     cedula = input("digite su documento de identificacion: ")
#     contraseña = input("digite su contraseña: ")
def menu_principal():
    activo=True
    while(activo):
        os.system("cls")
        print("************** MENU PRINCIPAL **************")
        
        print("""
            1. MENU USUARIOS
            2. MENU CLIENTES
            3. MENU PRODUCTOS
            4. VENDER
            5. MENU FACTURAS
            0. PARA SALIR  
            
            
            """)
        
        opcion=int(input("INGRESA TU ELECCION: "))
        
        
        match(opcion):
            case 1:menu_usuarios()
            case 2:menu_clientes()
            case 3:menu_productos()
            case 4:vender()
            # case 4:menu_factura()
            case 0: 
                print("*************HASTA LA VISTA BBY***************")
                activo = False
            case _: print("opc incorrecta")

#---------------------------------CRUD USUARIOS-------------------------------------------------
def menu_usuarios():
    
    activo=True
    while(activo):
        os.system("cls")
        print("************** MENU DE USUARIOS **************")
        print("""
            1. PARA AGREGAR USUARIO
            2. PARA BUSCAR USUARIO POR ID
            3. PARA LISTAR USUARIOS
            4. PARA ACTUALIZAR USUARIOS
            5. PARA ELIMINAR USUARIOS 
            0. PARA SALIR   
            
            """)
        
        opcUsuario=int(input("Ingresa tu eleccion: "))
        
        match (opcUsuario):
            case 1: agregar_usuario()
            case 2: buscar_usuario_id()
            case 3: listar_usuario()
            case 4: actualizar_usuario()
            case 5: eliminar_usuario()
            case 0: 
                menu_principal()
                print("*************HASTA LA VISTA BBY***************")
                activo=False
            case _:print("Opc incorrecta")


def agregar_usuario():
    id = int(input("INGRESE SU CC: "))
    nombre = input("INGRESE SU NOMBRE: ").lower()
    contraseña = input("INGRESE SU CONTRASEÑA: ")
    rol = input("INGRESAR ROL: ")

    try:
        with open("usuarios.csv", "r") as file:
            for linea in file:
                datos = linea.strip().split(";")
                if int(datos[0]) == id:
                    print(f"ERROR: El ID QUE ACABA DE AGREGAR ES EL '{id}' Y YA EXISTE.")
                    input("\nPresiona Enter para continuar...")
                    return
    except FileNotFoundError:
        
        pass
    with open("usuarios.csv", "a") as file:
        file.write(f"{id};{nombre};{contraseña};{rol}\n")
        print('USUARIO AGREGADO CON ÉXITO')
# __________________________________________________________________________________________
        
def buscar_usuario_id():
    print("************** BUSCAR *******************")
    id= input("INGRESE EL ID DEL USUARIO A BUSCAR: ")
    
    
    with open("usuarios.csv","r") as file:
        for fila in file:
            lista_fila = fila.split(';')
            
            if lista_fila[0] == id:
                print(fila.split(';'))
                print('ENCONTRAMOS USUARIO')
                input("\nPresiona Enter para continuar...")
                print('\n ')
                break
        if lista_fila[0] != id:
            print('Usuario no encontrado')
            input("\nPresiona Enter para continuar...")
        
    
            

def listar_usuario():
    os.system("cls")
    print('-----------------LISTADO DE USUARIOS-----------')
    
    with open("usuarios.csv","r") as file:
        for fila in file:
            print(fila.split(';'))

    input("\nPresiona Enter para continuar...")
    
def borrar_informacion_usuarios():
    print('INFORMACION ELIMINADA ')
    with open("usuarios.csv","w") as file:
        file.close

def actualizar_usuario():
    print("**************ACTUALIZAR USUARIOS*******************")
    id= input("INGRESE EL CC DEL USUARIO QUE DESEA ACTUALIZAR: ")
    lista_copia = [] #copia de los datos actualizados
    lista_fila = [] # datos que provienen de usuarios.csv
    with open("usuarios.csv","r") as file:
        for fila in file:
            lista_fila = fila.split(';')
            if lista_fila[0] == id:
                id= input('INGRESE LA NUEVA ID: ')
                nombre= input('INGRESE EL NUEVO NOMBRE: ')
                contraseña= input('INGRESE LA NUEVA CONTRASEÑA: ')
                rol= input('INGRESE EL NUEVO ROL: ')
                nueva_fila = id + ';' + nombre +';'+ contraseña +';'+ rol + '\n'
                lista_copia.append(nueva_fila)
                print('ENCONTRAMOS USUARIO')
                input("\nPresiona Enter para continuar...")
                print('\n ')
            else:
                lista_copia.append(fila)
    borrar_informacion_usuarios()
    for dato in lista_copia:
        with open("usuarios.csv","a") as file:
            file.write(dato)
    print("USUARIO ACTUALIZADO CON EXITO")
    input("\nPresiona Enter para continuar...")

def eliminar_usuario():
    print("************ELIMINAR USUARIOS**************")
    eliminar = input("INGRESE EL ID DEL USUARIO QUE DESEA ELIMINAR: ")
    lista_copia = []

    with open("usuarios.csv", "r") as file:
        for fila in file:
            lista_fila = fila.strip().split(';')                 #strip() para eliminar posibles saltos de línea o espacios en los datos leídos
            if lista_fila[0] != eliminar:                         # eliminar es la variable que asigno para que busque el id que deseo eliminar y esto quiere decir si esta fila NO es la del usuario a eliminar
                lista_copia.append(fila)
                
            else:
                print("USUARIO ELIMINADO")

    with open("usuarios.csv", "w") as file:
        for fila in lista_copia:
            file.write(fila)               

# -----------------------------------CRUD PRODUCTOS----------------------------------------------------------------------
def menu_productos():
    
    activo=True
    while(activo):
        os.system("cls")
        print("************** MENU DE PRODUCTOS **************")
        print("""
            1. PARA INGRESAR EL PRODUCTO
            2. PARA LISTAR EL PRODUCTO
            3. PARA ACTUALIZAR EL PRODUCTO
            4. PARA ELIMINAR EL PRODUCTO
            0. PARA SALIR     
            """)
        opcUsuario=int(input("INGRESE SU ELECCION: "))
        match (opcUsuario):
            case 1: agregar_producto()
            case 2: listar_productos()
            case 3: actualizar_producto()
            case 4: eliminar_producto()
            case 0: 
                print("*************HASTA LA VISTA BBY***************")
                activo=False
            case _:print("Opc incorrecta")


def agregar_producto():
    id = input("INGRESE EL ID DEL PRODUCTO: ")
    tipo = input("INGRESE EL TIPO DEL PRODUCTO (BOLIS, PALETA, HELADO CUADRADO, HELADO REDONDO): ")
    sabor = input("INGRESE EL SABOR (NARANJA, PIÑA, MORA, TRICOLOR, LIMÓN, ETC): ")
    stock = input("CANTIDAD DE PRODUCTO: ")
    precio = input("INGRESE PRECIO DEL PRODUCTO: ")

    try:
        with open("productos.csv", "r") as file:
            for linea in file:
                datos = linea.strip().split(";")
                if datos[0] == id:
                    print(f"ERROR: El ID DEL PRODUCTO ES EL  '{id}' YA EXISTE.")
                    input("\nPresiona Enter para continuar...")
                    return
    except FileNotFoundError:
        pass 

    with open("productos.csv", "a") as file:
        file.write(f"{id};{tipo};{sabor};{stock};{precio}\n")
        print('PRODUCTO AGREGADO CON ÉXITO')
# ____________________________________________________________________________________________________

def listar_productos():
    print("******LISTAR LOS PRODUCTOS*****")
    with open("productos.csv","r") as file:
        for fila in file:
            print(fila.split(';'))
            
    input("\nPresiona Enter para continuar...")


def borrar_informacion_productos():
    print('INFORMACION ELIMINADA')
    with open("productos.csv","w") as file:
        file.close       

def actualizar_producto():
    print("**************ACTUALIZAR PRODUCTOS*******************")
    id= input("INGRESE EL ID DEL PRODUCTO QUE DESEA ACTUALIZAR: ")
    lista_copia = [] #copia de los datos actualizados
    lista_fila = [] # datos que provienen de productos.csv
    with open("productos.csv","r") as file:
        for fila in file:
            lista_fila = fila.split(';')
            if lista_fila[0] == id:
                id= input('INGRESE LA NUEVA ID: ')
                tipo= input('INGRESE EL NUEVO TIPO: ')
                sabor= input('INGRESE EL NUEVO SABOR: ')
                stock= input('INGRESE LA NUEVA CANTIDAD: ')
                precio= input('INGRESE EL NUEVO PRECIO: ')
                nueva_fila = id + ';' + tipo +';'+ sabor +';'+ stock +';'+precio + '\n'
                lista_copia.append(nueva_fila)
                print('ENCONTRAMOS EL PRODUCTO')
            else:
                lista_copia.append(fila)
    borrar_informacion_productos()
    for dato in lista_copia:
        with open("productos.csv","a") as file:
            file.write(dato)
        print('ACTUALIZAMOS EL PRODUCTO')



def eliminar_producto():
    print("************ELIMINAR PRODUCTOS**************")
    eliminar = input("INGRESE EL ID DEL PRODUCTO QUE DESEA ELIMINAR: ")
    lista_copia = []

    with open("productos.csv", "r") as file:
        for fila in file:
            lista_fila = fila.strip().split(';')#strip() para eliminar posibles saltos de línea o espacios en los datos leídos
            if lista_fila[0] != eliminar:
                lista_copia.append(fila)
                
            else:
                print("PRODUCTO ELIMINADO")

    with open("productos.csv", "w") as file:
        for fila in lista_copia:
            file.write(fila)   
            



# *********************************************************************************************************************************
def menu_clientes():
    activo=True
    while(activo):
        os.system("cls")
        print("************** MENU DE CLIENTES **************")
        print("""
            1. PARA AGREGAR CLIENTE
            2. PARA LISTAR CLIENTE
            3. PARA ACTUALIZAR CLIENTES
            4. PARA ELIMINAR CLIENTES
            0. PARA SALIR                                                             
            """)
        opcUsuario=int(input("INGRESE SU ELECCION: "))
        match (opcUsuario):
            case 1: agregar_clientes()
            case 2: listar_clientes()
            case 3: actualizar_clientes()
            case 4: eliminar_clientes()
            case 0: 
                print("*************HASTA LA VISTA BBY***************")
                activo=False
            case _:print("OPC INCORRECTA")

lista_cliente = []
def agregar_clientes():
    
    id = input("INGRESE EL CC DEL CLIENTE: ")
    cliente_existe = False
    try:
        with open("clientes.csv","r") as file:
            for fila in file:
                lista_fila = fila.strip().split(';')
                
                if lista_fila[0] == id:
                    print('CLIENTE YA REGISTRADO :/')
                    cliente_existe = True
                    input("\nPresiona Enter para continuar...")
                    print('\n ')
                    break
    except FileNotFoundError:
        # Si el archivo no existe, lo tratamos como vacío (no hay clientes aún)
        pass
        
    if not cliente_existe:
        nombre =input("INGRESE SU NOMBRE: ").lower()
        with open("clientes.csv","a") as file:
            file.write(f"{id};{nombre}\n")
            
        print('CLIENTE AGREGADO CON EXITO')
        
        input("\nPresiona Enter para continuar...")
        print("\n")

# def buscar_cliente_id():
#     print("************** BUSCAR CLIENTE POR ID*******************")
#     id= input("INGRESE EL ID DEL CLIENTE A BUSCAR: ")

#     with open("clientes.csv","r") as file:
#         for fila in file:
#             lista_fila = fila.split(';')
            
#             if lista_fila[0] == id:
#                 print(fila.split(';'))
#                 print('ENCONTRAMOS CLIENTE')
#                 input("\nPresiona Enter para continuar...")
#                 print('\n ')
#                 break
                
#         if lista_fila[0] != id:
#             print('CLIENTE NO ENCONTRADO')
#             input("\nPresiona Enter para continuar...")
    
    


def listar_clientes():
    os.system("cls")
    print('-----------------LISTADO DE CLIENTES-----------')
    
    with open("clientes.csv","r") as file:
        for fila in file:
            print(fila.split(';'))

    input("\nPresiona Enter para continuar...")

def borrar_informacion_clientes():
    print('INFORMACION ELIMINADA')
    with open("clientes.csv","w") as file:
        file.close       

def actualizar_clientes():
    print("**************ACTUALIZAR CLIENTES*******************")
    id= input("INGRESE EL ID DEL CLIENTE QUE DESEA ACTUALIZAR: ")
    lista_copia = [] #copia de los datos actualizados
    lista_fila = [] # datos que provienen de usuarios.csv
    with open("clientes.csv","r") as file:
        for fila in file:
            lista_fila = fila.split(';')
            if lista_fila[0] == id:
                id= input('INGRESE LA NUEVA ID: ')
                nombre= input('INGRESE EL NUEVO NOMBRE: ')
                
                nueva_fila = id + ';' + nombre + '\n'
                lista_copia.append(nueva_fila)
                print('ENCONTRAMOS CLIENTES')
                input("\nPresiona Enter para continuar...")
                print('\n ')
            else:
                lista_copia.append(fila)
    borrar_informacion_clientes()
    for dato in lista_copia:
        with open("clientes.csv","a") as file:
            file.write(dato)
    print("CLIENTES ACTUALIZADO CON EXITO")
    input("\nPresiona Enter para continuar...")
    
def eliminar_clientes():
    print("************ELIMINAR CLIENTES**************")
    eliminar = input("INGRESE EL ID DEL CLIENTE QUE DESEA ELIMINAR: ")
    lista_copia = []

    with open("clientes.csv", "r") as file:
        for fila in file:
            lista_fila = fila.strip().split(';')                 #strip() para eliminar posibles saltos de línea o espacios en los datos leídos
            if lista_fila[0] != eliminar:                         # eliminar es la variable que asigno para que busque el id que deseo eliminar y esto quiere decir si esta fila NO es la del cliente a eliminar
                lista_copia.append(fila)
                print('Ususario no existe')
                input("\nPresiona Enter para continuar...")
                print('\n ')
                
            else:
                print("CLIENTE ELIMINADO")
                input("\nPresiona Enter para continuar...")

    with open("clientes.csv", "w") as file:
        for fila in lista_copia:
            file.write(fila) 





# ******************************************************************************************************************
# def vender():
#     print ("**********************INICIAR VENTA***************************")



# Pedir ID del cliente y validar que existe.

    
# Generar número de factura automáticamente leyendo el último facturas.csv.

# Permitir al usuario:

# Ver productos disponibles.

# Elegir varios productos (por ID) y cantidades.

# Verificar si hay stock suficiente.

# Calcular subtotales y total.

# Actualizar el stock de los productos en productos.csv.

# Crear un archivo factura_<n>.csv con el detalle de la venta.

# Agregar un resumen en facturas.csv.
def vender():
    print("********************** INICIAR VENTA ***************************")

    #--------------------------------------------Pedir cliente y validar si existe
    cliente_id = input("Ingrese el ID del cliente: ")
    cliente_nombre = ""
    with open("clientes.csv", "r") as file:
        for fila in file:
            partes = fila.strip().split(";")
            if partes[0] == cliente_id:
                cliente_nombre = partes[1]
                break
    if cliente_nombre == "":
        print(" Cliente no encontrado.")
        return

    # ------------------------------------------Obtener el número de factura
    factura_id = 1
    if os.path.exists("facturas.csv"):
        with open("facturas.csv", "r") as file:
            lineas = file.readlines()
            if lineas:
                ultima = lineas[-1].split(";")[0]
                factura_id = int(ultima) + 1

    # ---------------------------------------Ingreso de productos a la venta
    carrito = []
    total = 0
    seguir = True
    while seguir:
        listar_productos()
        prod_id = input("Ingrese el ID del producto a vender: ")
        cantidad = int(input("Cantidad: "))

        encontrado = False
        productos_actualizados = []
        with open("productos.csv", "r") as file:
            for fila in file:
                partes = fila.strip().split(";")
                if partes[0] == prod_id:
                    encontrado = True
                    tipo = partes[1]
                    sabor = partes[2]
                    stock = int(partes[3])
                    precio = int(partes[4])
                    if cantidad > stock:
                        print("No hay suficiente stock.")
                        return
                    subtotal = cantidad * precio
                    carrito.append([prod_id, tipo, sabor, cantidad, precio, subtotal])
                productos_actualizados.append(partes)

        if not encontrado:
            print("Producto no encontrado.")
            return

        continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
        seguir = continuar == "s"


    #------------------------------------------Guardar {id}.csv
    nombre_archivo_factura = f"{factura_id}.csv"
    with open(nombre_archivo_factura, "w") as factura:
        factura.write("producto_id;nombre_producto;sabor;cantidad;precio_unitario;subtotal\n")
        for item in carrito:
            factura.write(";".join(str(x) for x in item) + "\n")
            total += item[5]
        factura.write(f"TOTAL;;;;;{total}\n")

    #----------------------------------------Agregar a facturas.csv
    with open("facturas.csv", "a") as resumen:
        resumen.write(f"{factura_id};{cliente_id};{cliente_nombre};{total}\n")

    #-----------------------------------Actualizar productos.csv con nuevo stock
    nuevos_datos = []
    for partes in productos_actualizados:
        for item in carrito:
            if partes[0] == item[0]:  # la misma id
                partes[3] = str(int(partes[3]) - item[3])  # restamos la cantidad
        nuevos_datos.append(";".join(partes) + "\n")

    with open("productos.csv", "w") as file:
        file.writelines(nuevos_datos)

    print(f"Venta registrada con éxito. Factura #{factura_id}")
    input("Presiona Enter para continuar...")


menu_principal()





















# def menu_facturas():
    
#     activo=True
#     while(activo):
#         os.system("cls")
#         print("************** MENU DE FACTURAS **************")
#         print("""
#             1.CREAR FACTURA
#             2.LISTAR FACTURAS
#             3.BUSCAR FACTURAS POR ID
#             4.ACTUALIZAR FACTURAS
#             5.ELIMINAR FACTURAS
#             0.SALIR    
#             """)
#         opcUsuario=int(input("INGRESE SU ELECCION: "))
#         match (opcUsuario):
#             case 1: pass
#             case 2: pass
#             case 3:pass
#             case 4:pass
#             case 0: 
#                 print("*************HASTA LA VISTA BBY***************")
#                 activo=False
#             case _:print("OPC INCORRECTA")










este_es_el_nuevo_codigooooooooo= 2