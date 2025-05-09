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
                print("El vehiculo de patente:", vehiculo.patente ,"ya se encuentra registrado.")
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
            fmin1, fmin2, fmin3, pos3, pos2, pos1 = 100000000000 , 100000000000, 100000000000, -1, -1, -1
            for k in paciente.organos:
                for i in self.lista_r:
                    if (i.prioridad==3 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if(espera < fmin3):
                            fmin3=espera
                            pos3=i
                    elif (i.prioridad==2 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if(espera < fmin2):
                            fmin2=espera 
                            pos2=i
                    elif (i.prioridad==1 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if(espera < fmin1):
                            fmin1=espera 
                            pos1=i
            if (pos3 != -1):
                self.transporte(pos3)
                self.borrar(k, pos3)
            elif (pos3 == -1 and pos2 != -1):
                self.transporte(pos2)
                self.borrar(k, pos2)
            elif (pos3 == -1 and pos2 == -1 and pos1 != -1):
                self.transporte(pos1)
                self.borrar(k, pos1)

            #falta retirar de la lista, los datos de paciente y receptor en caso de match

        if type(paciente) == RECEPTOR:
            for i in self.lista_d:
                pass

    def transporte(self, paciente: PACIENTE, posicion):
        if type(paciente) == DONANTE:
            cont = 0
            for i in self.lista_c:
                if(paciente.centro_de_salud == i.nombre):
                    p_centro_donante = i 
                    cont +=1
                if(self.lista_r[posicion].centro_de_salud == i.nombre):
                    p_centro_receptor = i
            if cont == 0:
                print("el centro de salud del donante no se encuentra registrado.")
            condicion1 = (self.lista_c[p_centro_donante].provincia != self.lista_c[p_centro_receptor].provincia)
            condicion2 =(self.lista_c[p_centro_donante].partido != self.lista_c[p_centro_receptor].partido)

            if (condicion1==True):
                for i in self.lista_v:
                    if(i.tipo == "Avion" and i.centro == self.lista_c[p_centro_donante].nombre):
                        pos_vehiculo = i
            elif (condicion2==True and condicion1==False):
                for i in self.lista_v:
                    if(i.tipo == "Helicoptero" and i.centro == self.lista_c[p_centro_donante].nombre):
                        pos_vehiculo = i
            elif (condicion2==False and condicion1==False):
                for i in self.lista_v:
                    if(i.tipo == "Ambulancia" and i.centro == self.lista_c[p_centro_donante].nombre):
                        pos_vehiculo = i

            
        if type(paciente) == DONANTE:
            pass
            


        

#Este le pide al
#centro de salud del donante que asigne un vehículo y un cirujano. Una vez que se asignó el vehículo, el centro
#procede a realizar la ablación del órgano que necesita el receptor. En la ablación se setea la fecha y horario de
#ablación del órgano y se quita el órgano removido de la lista de órganos del paciente donante. Ese vehículo
#realiza el transporte (el cual demora un tiempo dependiendo de la distancia). Finalmente, el centro de salud
#del receptor realiza el trasplante. Para realizar el trasplante se verifica que no hayan transcurrido más de 20
#horas desde la ablación del órgano y procede a realizar el trasplante con el cirujano elegido. Si el trasplante es
#exitoso, se remueve al paciente receptor de la lista de pacientes receptores. Si el trasplante falla, se cambia la
#prioridad del paciente receptor a la de mayor prioridad y se setea su estado a inestable. Si el trasplante es
#exitoso o no se define con un valor aleatorio que varia dependiendo de la especialidad del cirujano.


    def borrar(self, posd, posr):
        del self.lista_r[posr]
        del self.lista_d[-1].organos[posd]
        if len(self.lista_d[-1].organos) == 0:
            del self.lista_d[-1]


        


