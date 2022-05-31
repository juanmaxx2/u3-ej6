from aparatosElectronicos import AparatosElectronicos
from televisor import Televisor
from heladera import Heladera
from lavarropa import Lavarropa
from lista import Lista
class Manejador:
    __Lista=None
    
    def __init__(self):
        self.__Lista=Lista()
    
    def Iniciar(self):
        tipo=input('Ingrese el tipo de aparato electronico(1.Televisor,2.Heladera,3.Lavarropa):')
        if tipo=='1' or tipo=='2' or tipo=='3':    
            if tipo=='1':
                Marca=input('\nIngrese la Marca:')
                Modelo=input('Ingrese el Modelo:')
                Color=input('Ingrese el color:')
                PaisdeFabricacion=input('Ingrese el pais de fabricacion:')
                PrecioBase=input('Ingrese el precio:')
                TipodePantalla=input('Ingrese el tipo de pantalla:')
                Pulgadas=input('Ingrese las pulgadas:')
                TipodeDefinición=input('Ingrese el tipo de definicion:')
                ConexionaInternet=input('Ingrese Verdadero si tiene conexion a interneto o Falso si no lo tiene:')
                unTelevisor=Televisor(Marca,Modelo,Color,PaisdeFabricacion,PrecioBase,TipodePantalla,Pulgadas,TipodeDefinición,ConexionaInternet)
                unAparato=unTelevisor
            elif tipo=='2':
                Marca=input('\nIngrese la Marca:')
                Modelo=input('Ingrese el Modelo:')
                Color=input('Ingrese el color:')
                PaisdeFabricacion=input('Ingrese el pais de fabricacion:')
                PrecioBase=input('Ingrese el precio:')
                CapacidadenLitros=input('Ingrese la capacidad en litros(solo el numero):')
                Freezer=input('Ingrse Verdadero si tiene freezer o Falso si no lo tiene:')
                Ciclica=input('Ingrse Verdadero si es ciclica o Falso si no lo es:')
                unaHeladera=Heladera(Marca,Modelo,Color,PaisdeFabricacion,PrecioBase,CapacidadenLitros,Freezer,Ciclica)
                unAparato=unaHeladera
            elif tipo=='3':
                Marca=input('\nIngrese la Marca:')
                Modelo=input('Ingrese el Modelo:')
                Color=input('Ingrese el color:')
                PaisdeFabricacion=input('Ingrese el pais de fabricacion:')
                PrecioBase=input('Ingrese el precio:')
                CapacidaddeLavado=input('Ingrse la capacidad de lavado(solo en numero):')
                VelocidaddeCentrifugado=input('Ingrese la velocidad de lavado(solo el numero):')
                CantidaddeProgramas=input('Ingrese la cantidad de programas:')
                TipodeCarga=input('Ingrese el tipo de carga:')
                unLavarropa=Lavarropa(Marca,Modelo,Color,PaisdeFabricacion,PrecioBase,CapacidaddeLavado,VelocidaddeCentrifugado,CantidaddeProgramas,TipodeCarga)
                unAparato=unLavarropa
        else:
            print('opcion incorrecta o no se encuentra')
        return unAparato

    def AgregarAparato(self,aparato):
        self.__Lista.AgregarAparatoElectronico(aparato)

    def InsetarAparato(self,aparato,pos):
        self.__Lista.Insertar(aparato,pos)

    def Mostrar(self):
        for dato in self.__Lista:
            print(dato)

    def MostrarTipo(self,pos):
        self.__Lista.MostrarTipo(pos)
    
    def CantidadPhillips(self):
        cant=0
        for dato in self.__Lista:
            if dato.getMarca().lower()=='Phillips' or dato.getMarca().lower()=='phillips' or dato.getMarca().lower()=='PHILLIPS':
                cant+=1
        print('La cantidad de aparatos phillips es:{}'.format(cant))
    
    def CargaSuperior(self):
        for dato in self.__Lista:
            if isinstance(dato,Lavarropa):
                if dato.getTipodeCarga()=='Superior' or dato.getTipodeCarga()=='superior' or dato.getTipodeCarga()=='SUPERIOR':
                    print('La marca del lavarropa es:{}'.format(dato.getMarca()))

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[AparatosElectronicos.toJSON() for AparatosElectronicos in self.__lista]
            )
        return d
    
    def GuardarJSON(self):
        listaJSON = [AparatosElectronicos.toJSON() for AparatosElectronicos in self.__lista]
        return listaJSON