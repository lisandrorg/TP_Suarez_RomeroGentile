class Viajes:


    def __init__(self, organo: str, distancia: int, fecha: str):
        self.organo = organo 
        self.distancia = distancia 
        self.fecha = fecha

    def __str__(self):
        return f"Organo: {self.organo} - Distancia: {self.distancia} Km - Fecha: {self.fecha}\n"