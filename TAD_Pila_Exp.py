#TAD Pila Exp
#Permite almacenar una pila de expedientes

#===================================================================#

#Especificación TAD pila de expedientes

#crearPila():
    #Crea una pila de expedientes vacía
 
#esVacia(pila):
    #Retorna Verdadero si la pila no tiene elementos
 
#apilar(pila,elem):
    #Agrega un expediente al final de la pila
 
#desapilar(pila):
    #Retorna y elimina el último expediente de la pila
 
#tamanio(pila):
    #Retorna la cantidad de expedientes en la pila
 
#copiasPila(pila1,pila2):
    #Copia los datos de la pila 2 a la pila 1

#Fin Especificación

#===================================================================#

#crea una Pila vacía
def crearPila():
    pila=[]
    return pila

#Retorna Verdadero si la pila no tiene elementos
def esVacia(pila):
    return len(pila)==0

#Agrega un elemento al final de la pila
def apilar(pila,elem):
    pila.append(elem)

#Retorna y elimina el último elemento de la pila
def desapilar(pila):
    elem=pila.pop()
    return elem

#Retorna la cantidad de elementos de la pila
def tamanio(pila):
    return len(pila)

#Copia la pila 2 en la pila 1
def copiarPila(pila1,pila2):
    aux=crearPila()
    while not esVacia(pila2):
        elem=desapilar(pila2)
        apilar(aux,elem)
    while not esVacia(aux):
        elem=desapilar(aux)
        apilar(pila1,elem)
        apilar(pila2,elem)