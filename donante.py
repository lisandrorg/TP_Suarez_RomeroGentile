from paciente import PACIENTE

class DONANTE(PACIENTE):
    def __init__(self, nombre: str , DNI: int, nacimiento: int, sexo: str, telefono: int, tipo_de_sangre: str, centro_de_salud: str, organos: str):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.fecha_ablacion = None
        self.hora_ablacion = None
        self.organos = organos 