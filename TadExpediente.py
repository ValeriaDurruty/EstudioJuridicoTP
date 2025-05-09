#Tad Expediente
#Permite almacenar los datos de un expediente.

    # Expediente = {
    #     numero: Int
    #     titular: String
    #     tramite: String
    #     fecha: datetime
    # }

#===================================================================#

#Especificación TAD expedientes

#CrearExpediente():
    #Crea un expediente vacio

#CargarExpediente(expediente):
    #carga los datos del expediente

#VerNumero(expediente):
    #retorna el numero de expediente

#VerTitular(expediente):
    #retorna el titular del expediente

#VerTramite(expediente):
    #retorna el tipo de tramite

#VerFecha(expediente):
    #retorna la fecha del expediente

#VerAnio(expediente):
    #retorna año del expediente

#VerMes(expediente):
    #retorna mes del expediente

#VerDia(expediente):
    #retorna dia del expediente

#VerHora(expediente):
    #retorna hora del expediente

#VerMinuto(expediente):
    #retorna minuto del expediente

#ModiNumero(expediente,Otronumero):
    #modifica el numero de expediente

#ModiTitular(expediente,Otrotitular):
    #modifica el titular del expediente

#ModiTramite(expediente,Otrotramite):
    #modifica el tipo de tramite del expediente

#ModiFecha(expediente,OtraFecha):
    #modifica la fecha del expediente

#asignar(expediente1,expediente2):
    #asigna los datos del expediente 1 al expediente 2

#Fin Especificación

#===================================================================#

import datetime

def CrearExpediente():
    #crea y retorna un expediente vacio
    expediente=[0,"","",datetime]
    return expediente

def CargarExpediente(expediente,numero,titular,tramite,fecha):
    #cargar los datos del expediente
    expediente[0]=numero
    expediente[1]=titular
    expediente[2]=tramite
    expediente[3]=fecha

def VerNumero(expediente):
    #retorna el numero de expediente
    return expediente[0]

def VerTitular(expediente):
    #retorna el titular del expediente
    return expediente[1]

def VerTramite(expediente):
    #retorna el tipo de tramite
    return expediente[2]

def VerFecha(expediente):
    #retorna la fecha del expediente
    return expediente[3]

def VerAnio(expediente):
    #retorna año del expediente
    return VerFecha(expediente).year

def VerMes(expediente):
    #retorna mes del expediente
    return VerFecha(expediente).month

def VerDia(expediente):
    #retorna dia del expediente
    return VerFecha(expediente).day

def VerHora(expediente):
    #retorna hora del expediente
    return VerFecha(expediente).hour

def VerMinuto(expediente):
    #retorna minuto del expediente
    return VerFecha(expediente).minute

def ModiNumero(expediente,Otronumero):
    #modifica el numero de expediente
    expediente[0]=Otronumero

def ModiTitular(expediente,Otrotitular):
    #modifica el titular del expediente
    expediente[1]=Otrotitular

def ModiTramite(expediente,Otrotramite):
    #modifica el tipo de tramite del expediente
    expediente[2]=Otrotramite

def ModiFecha(expediente,OtraFecha):
    #modifica la fecha del expediente
    expediente[3]=OtraFecha

def asignar(expediente1,expediente2):
    #asigna los datos del expediente 1 al expediente 2
    expediente1[0]=expediente2[0]
    expediente1[1]=expediente2[1]
    expediente1[2]=expediente2[2]
    expediente1[3]=expediente2[3]