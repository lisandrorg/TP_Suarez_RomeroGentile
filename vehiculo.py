from viajes import VIAJES

class VEHICULO :
    def __init__(self, tipo: str, velocidad: int, patente: str, centro: str):
        self.tipo = tipo 
        self.patente = patente
        self.velocidad = velocidad
        self.centro = centro
        self.dispo = 1 
        self.registro = []
#ver este tema de llevar registro de todos los viajes de cada vehiculo.