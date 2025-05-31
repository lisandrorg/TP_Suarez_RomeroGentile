class PACIENTE:
    def __init__(self, nombre: str, DNI: int, nacimiento: int, sexo: str, telefono: int, tipo_de_sangre: str, centro_de_salud: str):
        self.nombre = nombre 
        self.DNI = DNI
        self.nacimiento = nacimiento 
        self.sexo = sexo
        self.telefono = telefono
        self.tipo_de_sangre = tipo_de_sangre
        self.centro_de_salud = centro_de_salud
