from vehiculo.vehiculo import Vehiculo
from viajes.viajes import Viajes
import random



class Ambulancia(Vehiculo): 

    '''
    Esta clase es hija de Vehiculo.
    '''

    def __init__(self, velocidad: int, patente: str, centro: str):
        super().__init__(velocidad, patente, centro)

    def calcular_distancia(self, organo: str, ablacion: int):
        
        '''
            Se encarga de calcular el tiempo necesario de
            viaje, ademas de registrar el viaje.
        PARAMETROS:
            organo: variable str que contiene el organo operado
            ablacion: variable int que contiene la fecha de 
            ablacion del organo
        RETURNS:
            Retorna el tiempo de viaje
        '''

        trafico = random.randint(0,40)
        distancia = random.randint(60,150)
        tiempo = (distancia + trafico)/self.velocidad
        viaje = Viajes(organo, distancia, ablacion)
        self.registro.append(viaje)
        return tiempo
