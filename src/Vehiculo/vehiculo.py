from abc import abstractmethod



class Vehiculo:


    def __init__(self, velocidad: int, patente: str, centro: str):
        self.patente = patente
        self.velocidad = velocidad
        self.centro = centro
        self.dispo = 1 
        self.registro = []

    @abstractmethod
    def calcular_distancia():
        return    

    def print_registro(self):
        if len(self.registro) != 0:
            for v in range(len(self.registro)):
                print('Viaje N.', v+1 ,': ' , self.registro[v].__str__())
        else:
            print("Este vehiculo no ha registrado viajes aun.")
        return -1