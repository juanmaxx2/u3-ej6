class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=None

    def Iniciar(self,unManejador,encoder):
        while self.__opcion!='8':
            print('\n0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0')
            print('|                                                                                      |')
            print('0                                                                                      0')
            print('|     1.Agregar un aparato electronico en una posicion determinada.                    |')
            print('|     2.Agregar un aparato electronico.                                                |')
            print('|     3.Buscar un tipo de aparato electronico en una posicion.                         |')
            print('|     4.Mostrar cantidad aparatos que sean marca philips                               |')
            print('|     5.Mostrar marca de lavarropas con carga superior                                 |')
            print('|     6.Mostrar los datos de todos los aparatos electronicos                           |')
            print('|     7.Mostrar los datos de todos los aparatos electronicos                           |')
            print('|     8.Salir                                                                          |')
            print('0                                                                                      0')
            print('|                                                                                      |')
            print('0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0--0 \n')
            self.__opcion=input('\nIngrese la opcion a realizar:')
            if int(self.__opcion)>0 and int(self.__opcion)<=8:
                if self.__opcion=='1':
                    pos=input('Ingrese la posicion donde desea agregar el aparato electronico:')
                    aparato=unManejador.Iniciar()
                    unManejador.InsetarAparato(aparato,pos)
                elif self.__opcion=='2':
                    aparato=unManejador.Iniciar()
                    unManejador.AgregarAparato(aparato)
                elif self.__opcion=='3':
                    pos=input('Ingrese la posicion que desea mostrar:')
                    unManejador.MostrarTipo(pos)
                elif self.__opcion=='4':
                    unManejador.CantidadPhillips()
                elif self.__opcion=='5':
                    unManejador.CargaSuperior()
                elif self.__opcion=='6':
                    unManejador.Mostrar()
                elif self.__opcion=='7':
                    listaJSON = unManejador.guardarJSON()
                    encoder.guardarJSONArchivo(listaJSON, 'Aparato.json')
                    print('Archivo guardado')
            else:print('Opcion incorrecta')
