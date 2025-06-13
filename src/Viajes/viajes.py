class VIAJES:
    def __init__(self, organo: str, distancia: int, fecha: str):
        self.organo = organo 
        self.distancia = distancia 
        self.fecha = fecha

    def __str__(self):
        return f" {self.organo} - {self.distancia} Km - {self.fecha} "