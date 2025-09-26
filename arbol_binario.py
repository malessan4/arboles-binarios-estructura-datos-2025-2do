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
        return self.raiz == None

    def insertar(self, dato):
        # inserto el dato en el árbol (método público)
        self.raiz = self._insertar_recursivo(self.raiz, dato)
        
    def _insertar_recursivo(self, nodo_actual, dato):
        # inserto el dato en el árbol (método privado)
        if nodo_actual is None:
            return nodo_arbol(dato)
        elif dato >= nodo_actual.informacion:
            nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, dato)
        else:
            nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, dato)
        return nodo_actual

        def inorden(self):
        """Recorrido inorden"""
        self._inorden_recursivo(self.raiz)
        print()

    def _inorden_recursivo(self, nodo):
        """Método privado para inorden"""
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda)
            print(nodo.informacion, end=" ")
            self._inorden_recursivo(nodo.derecha)

    def buscar(self, dato):
        """Busca un dato en el árbol"""
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        """Método privado para búsqueda"""
        if nodo is None:
            return False
        if dato == nodo.informacion:
            return True
        elif dato > nodo.informacion:
            return self._buscar_recursivo(nodo.derecha, dato)
        else:
            return self._buscar_recursivo(nodo.izquierda, dato)

# PROGRAMA PRINCIPAL
def main():
    arbol = ArbolBinario()  # Crear instancia del árbol
    
    while True:
        print("\n" + "="*50)
        print("          MENÚ ÁRBOL BINARIO (POO)")
        print("="*50)
        print("1. Insertar nodo")
        print("2. Mostrar árbol (Inorden)")
        print("3. Buscar nodo")
        print("4. Verificar si está vacío")
        print("5. Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                dato = int(input("Ingrese el número a insertar: "))
                arbol.insertar(dato)
                print(f"✓ Nodo {dato} insertado correctamente")
            except ValueError:
                print("✗ Error: Ingrese un número válido")
                
        elif opcion == "2":
            if arbol.arbol_vacio():
                print("El árbol está vacío")
            else:
                print("Recorrido Inorden:", end=" ")
                arbol.inorden()
                
        elif opcion == "3":
            if arbol.arbol_vacio():
                print("El árbol está vacío")
            else:
                try:
                    dato = int(input("Ingrese el número a buscar: "))
                    if arbol.buscar(dato):
                        print(f"✓ El número {dato} SÍ está en el árbol")
                    else:
                        print(f"✗ El número {dato} NO está en el árbol")
                except ValueError:
                    print("✗ Error: Ingrese un número válido")
                    
        elif opcion == "4":
            if arbol.arbol_vacio():
                print("✓ El árbol está vacío")
            else:
                print("✗ El árbol NO está vacío")
                
        elif opcion == "5":
            print("¡Hasta luego!")
            break
            
        else:
            print("✗ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()