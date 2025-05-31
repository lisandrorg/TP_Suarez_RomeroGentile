from paciente import PACIENTE

class RECEPTOR(PACIENTE):
    def __init__(self, nombre: str, DNI: int , nacimiento: int , sexo: str,  telefono: int, tipo_de_sangre: str, centro_de_salud: str, organo: str, espera: int, prioridad: int):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.organo = organo
        self.espera = espera
        self.prioridad = prioridad #Baja, Media, Alta

    def __str__(self):
        return f"{self.nombre} - {self.DNI} - {self.nacimiento} - {self.sexo} - {self.telefono} - {self.tipo_de_sangre} - {self.centro_de_salud} - {self.organo} - {self.espera} - {self.prioridad}"