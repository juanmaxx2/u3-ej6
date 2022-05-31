from aparatosElectronicos import AparatosElectronicos
class Lavarropa(AparatosElectronicos):
    __CapacidaddeLavado=None
    __VelocidaddeCentrifugado=None
    __CantidaddeProgramas=None
    __TipodeCarga=None

    def __init__(self,Marca,Modelo,Color,PaisdeFabricacion,PrecioBase,CapacidaddeLavado,VelocidaddeCentrifugado,CantidaddeProgramas,TipodeCarga):
        super.__init__(Marca,Modelo,Color,PaisdeFabricacion,PrecioBase)
        self.__CapacidaddeLavado=int(CapacidaddeLavado)
        self.__VelocidaddeCentrifugado=VelocidaddeCentrifugado
        self.__CantidaddeProgramas=CantidaddeProgramas
        self.__TipodeCarga=TipodeCarga
    
    def getCapacidaddeLavado(self):
        return self.__CapacidaddeLavado

    def getVelocidaddeCentrifugado(self):
        return self.__VelocidaddeCentrifugado

    def getCantidaddeProgramas(self):
        return self.__CantidaddeProgramas

    def getTipodeCarga(self):
        return self.__TipodeCarga
    
    def getPrecioVenta(self):
        precio=self.getPrecioBase()
        if self.getCapacidaddeLavado()>=5:
            precio+=(((self.getPrecioBase()*1)/100)+precio)
        elif self.getCapacidaddeLavado()<5:
            precio+=(((self.getPrecioBase()*3)/100)+precio)
        return precio
