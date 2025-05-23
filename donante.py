from paciente import PACIENTE

class DONANTE(PACIENTE):
    def __init__(self, nombre: str , DNI: int, nacimiento: str, sexo: str, telefono: str, tipo_de_sangre: str, centro_de_salud: str, fecha_muerte: str, hora_muerte: str, fecha_ablacion: str, hora_ablacion: str, organos: str):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.fecha_muerte = fecha_muerte
        self.hora_muerte = hora_muerte
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.organos = organos 