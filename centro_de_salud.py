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
        cont = 0
        for i in self.vehiculos:
            if(i.patente == vehiculo.patente):
                print("El vehiculo ya se encuentra registrado")
                cont += 1
                break
        if (cont == 0):
            self.vehiculos.append(vehiculo)
            print("El vehiculo se ha registrado con exito.")

    def registrar_cirujano(self, cirujano: CIRUJANO):
        cont = 0
        for i in self.cirujanos:
            if(i.matricula == cirujano.matricula):
                print("El cirujano ya se encuentra registrado")
                cont += 1
                break
        if (cont == 0):
            self.cirujanos.append(cirujano)
            print("El vehiculo se ha registrado con exito.")


