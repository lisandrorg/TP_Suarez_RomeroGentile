from receptor import RECEPTOR
from donante import DONANTE
from centro_de_salud import CENTRO
from paciente import PACIENTE
from vehiculo import VEHICULO
from cirujano import CIRUJANO

class INCUCAI:
    def __init__(self):
        self.lista_d = [] #donante
        self.lista_r = [] #receptor
        self.lista_c = [] #centro
        self.lista_v = [] #vehiculo
        self.lista_ci = [] #cirujano
    
    def registrar_paciente(self, paciente:PACIENTE ):
        cont = 0
        for i in self.lista_d + self.lista_r: 
            if(i.DNI == paciente.DNI or i.DNI == paciente.DNI): #preguntar si seria necesario que el organo que done, este dentro de las opciones de la consigna
                print("El paciente con DNI:", paciente.DNI ,"ya se encuentra registrado.")
                cont = 1
        if cont == 0:
            if isinstance(paciente, DONANTE):
                self.lista_d.append(paciente)
            elif isinstance(paciente, RECEPTOR):
                self.lista_r.append(paciente)
            print("Se ha registrado al paciente")
            paciente.match(paciente)

    def registrar_vehiculo(self, vehiculo: VEHICULO):
        cont = 0
        for i in self.lista_d + self.lista_r: 
            if(i.patente == vehiculo.patente or i.patente == vehiculo.patente): #preguntar si seria necesario que el organo que done, este dentro de las opciones de la consigna
                print("El paciente con DNI:", vehiculo.patente ,"ya se encuentra registrado.")
                cont = 1
        if cont == 0:
            self.lista_v.append(vehiculo)
            print("Se ha registrado el vehiculo")

    def registrar_cirujano(self, cirujano: CIRUJANO):
        cont = 0
        for i in self.lista_d + self.lista_r: 
            if(i.matricula == cirujano.matricula or i.matricula == cirujano.matricula): #preguntar si seria necesario que el organo que done, este dentro de las opciones de la consigna
                print("El cirujano de matricula:", cirujano.matricula ,"ya se encuentra registrado.")
                cont = 1
        if cont == 0:
            self.lista_ci.append(cirujano)
            print("Se ha registrado el cirujano")

    def registrar_centro(self, centro: CENTRO):
        cont = 0
        for i in self.lista_d + self.lista_r: 
            if(i.nombre == centro.nombre or i.nombre == centro.nombre): #preguntar si seria necesario que el organo que done, este dentro de las opciones de la consigna
                print("El centro:", centro.nombre ,"ya se encuentra registrado.")
                cont = 1
        if cont == 0:
            self.lista_c.append(centro)
            print("Se ha registrado el centro")

    def match(self, paciente:PACIENTE):
        if type(paciente) == DONANTE:
            fmin1, fmin2, fmin3 = 0 , 0, 0
            for k in paciente.organos:
                for i in self.lista_r:
                    if (i.prioridad==3 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if(espera > fmin3):
                            fmin3=espera
                            pos3=i
                    elif (i.prioridad==2 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if(espera > fmin2):
                            fmin2=espera 
                            pos2=i
                    elif (i.prioridad==1 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if(espera > fmin1):
                            fmin1=espera 
                            pos1=i
            if (pos3 != 0):
                pass #organizar viaje prioridad 3
            elif (pos3 == 0 and pos2 != 0):
                pass #organizar viaje prioridad 2
            elif (pos3 == 0 and pos2 == 0 and pos1 != 0):
                pass #organizar viaje prioridad 1

            #falta retirar de la lista, los datos de paciente y receptor en caso de match

        if type(paciente) == RECEPTOR:
            for i in self.lista_d:
                pass

            
