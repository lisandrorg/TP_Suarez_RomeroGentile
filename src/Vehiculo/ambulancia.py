from vehiculo.vehiculo import Vehiculo
from viajes.viajes import Viajes
import random



class Ambulancia(Vehiculo): 


    def __init__(self, velocidad: int, patente: str, centro: str):
        super().__init__(velocidad, patente, centro)

    def calcular_distancia(self, organo: int, ablacion: int):
        trafico = random.randint(0,40)
        distancia = random.randint(60,150)
        tiempo = (distancia + trafico)/self.velocidad
        viaje = Viajes(organo, distancia, ablacion)
        self.registro.append(viaje)
        return tiempo
