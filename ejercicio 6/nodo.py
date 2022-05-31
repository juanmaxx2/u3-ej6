class Nodo:
    __AparatoElectronico=None
    __Siguiente=None

    def __init__(self, AparatoElectronico):
        self.__AparatoElectronico=AparatoElectronico
        self.__Siguiente=None

    def getSiguiente(self):
        return self.__Siguiente
        
    def getDato(self):
        return self.__AparatoElectronico

    def setSiguiente(self, Siguiente):
        self.__Siguiente=Siguiente

    