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
            4. COMPRAR
            3. MENU FACTURAS
            0. PARA SALIR  
            
            
            """)
        
        opcion=int(input("INGRESA TU ELECCION: "))
        
        
        match(opcion):
            case 1:menu_usuarios()
            case 2:menu_clientes()
            case 3:menu_productos()
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


lista_empleados=[]
def agregar_usuario():
    id = int(input("INGRESE SU CC: "))
    nombre =input("INGRESE SU NOMBRE: ").lower()
    contraseña = (input("INGRESE SU CONTRASEÑA: "))
    rol = (input("INGRESAR ROL: "))
    with open("usuarios.csv","a") as file:
        file.write(f"{id};{nombre};{contraseña};{rol}\n")
        print('USUARIO AGREGADO CON EXITO')
        
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
    id=input("INGRESE EL ID DEL PRODUCTO: ")
    tipo= input("INGRESE EL TIPO DEL PRODUCTO(BOLIS,PALETA,HELADO CUADRADO,HELADO REDONDO): ")
    sabor=input("INGRESE EL SABOR(NARANJA,PIÑA,MORA,TRICOLOR,LIMON,ETC): ")
    stock= input("CANTIDAD DE PRODUCTO: ")
    precio=input("INGRESE PRECIO DEL PRODUCTO: ")
    with open("productos.csv","a") as file:
        file.write(f"{id};{tipo};{sabor};{stock};{precio}\n")
        print('PRODUCTO AGREGADO CON EXITO')


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
            2. PARA BUSCAR CLIENTE POR ID
            3. PARA LISTAR CLIENTE
            4. PARA ACTUALIZAR CLIENTES
            5. PARA ELIMINAR CLIENTES
            0. PARA SALIR                                                             
            """)
        opcUsuario=int(input("INGRESE SU ELECCION: "))
        match (opcUsuario):
            case 1: agregar_clientes()
            case 2: buscar_cliente_id()
            case 3: listar_clientes()
            case 4: actualizar_clientes()
            case 5: eliminar_clientes()
            case 0: 
                print("*************HASTA LA VISTA BBY***************")
                activo=False
            case _:print("OPC INCORRECTA")

lista_cliente = []
def agregar_clientes():
    id = int(input("INGRESE SU CC: "))
    nombre =input("INGRESE SU NOMBRE: ").lower()
    
    with open("clientes.csv","a") as file:
        file.write(f"{id};{nombre}\n")
        print('CLIENTE AGREGADO CON EXITO')

def buscar_cliente_id():
    print("************** BUSCAR CLIENTE POR ID*******************")
    id= input("INGRESE EL ID DEL CLIENTE A BUSCAR: ")

    with open("clientes.csv","r") as file:
        for fila in file:
            lista_fila = fila.split(';')
            
            if lista_fila[0] == id:
                print(fila.split(';'))
                print('ENCONTRAMOS CLIENTE')
                input("\nPresiona Enter para continuar...")
                print('\n ')
                break
                
        if lista_fila[0] != id:
            print('CLIENTE NO ENCONTRADO')
            input("\nPresiona Enter para continuar...")
    
    


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
                input("\nPresiona Enter para continuar...")
                print('\n ')
                
            else:
                print("CLIENTE ELIMINADO")

    with open("clientes.csv", "w") as file:
        for fila in lista_copia:
            file.write(fila) 



menu_principal()

# ******************************************************************************************************************
# def vender():
#     print ("**********************INICIAR VENTA***************************")






























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