from aparatosElectronicos import AparatosElectronicos
class Heladera(AparatosElectronicos):
    __CapacidadenLitros=None
    __Freezer=None
    __Ciclica=None

    def __init__(self,Marca,Modelo,Color,PaisdeFabricacion,PrecioBase,CapacidadenLitros,Freezer,Ciclica):
        super.__init__(Marca,Modelo,Color,PaisdeFabricacion,PrecioBase)
        self.__CapacidadenLitros=CapacidadenLitros
        self.__Freezer=Freezer
        self.__Ciclica=Ciclica

    def getCapacidadenLitros(self):
        return self.__CapacidadenLitros

    def getFreezer(self):
        return self.__Freezer

    def getCiclica(self):
        return self.__Ciclica
    
    def getPrecioVenta(self):
        precio=self.getPrecioBase()
        if self.getFreezer()=="Falso":
            precio+=(((self.getPrecioBase()*1)/100)+precio)
        elif self.getFreezer()=="Verdadero":
            precio+=(((self.getPrecioBase()*5)/100)+precio)
        if self.getCiclica=='Verdadero':
            precio+=(((self.getPrecioBase()*10)/100)+precio)
        return precio
