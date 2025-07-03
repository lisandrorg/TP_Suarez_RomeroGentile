from vehiculo.vehiculo import Vehiculo
from cirujano.cirujano import Cirujano
from vehiculo.avion import Avion
from vehiculo.ambulancia import Ambulancia
from vehiculo.helicoptero import Helicoptero



class Centro:


    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.cirujanos = []
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo: Vehiculo):
        for i in self.vehiculos: #verifico que el vehiculo no este previamente registrado
            if(i.patente == vehiculo.patente):
                print("El vehiculo ya se encontraba registrado")
                return
        self.vehiculos.append(vehiculo)
        print("El vehiculo se ha registrado con exito.")

    def registrar_cirujano(self, cirujano: Cirujano):
        for i in self.cirujanos:
            if(i.matricula == cirujano.matricula):
                print("El cirujano ya se encontraba registrado")
                return
        self.cirujanos.append(cirujano)
        print("El cirujano se ha registrado con exito.")

    def buscar_vehiculo (self, tipo: Avion|Ambulancia|Helicoptero):
        pos=-1
        for i in range(len(self.vehiculos)):
            if(type(self.vehiculos[i]) == tipo and self.vehiculos[i].dispo == 1):
                self.vehiculos[i].dispo = 0
                pos = i
                break
        return pos

    def buscar_cirujano (self, especialidad: str):
        pos = -1
        for i in range(len(self.cirujanos)):
            if self.cirujanos[i].especialidad == especialidad and self.cirujanos[i].dispo == 1:
                self.cirujanos[i].dispo == 0
                pos=i                    
                break
        return pos
