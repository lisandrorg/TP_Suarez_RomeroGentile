from receptor import RECEPTOR
from donante import DONANTE
from centro_de_salud import CENTRO
from paciente import PACIENTE
from vehiculo import VEHICULO
from cirujano import CIRUJANO
from datetime import datetime
from viajes import VIAJES
import random

class INCUCAI:
    def __init__(self):

        self.lista_c = [] #centro
        self.procedimiento = [] #[nombre r, nombre d, posicion centro donante, posicion centro receptor, organo, posicion v en centro, especialidad si o no, posicion ci en centro, fecha ablacion, hora ablacion]
    
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
            pos4, pos3, pos2, pos1 = -1, -1, -1, -1
            for k in paciente.organos:
                if pos1 != -1 or pos2 != -1 or pos3 != -1 or pos4 != -1:
                    break
                for i in self.lista_r:
                    if (i.prioridad==4 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if i==0:
                            fmin4=espera
                            pos4=i
                        elif (espera < fmin4):
                            fmin4=espera
                            pos4=i
                    if (i.prioridad==3 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if i==0:
                            fmin3=espera
                            pos3=i
                        elif (espera < fmin3):
                            fmin3=espera
                            pos3=i
                    elif (i.prioridad==2 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if i==0:
                            fmin3=espera
                            pos3=i
                        elif(espera < fmin2):
                            fmin2=espera 
                            pos2=i
                    elif (i.prioridad==1 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre):
                        espera = i.espera 
                        if i==0:
                            fmin3=espera
                            pos3=i
                        elif(espera < fmin1):
                            fmin1=espera 
                            pos1=i
            if (pos4 != -1):
                self.transporte(paciente, pos4)
                tiempo=self.viaje()
                self.operar(tiempo, pos4)
            elif (pos4 == -1 and pos3 != -1):
                self.transporte(paciente, pos3)
                tiempo=self.viaje()
                self.operar(tiempo, pos3)
            elif (pos4 == -1 and pos3 == -1 and pos2 != -1):
                self.transporte(paciente, pos2)
                tiempo=self.viaje()
                self.operar(tiempo, pos2)
            elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 != -1):
                self.transporte(paciente, pos1)
                tiempo=self.viaje()
                self.operar(tiempo, pos1)
            elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 == -1):
                print('No se ha encontrado una coincidencia')

    def transporte(self, paciente: PACIENTE, posicion):
        if type(paciente) == DONANTE:
            self.procedimiento.append(self.lista_r[posicion].nombre)
            self.procedimiento.append(paciente.nombre)
            self.procedimiento.append(self.lista_r[posicion].organo)
            cont = 0
            p_centro_receptor = p_centro_donante = -1
            for i in self.lista_c:
                if(paciente.centro_de_salud == i.nombre):
                    p_centro_donante = i 
                    cont +=1
                if(self.lista_r[posicion].centro_de_salud == i.nombre):
                    p_centro_receptor = i
            if cont == 0:
                print("El centro de salud del donante no se encuentra registrado.")
            
            condicion1 = (self.lista_c[p_centro_donante].provincia != self.lista_c[p_centro_receptor].provincia)
            condicion2 =(self.lista_c[p_centro_donante].partido != self.lista_c[p_centro_receptor].partido)
            contv=0
            if (condicion1==True):
                for i in self.lista_v:
                    if(i.tipo == "Avion" and i.centro == self.lista_c[p_centro_donante].nombre and self.dispo == 1):
                        self.procedimiento.append(i.patente)
                        self.lista_v[i].dispo = 0
                        contv+=1
                        break
            elif (condicion2==True and condicion1==False): #cambiar
                for i in self.lista_v:
                    if(i.tipo == "Helicoptero" and i.centro == self.lista_c[p_centro_donante].nombre and self.dispo == 1):
                        self.procedimiento.append(i.patente)
                        self.lista_v[i].dispo = 0
                        contv+=1
                        break
            elif (condicion2==False and condicion1==False): #cambiar
                for i in self.lista_v:
                    if(i.tipo == "Ambulancia" and i.centro == self.lista_c[p_centro_donante].nombre and self.dispo == 1):
                        self.procedimiento.append(i)
                        self.lista_v[i].dispo = 0
                        contv+=1
                        break
            if (contv == 0):
                print('No se encontraron vehiculos disponibles para el transporte.')
                self.procedimiento.clear()
            
            #NO HAY COINCIDENCIA, ROMPER#


            ORGANO_A_ESPECIALIDAD = {
    "Corazon": "Cardiovascular",
    "Higado": "Gastorenterologo",
    "Riñon": "Gastorenterologo",
    "Pulmon": "Pulmonar",
    "Pancreas": "Gastorenterologo",
    "Intestino": "Gastorenterologo",
    "Huesos": "Traumatologo",
    "Corneas": "Plastico",
    "Piel": "Plastico"
}
            
            pos_c=next((c for c in self.lista_ci if (c.especialidad == ORGANO_A_ESPECIALIDAD.get(self.procedimiento[2]) and c.centro == paciente.centro_de_salud and c.dispo == 1)), None)
            self.procedimiento.append('Si')
            if pos_c == None:
                next((c for c in self.lista_ci if (c.centro == paciente.centro_de_salud and self.dispo == 1)), None)
                self.procedimiento.append('No')
            if pos_c == None:
                print('No se ha encontrado un cirujano disponible para operarlo')
                self.procedimiento.clear()
            else:
                self.procedimiento.append(pos_c) #cambiar
                self.lista_ci[pos_c].dispo=0

    def viaje(self):
        self.procedimiento.append(datetime.now().date())
        self.procedimiento.append(datetime.now().time())
        if self.lista_v[self.procedimiento[3]].tipo == 'Ambulancia':
            trafico = random.randint(0,40)
            distancia = random.randint(60,150)
            tiempo = (distancia + trafico)/self.lista_v[self.procedimiento[3]].velocidad
        elif self.lista_v[self.procedimiento[3]].tipo == 'Helicoptero':
            distancia=random.randint(150, 350)
            tiempo = distancia/self.lista_v[self.procedimiento[3]].velocidad
        elif self.lista_v[self.procedimiento[3]].tipo == 'Avion':
            distancia = random.randint(350, 1000)
            tiempo = distancia/self.lista_v[self.procedimiento[3]].velocidad
        #hacer pasar el tiempo#

        viaje = VIAJES(self.procedimiento[2], distancia,self.procedimiento[6])
        self.lista_v[self.procedimiento[3]].registro.append(viaje)

        return tiempo

    def operar(self, tiempo, posicion):
        if tiempo > 20:
            print('La ablacion ha superado las 20 horas')
        else:
            exito = random.randint(1,10)
            if (self.procedimiento[4] == 'Si'):
                if exito > 2:
                    print('La operacion de ', self.procedimiento[2] ,' del paciente ', self.procedimiento[0] ,'se realizo exitosamente.')
                    del(self.lista_r[posicion])
                else:
                    self.lista_r[posicion].prioridad = 4
            else:
                if exito > 5:
                    print('La operacion de ', self.procedimiento[2] ,' del paciente ', self.procedimiento[0] ,'se realizo exitosamente.')
                    del(self.lista_r[posicion])
                else:
                    self.lista_r[posicion].prioridad = 4
            self.lista_ci[self.procedimiento[5]].dispo = 1
            pos=next((c for c in self.lista_d if c.nombre == self.procedimiento[1]), None)
            poso=next((o for o in self.lista_d[pos].organos if o == self.procedimiento[2]), None)
            del(self.lista_d[pos].organos[poso])
            if len(self.lista_d[pos].organos) == 0:
                del (self.lista_d[pos])
            self.procedimiento.clear()

