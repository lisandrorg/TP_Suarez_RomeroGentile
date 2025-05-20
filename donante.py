from paciente import PACIENTE

class DONANTE(PACIENTE):
    def __init__(self, nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, organos):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.fecha_muerte = fecha_muerte
        self.hora_muerte = hora_muerte
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.organos = organos 