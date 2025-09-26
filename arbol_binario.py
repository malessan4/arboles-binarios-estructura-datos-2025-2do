class nodo_arbol(object):
    #clase nodo arbol
    def __init__(self,info):
        #crea un nodo con la información
        self.izquierda = None
        self.derecha = None
        self.informacion = info

class ArbolBinario:
    def __init__(self):
        self.raiz = None