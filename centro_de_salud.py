from paciente import PACIENTE
from receptor import RECEPTOR
from donante import DONANTE
from INCUCAI import INCUCAI
from vehiculo import VEHICULO
from cirujano import CIRUJANO


class CENTRO:

    def __init__(self, nombre, direccion, partido, provincia):
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
                print("el vehiculo ya se encuentra registrado")
                cont += 1
                break
        if (cont == 0):
            self.vehiculo.append(vehiculo)
            print("el vehiculo se ha registrado con exito.")

    def registrar_cirujano(self, cirujano: CIRUJANO):
        cont = 0
        for i in self.cirujanos:
            if(i.matricula == cirujano.matricula):
                print("el cirujano ya se encuentra registrado")
                cont += 1
                break
        if (cont == 0):
            self.cirujanos.append(cirujano)
            print("el vehiculo se ha registrado con exito.")



  
