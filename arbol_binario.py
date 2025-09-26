class nodo_arbol(object):
    #clase nodo arbol
    def __init__(self, info):
        #crea un nodo con la información
        self.izquierda = None
        self.derecha = None
        self.informacion = info

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def arbol_vacio(raiz):
        return raiz == None

    def insertar_nodo(raiz, dato):
        # inserto el dato en el árbol
        if arbol_vacio(raiz):
            raiz = nodo_arbol(dato)
        elif(raiz.informacion <= dato):
            raiz.derecha = insertar_nodo(raiz.derecha, dato)
        else:
            raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
        #una vez actualizado el dato se retorna la raiz
        return raiz


# Crear un árbol binario
arbol = ArbolBinario()

