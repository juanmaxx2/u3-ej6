import json
from pathlib import Path
from aparatosElectronicos import AparatosElectronicos
from televisor import Televisor
from heladera import Heladera
from lavarropa import Lavarropa
class ObjectEncoder(object):

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                AparatosElectronicos=d['AparatosElectronicos']
                dAparato = AparatosElectronicos[0]
                manejador=class_()
                for i in range(len(AparatosElectronicos)):
                    dAparato=AparatosElectronicos[i]
                    class_name=dAparato.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAparato['__atributos__']
                    unaparato=class_(**atributos)
                    manejador.AgregarAparatosElectronicos(unaparato)
            return manejador

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)