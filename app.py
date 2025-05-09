import os
from datetime import datetime
from TAD_Pila_Exp import *
from TadExpediente import *

pila1=crearPila()
pila2=crearPila()
pilaNueva=crearPila()

resp=0
while resp==0:
    os.system("cls" if os.name == "nt" else "clear")
    print("Bienvenido al Estudio Jurídico")
    print("-------"*5)
    print("1 - Agregar expediente")
    print("2 - Modificar expediente por número")
    print("3 - Eliminar expediente por número")
    print("4 - Listar expedientes")
    print("5 - Modificar hora de expedientes según dos fechas dadas")
    print("6 - Generar pila de expedientes según dos fechas dadas")
    print("7 - Eliminar expedientes según mes")
    print("8 - Salir")
    print("-------"*5)
    respMenu=int(input("Ingrese la opción deseada -->  "))
    os.system("cls" if os.name == "nt" else "clear")

    if respMenu==1:
        exp=CrearExpediente()
        num=int(input("Ingrese el número de expediente:  "))
        tit=input("Ingrese titular del expediente:  ")
        tra=input("Ingrese trámite del expediente:  ")
        cond=False
        while cond==False:
            try:
                fec=input("Ingrese fecha de presentación del expediente con formato 'AAAA-MM-DD HH:MM'  ")
                fec=datetime.datetime.strptime(fec, "%Y-%m-%d %H:%M")
                cond=True
                if fec>datetime.datetime.now():
                    print("Fecha inválida.")
                    cond=False
            except ValueError:
                print("Fecha inválida.")
        CargarExpediente(exp,num,tit,tra,fec)
        apilar(pila1,exp)
        print("Expediente cargado exitosamente.")
        os.system("pause")

    elif respMenu==2:
        if esVacia(pila1):
            print("No hay expedientes en la pila.")
            os.system("pause")
        else:   
            aux=int(input("Ingrese el número del expediente a modificar:  "))
            marca=0
            for i in range (0,tamanio(pila1)):
                exp=desapilar(pila1)
                if aux==VerNumero(exp):
                    marca=1
                    op=int(input("Ingrese el campo a modificar del expediente:  \n1 - Titular  \n2 - Trámite  \n3 - Fecha  \n  "))
                    if op==1:
                        nuevoTit=input("Ingrese nuevo titular:  ")
                        ModiTitular(exp,nuevoTit)
                        print("Titular modificado exitosamente.")
                        os.system("pause")
                    elif op==2:
                        nuevoTram=input("Ingrese nuevo trámite:  ")
                        ModiTramite(exp,nuevoTram)
                        print("Trámite modificado exitosamente.")
                        os.system("pause")
                    elif op==3:
                        cond=False
                        while cond==False:
                            try:
                                nuevafec=input("Ingrese nueva fecha de presentación del expediente con formato 'AAAA-MM-DD HH:MM'  ")
                                nuevafec=datetime.datetime.strptime(nuevafec, "%Y-%m-%d %H:%M")
                                cond=True
                                if nuevafec>datetime.datetime.now():
                                    print("Fecha inválida.")
                                    cond=False
                            except ValueError:
                                print("Fecha inválida.")
                        ModiFecha(exp,nuevafec)
                        print("Fecha modificada exitosamente.")
                        os.system("pause")
                    else:
                        print("Opción incorrecta")
                apilar(pila2,exp)
            if marca==0:
                print("No se ha encontrado expediente con dicho número.")
                os.system("pause")
            #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
            for j in range(0,tamanio(pila2)):      
                exp=desapilar(pila2)
                apilar(pila1,exp)         

    elif respMenu==3:
        if esVacia(pila1):
            print("No hay expedientes en la pila.")
            os.system("pause")
        else:   
            aux=int(input("Ingrese el número del expediente a eliminar:  "))
            marca=0
            for i in range(0,tamanio(pila1)):
                exp=desapilar(pila1)
                if aux!=VerNumero(exp):
                    apilar(pila2,exp)
                else:
                    marca=1
                    print("Expediente Nº ", VerNumero(exp), " eliminado exitosamente.")
                    os.system("pause")
            if(marca==0):
                print("No se ha encontrado el número de expediente a eliminar.")
                os.system("pause")
            #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
            for j in range(0,tamanio(pila2)):      
                exp=desapilar(pila2)
                apilar(pila1,exp)         

    elif respMenu==4:
        if esVacia(pila1):
            print("No hay expedientes en la pila.")
            os.system("pause")
        else:
            for i in range(0,tamanio(pila1)):
                exp=desapilar(pila1)
                print("-------"*7)
                print("-------"*7)
                print("Número de expediente:  ",VerNumero(exp))
                print("Titular:  ",VerTitular(exp))
                print("Trámite:  ",VerTramite(exp))
                print("Fecha de presentación:  ", VerFecha(exp))
                apilar(pila2,exp)
        #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
        for j in range(0,tamanio(pila2)):      
            exp=desapilar(pila2)
            apilar(pila1,exp)     
        os.system("pause")
   
    elif respMenu==5:
        print("Ingrese el rango de fechas de expedientes a modificar, ingresando primero la más antigua.")
        cond=False
        while cond==False:
            try:
                fecha1=input("Ingrese primera fecha con formato 'AAAA-MM-DD'  ")
                fecha1=datetime.datetime.strptime(fecha1, "%Y-%m-%d")
                cond=True
                if fecha1>datetime.datetime.now():
                    print("Fecha inválida.")
                    cond=False
            except ValueError:
                print("Fecha inválida.")
        cond=False
        while cond==False:
            try:
                fecha2=input("Ingrese segunda fecha con formato 'AAAA-MM-DD'  ")
                fecha2=datetime.datetime.strptime(fecha2, "%Y-%m-%d")
                cond=True
                if fecha2>datetime.datetime.now():
                    print("Fecha inválida.")
                    cond=False
            except ValueError:
                print("Fecha inválida.")
        hora=int(input("Ingrese nueva hora:  "))
        while hora<0 or hora>23:
            hora=int(input("Hora errónea, ingresela nuevamente:  "))
            os.system("cls" if os.name == "nt" else "clear")
        minutos=int(input("Ingrese minutos:  "))
        while((minutos>59) or (minutos<0)):
            minutos=int(input("Minutos erróneo, ingreselo nuevamente:  "))
            os.system("cls" if os.name == "nt" else "clear")
        marca=0
        for i in range (0,tamanio(pila1)):  
            exp=desapilar(pila1)
            if fecha1<=VerFecha(exp)<=fecha2:
                fechamod=datetime.datetime(VerAnio(exp),VerMes(exp),VerDia(exp),hora,minutos)
                ModiFecha(exp,fechamod)
                marca=1           
            apilar(pila2,exp)    
        #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
        for j in range(0,tamanio(pila2)):      
            exp=desapilar(pila2)
            apilar(pila1,exp)  
        if marca==0:
            print("No existen expedientes en ese rango.")
        else:
            print("La modificación se realizó exitosamente.")
        os.system("pause")
  
    elif respMenu==6:
        print("Ingrese el rango de fechas de expedientes a apilar, ingresando primero la más antigua.")
        cond=False
        while cond==False:
            try:
                fecha1=input("Ingrese primera fecha con formato 'AAAA-MM-DD'  ")
                fecha1=datetime.datetime.strptime(fecha1, "%Y-%m-%d")
                cond=True
                if fecha1>datetime.datetime.now():
                    print("Fecha inválida.")
                    cond=False
            except ValueError:
                print("Fecha inválida.")
        cond=False
        while cond==False:
            try:
                fecha2=input("Ingrese segunda fecha con formato 'AAAA-MM-DD'  ")
                fecha2=datetime.datetime.strptime(fecha2, "%Y-%m-%d")
                cond=True
                if fecha2>datetime.datetime.now():
                    print("Fecha inválida.")
                    cond=False
            except ValueError:
                print("Fecha inválida.")
        os.system("cls" if os.name == "nt" else "clear")
        marca=0
        for i in range (0,tamanio(pila1)):  
            exp=desapilar(pila1)
            if fecha1<=VerFecha(exp)<=fecha2:
                apilar(pilaNueva,exp)
                apilar(pila2,exp) 
                marca=1
            else:
                apilar(pila2,exp)          
        #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
        for j in range(0,tamanio(pila2)):      
            exp=desapilar(pila2)
            apilar(pila1,exp)  
        if marca==0:
            print("No existen expedientes en ese rango.")
        else:
            print("La nueva pila se generó exitosamente con los siguiente expedientes:")
            for k in range(0,tamanio(pilaNueva)):
                exp=desapilar(pilaNueva)
                print("-------"*7)
                print("-------"*7)
                print("Número de expediente:  ",VerNumero(exp))
                print("Titular:  ",VerTitular(exp))
                print("Trámite:  ",VerTramite(exp))
                print("Fecha de presentación:  ", VerFecha(exp))
                apilar(pila2,exp)
            #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
            for j in range(0,tamanio(pila2)):      
                exp=desapilar(pila2)
                apilar(pilaNueva,exp)     
        os.system("pause")

    elif respMenu==7:
        print("Ingrese mes de los expedientes a eliminar.")
        mes=int(input("Ingrese mes:  "))
        while mes>12 or mes<1:
            mes=int(input("Mes erróneo, ingreselo nuevamente:  "))
            os.system("cls" if os.name == "nt" else "clear")
        marca=0
        for i in range (0,tamanio(pila1)):  
            exp=desapilar(pila1)
            if VerMes(exp)==mes:
                print("Expediente N° ", VerNumero(exp), " eliminado exitosamente.")
                marca=1     
            else:
                apilar(pila2,exp)                                       
        #BUCLE PARA RESPETAR LA POLITICA DE PILA (LIFO)
        for j in range(0,tamanio(pila2)):      
            exp=desapilar(pila2)
            apilar(pila1,exp)  
        if marca==0:
            print("No existen expedientes en ese rango.")
        os.system("pause")

    elif respMenu==8:
        break

    else:
        print("Opción incorrecta, intentelo nuevamente...")
        os.system("pause")