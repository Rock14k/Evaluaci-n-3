from random import *
import csv
import os

def limpiezapantalla():
    os.system("cls")

limpiezapantalla()

menu_de_op = 1
sueldo_aleatorio = []
trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", 
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos = [["Nombres    ", "      Sueldo"]]
valor_datos = []
reporte= [["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"]]

def limpiear_pantalla():
    os.system("cls")


def menu ():
    print("-"*50)
    print("\nBienvenido a nuestro menu:  ")
    print("-"*50)
    print("Opcion_1 / Asignar sueldos_aleatorios.")
    print("Opcion_2 / Clasificar_sueldos.")
    print("Opcion_3 / Ver_estadisticas.")
    print("Opcion_4 / Reporte_de_sueldos")
    print("Opcion_5 / Salir_del_programa")

def agregar_sueldos():
    for trabajador in trabajadores:
        sueldo = randint(300000, 2500000)
        sueldos.append([trabajador, sueldo])
        valor_datos.append(sueldo)
    print(" los sueldos fueron agregados de manera correcta.")
    
def clasificar_sueldos():
    sueldo_menor = [["Nombres    ", "      Sueldo"]]
    sueldo_inter = [["Nombres    ", "      Sueldo"]]
    sueldo_mayor = [["Nombres    ", "      Sueldo"]]
    for y in sueldos[1:]:
        trabajador, sueldo = y
        if sueldo < 800000:
            sueldo_menor.append([trabajador, sueldo])
        elif sueldo >= 800000 or sueldo <= 2000000:
            sueldo_inter.append([trabajador, sueldo])
        elif sueldo > 2000000:
            sueldo_mayor.append([trabajador, sueldo])
    
    cant_sueldo_menor = int(len(sueldo_menor))
    print(f"Sueldos menores a $800.000\nTOTAL: {cant_sueldo_menor-1}")
    for i in sueldo_menor:
        print(i)
    print("")
    cant_sueldo_inter = int(len(sueldo_inter))
    print(f"Sueldos entre $800.000 y $2.000.000\nTOTAL: {cant_sueldo_inter-1}")
    for f in sueldo_inter:
        print(f)
    print("")
    cant_sueldo_mayor = int(len(sueldo_mayor))   
    print(f"Sueldos mayores a $2.000.000\nTOTAL: {cant_sueldo_mayor-1}")
    print("")
    total_sueldo = sum(valor_datos)
    print(f"TOTAL SUELDOS: ${total_sueldo}")
    

def media_geometria(geometria):
    producto = 1
    for valor in geometria:
        producto *= valor
    return producto ** (1-len(geometria))
    

def ver_estadisticas():
    total_sueldo = sum(valor_datos)
    mayor_sueldo = max(valor_datos)
    menor_sueldo = min(valor_datos)
    sueldo_prom= total_sueldo / int(len(valor_datos))

    print(f"El mayor sueldo en  nuestra lista es de: ${mayor_sueldo}")
    print(f"El menor sueldo en nuestra lista es de: ${menor_sueldo}")
    print(f"El Promedio de los sueldos es de : ${sueldo_prom}")
    print(f"Nuestra media geometica es de :{media_geometria(valor_datos):>6f}")
    print("")
  
def reporte_sueldos():
    for fila in sueldos[1:]:
        nombre, sueldobase = fila
        descsalud = round(sueldobase*0.07)
        descafp = round(sueldobase*0.12)
        sueldoliq = sueldobase-descsalud-descafp
        reporte.append([nombre, sueldobase, descsalud, descafp, sueldoliq])
    for rango1 in reporte:
        print(f"{rango1[0]:<18} {rango1[1]:<13} {rango1[2]:<13} {rango1[3]:<13} {rango1[4]:<13}")
    print("")
    with open ( 'reporte_sueldos.csv','w',newline='' ) as report_csv:
        escritor_csv = csv.writer(report_csv)
        escritor_csv.writerows(reporte)
    print("Se ha guardado el reporte en un archivo reporte_sueldos.csv ")
    print("")

def salir():
    print("\nFinalizando Programa...\nDesarrollado por Hawk Durant\nRUT 25753250-k")
    



while menu_de_op == 1:
    menu()
    try:
        opcion = int(input("Por favor elije una opcion en base a nuestro menu"))
        print("")
    except ValueError:
        print("Tiene que elegir un numero del 1 al 5.")
        continue
    if  opcion == 1:
        agregar_sueldos()
    elif opcion == 2:
        clasificar_sueldos()
    elif opcion == 3:
        ver_estadisticas() 
    elif opcion == 4:
        reporte_sueldos()  
    elif opcion == 5:
        salir()
        menu_de_op
        break
    else:
        print("Error!.")