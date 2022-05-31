from abc import abstractmethod
import json
from pathlib import Path
class AparatosElectronicos:
    __Marca=None
    __Modelo=None
    __Color=None
    __PaisdeFabricacion=None
    __PrecioBase=None

    def __init__(self,Marca,Modelo,Color,PaisdeFabricacion,PrecioBase):
        self.__Marca=Marca
        self.__Modelo=Modelo
        self.__Color=Color
        self.__PaisdeFabricacion=PaisdeFabricacion
        self.__PrecioBase=PrecioBase

    def getMarca(self):
        return self.__Marca

    def getModelo(self):
        return self.__Modelo

    def getColor(self):
        return self.__Color

    def getPaisdeFabricacion(self):
        return self.__PaisdeFabricacion

    def getPrecioBase(self):
        return self.__PrecioBase

    @abstractmethod
    def toJSON(self):
        pass