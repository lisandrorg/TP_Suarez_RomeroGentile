from vehiculo.vehiculo import Vehiculo
from viajes.viajes import Viajes
import random



class Helicoptero(Vehiculo): 


    def __init__(self, velocidad: int, patente: str, centro: str):
        super().__init__(velocidad, patente, centro)

    def calcular_distancia(self, organo: int, ablacion: int):
        distancia = random.randint(150, 350)
        tiempo = distancia/self.velocidad
        viaje = Viajes(organo, distancia, ablacion)
        self.registro.append(viaje)
        return tiempo
