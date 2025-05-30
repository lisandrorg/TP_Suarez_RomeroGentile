from vehiculo import VEHICULO
from cirujano import CIRUJANO

class CENTRO:

    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.cirujanos = []
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo: VEHICULO):
        for i in self.vehiculos: #verifico que el vehiculo no este previamente registrado
            if(i.patente == vehiculo.patente):
                print("El vehiculo ya se encontraba registrado")
                return
        self.vehiculos.append(vehiculo)
        print("El vehiculo se ha registrado con exito.")

    def registrar_cirujano(self, cirujano: CIRUJANO):
        for i in self.cirujanos:
            if(i.matricula == cirujano.matricula):
                print("El cirujano ya se encontraba registrado")
                return
        self.cirujanos.append(cirujano)
        print("El vehiculo se ha registrado con exito.")


