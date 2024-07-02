
import csv
from random import *

lista_pedido = []
menu_1 = True

num_pedido = num_pedido = randint(1,1000) 

datos_cliente = {"nroPedido": num_pedido, "nombre":"", "apellido":"", "direccion":"", "saco_20kg":0, "saco_10kg":0, "saco_20kg":0, "sector" :0 }




def registrar_pedido( ):
     lista_pedido.append (datos_cliente)
   
  
    
    
def listar_pedido():
   print(datos_cliente)
   return(datos_cliente)

def imprimir_hoja_de_ruta():
    print(datos_cliente["sector"])
    
   
def menu ():
    print("-"*50)
    print("Bienvenido a Cat_Premium, este es nuestro menu")
    print("-"*50)
    print("Opcion_1 / Registrar_pedido")
    print("Opcion_2 / Listar_pedido")
    print("Opcion_3 / imprimir_hoja_de_ruta")
    print("Opcion_4 / Salir")

def menu_2 ():
    menu ()
    print("-"*50)
    print("En cual de estos sectores vives: ")
    print("-"*50)
    print("Opcion_1 /San Bernado")
    print("Opcion_2 / Calera de Tango")
    print("Opcion_3 / Buin")




while menu_1 == True:
   menu()

   op = int(input("\nPor favor, Ingrese una opcion entre los del menu: "))
   

   if op == 1 :
        datos_cliente["nombre"] = input("\Por favor ingrese su nombre: ")
        try:
            if not datos_cliente["nombre"]  == '':
                datos_cliente["apellido"] = input("\nPor favor ingrese su apellido: ")
                if not datos_cliente["apellido"]  == '':
                    datos_cliente["direccion"] = input("\nPor favor ingrese su direccion: ") 
                    datos_cliente["saco_5kg"] = int(input("\nVas a querer sacos de 5kg? en caso de que si indique cuantas: "))
                    datos_cliente["saco_10kg"] = int(input("\nVas a querer sacos de 10kg? en caso de que si indique cuantas: "))
                    datos_cliente["saco_20kg"] = int(input("\nVas a querer sacos de 20kg? en caso de que si indique cuantas: "))
                   
                    menu_2()

                    op2 = int(input("\nPor favor, Ingrese una opcion entre los del menu_2: "))
                    if op2 == 1 :
                        datos_cliente["sector"] = "San Bernado"
                    elif op2 == 2 :
                        datos_cliente["sector"] = "Calera de Tango"
                    elif op2 == 3:
                        datos_cliente["sector"] = "Buin"
                        break
                    else:
                        print(" la opcion no existe!")
                        menu_1 = True
            else:
                print("DEBE INGRESAR SU NOMBRE Y SU APELLIDO")
                menu_1 = True
        except ValueError:
            print("Error de tipos de datos")
            menu_1 = True

   elif op == 2 :
       listar_pedido()
       

   elif op == 3:
        imprimir_hoja_de_ruta()

   elif op == 4 :
        resp = int(input("\nestas seguro que quieres salir? "))
        print("si estas seguro presione 1 en caso contrario presione 2")
        if resp == 1 :
            print("Hasta luego!")
            menu_1 = False
            break
        else :
            menu_1 = True
       
       
       
      
      

