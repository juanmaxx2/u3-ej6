from aparatosElectronicos import AparatosElectronicos
class Televisor(AparatosElectronicos):
    __TipodePantalla=None
    __Pulgadas=None
    __TipodeDefinición=None
    __ConexionaInternet=None

    def __init__(self,Marca,Modelo,Color,PaisdeFabricacion,PrecioBase,TipodePantalla,Pulgadas,TipodeDefinición,ConexionaInternet):
        super.__init__(Marca,Modelo,Color,PaisdeFabricacion,PrecioBase)
        self.__TipodePantalla=TipodePantalla
        self.__Pulgadas=Pulgadas
        self.__TipodeDefinición=TipodeDefinición
        self.__ConexionaInternet=ConexionaInternet
    
    def getTipodePantalla(self):
        return self.__TipodePantalla

    def getPulgadas(self):
        return self.__Pulgadas
    
    def getTipodeDefinicion(self):
        return self.__TipodeDefinición
    
    def getConexionInternet(self):
        return self.__ConexionaInternet

    def getPrecioVenta(self):
        precio=self.getPrecioBase()
        if self.getTipodeDefinicion()=='SD':
            precio+=(((self.getPrecioBase()*1)/100)+precio)
        elif self.getTipodeDefinicion()=='HD':
            precio+=(((self.getPrecioBase()*2)/100)+precio)
        elif self.getTipodeDefinicion()=='FULL HD':
            precio+=(((self.getPrecioBase()*3)/100)+precio)
        if self.getConexionInternet()=='Vedadero':
            precio+=(((self.getPrecioBase()*10)/100)+precio)
        return precio