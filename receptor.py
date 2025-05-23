from paciente import PACIENTE

class RECEPTOR(PACIENTE):
    def __init__(self, nombre: str, DNI: int , nacimiento: str , sexo: str,  telefono: str, tipo_de_sangre: str, centro_de_salud: str, organo: str, espera: str, prioridad: int, patologia: str, estado:str):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.organo = organo
        self.espera = espera
        self.prioridad = prioridad #Baja, Media, Alta
        self.patologia = patologia 
        self.estado = estado #estable, intestable