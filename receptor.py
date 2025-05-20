from paciente import PACIENTE

class RECEPTOR(PACIENTE):
    def __init__(self, nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, organo, espera, prioridad, patologia, estado):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.organo = organo
        self.espera = espera
        self.prioridad = prioridad #Baja, Media, Alta
        self.patologia = patologia 
        self.estado = estado #estable, intestable