#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, time
from tkinter import CENTER

def Admin_poduc():
    while True:
        try:
            print("╔═════════════════════════════════╗")
            print("║       Menu de productos:        ║")
            print("║   1.Lista de productos          ║")
            print("║   2.Dar de alta producto        ║")
            print("║   4.Dar de baja de producto     ║")
            print("║   3.Salir                       ║")
            print("╚═════════════════════════════════╝")
            opc_pro = int(input("Ingrese su opcion: "))
            if opc_pro == 1:
                print("Lista de productos: ")
                input("Presiona Enter para continuar:")
            elif opc_pro == 2:
                dar_alta = input("Ingresa el producto:")
                print()
            elif opc_pro == 3:
                dar_baja = input("Dar de baja producto")
            elif opc_pro == 4:
                break
        except:
            print("El dato no es valido.")

def Admin_pers():
    while True:
        try:
            print("╔═════════════════════════════════╗")
            print("║       Menu de personal:         ║")
            print("║   1.Lista de personal           ║")
            print("║   2.Dar de alta personal        ║")
            print("║   3.Dar de baja personal        ║")
            print("║   4.Salir                       ║")
            print("╚═════════════════════════════════╝")
            opc_per = int(input("Ingrese su opcion: "))
            if opc_per == 1:
                print("Lista de personal: ")
                input("Presiona Enter para continuar:")
            elif opc_per == 2:
                dar_alta_per= input("Dar de alta personal: ")
                print()
            elif opc_per == 3:
                dar_baja_per = input("Dar de baja producto")
            elif opc_per == 4:
                break
        except:
            print()
def Admin_credi():
    while True:
        try:
            print("╔═════════════════════════════════╗")
            print("║       Menu de credito:          ║")
            print("║   1.Lista de credito            ║")
            print("║   2.Ingresar credito            ║")
            print("║   3.Pagar credito               ║")
            print("║   4.Salir                       ║")
            print("╚═════════════════════════════════╝")
            opc_cre = int(input("Ingrese su opcion: "))
            if opc_cre == 1:
                print("Lista de creditos: ")
                input("Presiona Enter para continuar:")
            elif opc_cre == 2:
                dar_nuevo_cred= input("Ingrese Credito: ")
                print()
            elif opc_cre == 3:
                dar_pagar_cred = input("Pago de credito de cliente: ")
            elif opc_cre == 4:
                break
        except:
            print()
car = "     ▄"
car2 = "▄"
Men = ["╔╗──╔╗──╔╗─────────────────────────────╔╗", "║╚╗╔╝║─╔╝╚╗────────────────────────────║║",
    "╚╗║║╔╬═╩╗╔╬══╦═╗╔╗─╔╗╔══╦══╦══╦══╦╦══╦═╝╠══╦══╗","─║╚╝╠╣╔═╣║║╔╗║╔╝║║─║║║╔╗║══╣╔╗║╔═╬╣╔╗║╔╗║╔╗║══╣",
    "─╚╗╔╣║╚═╣╚╣╚╝║║─║╚═╝║║╔╗╠══║╚╝║╚═╣║╔╗║╚╝║╚╝╠══║","──╚╝╚╩══╩═╩══╩╝─╚═╗╔╝╚╝╚╩══╩══╩══╩╩╝╚╩══╩══╩══╝",
    "────────────────╔═╝║","────────────────╚══╝"]
    
for i in range(8):
    print(Men[i])
time.sleep(10)
for i in range(21):
    os.system("cls")
    print(car)
    if i > 19:
        print("       Carga completada")
    elif i < 20:
        print("           Cargando")
    
    
    car = car + car2
    time.sleep(1)

input("\nPor favor presione la tecla Enter para continuar:")
os.system("cls")

while True:
    try:
        print("╔═════════════════════════════════╗")
        print("║      Inicio de secion:          ║")
        print("╚═════════════════════════════════╝")
        val1 = input("Ingrese su cuanta:")
        val2 = int(input("Ingresar su conraseña:"))
        if (val1 == "admin" and val2 == 1234):
            break
        else:
            os.system("cls")
            print("El dato no es valido.")
    except:
        print("El dato no es correcto.")

while True:
    try:
        print("╔═════════════════════════════════╗")
        print("║             Menu:               ║")
        print("║   1.Administrar productos       ║")
        print("║   2.Administrar personal        ║")
        print("║   3.Creditos                    ║")
        print("║   4.Salir                       ║")
        print("╚═════════════════════════════════╝")
        opc_0 = int(input("Ingrese la opcion: "))
        if opc_0  == 1:
            print("Administrar productos")
            Admin_poduc()
        elif opc_0 == 2:
            print("2.Administrar personal")
            Admin_pers()
        elif opc_0 == 3:
            print("3.Administrar creditos")
            Admin_credi()
        elif opc_0 == 4:
            break
        else:
            print("Error")
    except:
        print("El dato no es numérico")
