from abc import abstractmethod



class Vehiculo:

    '''
    Esta clase posee todos los datos necesarios
    para registrar un vehiculo. Ademas es capaz 
    de mostrar los viajes registrados.
    '''

    def __init__(self, velocidad: int, patente: str, centro: str):
        self.patente = patente
        self.velocidad = velocidad
        self.centro = centro
        self.dispo = 1 
        self.registro = []


    @abstractmethod
    def calcular_distancia(self, organo: str, ablacion: int) -> None:
        
        '''
            Se encarga de calcular el tiempo necesario de
            viaje, ademas de registrar el viaje. Es abstracto 
            ya que varia su funcionamiento segun que tipo de
            vehiculo se encarga del viaje.
        PARAMETROS:
            organo: variable str que contiene el organo operado
            ablacion: variable int que contiene la fecha de 
            ablacion del organo
        RETURNS:
            Retorna el tiempo de viaje
        '''
        return    

    def print_registro(self) -> int:
        
        '''
            Se imprime en pantalla la lista de viajes
            registrados.
        PARAMETROS:
            -No recibe parametros
        RETURNS:
            -Retorna un entero -1.
        '''

        if len(self.registro) != 0:
            for v in range(len(self.registro)):
                print('Viaje N.', v+1 ,': ' , self.registro[v].__str__())
        else:
            print("Este vehiculo no ha registrado viajes aun.")
        return -1