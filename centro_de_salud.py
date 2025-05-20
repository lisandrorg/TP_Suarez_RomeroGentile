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
        self.cirujano = []
        self.vehiculo = []
        self.receptor = []
        self.donante = []
    
    
    def registrar_paciente(self, paciente:PACIENTE):
        cont = 0
        for i in self.lista_d + self.lista_r: 
            if(i.DNI == paciente.DNI or i.DNI == paciente.DNI):
                print("El paciente con DNI:", paciente.DNI ,"ya se encuentra registrado.")
                cont = 1
        if cont == 0:
            if isinstance(paciente, DONANTE):
                self.lista_d.append(paciente)
            elif isinstance(paciente, RECEPTOR):
                self.lista_r.append(paciente)
            print("Se ha registrado al paciente")
            INCUCAI.match(paciente)

    def registrar_vehiculo(self, vehiculo: VEHICULO):
        cont, pos = 0, -1
        for i in self.lista_c:
            if(vehiculo.centro == i.nombre):
                pos = i
        for f in self.lista_c[pos].vehiculo:
            if f.patente == vehiculo.patente:
                print('El vehiculo ya esta registrado')
                cont=1
                break
        if cont == 0:
            self.lista_c[pos].vehiculo.append(vehiculo)
            print('El vehiculo fue registrado con exito.')
    
    def registrar_cirujano(self, cirujano: CIRUJANO):
        cont, pos = 0, -1
        for i in self.lista_c:
            if(cirujano.centro == i.nombre):
                pos = i
        for f in self.lista_c[pos].cirujano:
            if f.matricula == cirujano.matricula:
                print('El cirujano ya esta registrado')
                cont=1
                break
        if cont == 0:
            self.lista_c[pos].cirujano.append(cirujano)
            print('El cirujano fue registrado con exito.')

   

  
