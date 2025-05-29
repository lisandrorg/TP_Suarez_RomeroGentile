from receptor import RECEPTOR
from donante import DONANTE
from centro_de_salud import CENTRO
from paciente import PACIENTE
from vehiculo import VEHICULO
from cirujano import CIRUJANO
from datetime import datetime
from viajes import VIAJES
import random
from datetime import datetime, time, timedelta

class INCUCAI:

    def __init__(self):

        self.lista_c = [] #centro
        self.procedimiento = [] #[dni r, dni d, organo, posicion centro donante, posicion centro receptor, posicion v en centro, especialidad si o no, posicion ci en centro, fecha ablacion, hora ablacion]
        self.lista_r = []
        self.lista_d = []

    def buscar_centro(self, nombre: str):
        for i in self.lista_c:
            if i.nombre == nombre:
                return i
        return False

    def registrar_paciente(self, paciente:RECEPTOR|DONANTE): 
        
        cont = 0
        for i in self.lista_d + self.lista_r: 
            if(i.DNI == paciente.DNI or i.DNI == paciente.DNI):
                print("El paciente con DNI:", paciente.DNI ,"ya se encuentra registrado.")
                cont += 1

        for i in self.lista_c:
            if(i.nombre != paciente.centro_de_salud):
                print("el paciente con DNI:", paciente.DNI, "no tiene un centro de salud asociado.")
                cont +=1

        if cont == 0:
            if type(paciente) == DONANTE: 
                self.lista_d.append(paciente)
            if type(paciente) == RECEPTOR: 
                self.lista_r.append(paciente)
            else:
                print('No se ha podido registrar al paciente, intente nuevamente.')
                return

        print("Se ha registrado al paciente exitosamente.")
        INCUCAI.match(paciente)

    def registrar_centro(self, centro: CENTRO):
        cont = 0
        if type(centro) == CENTRO:
            for i in self.lista_c: 
                if(i.nombre == centro.nombre):
                    print("El centro:", centro.nombre ,"ya se encuentra registrado.")
                    cont += 1
            
            if cont == 0:
                self.lista_c.append(centro)
                print("Se ha registrado el centro.")
        else: 
            print("No se ha podido registrar el centro, intente nuevamente.")
        return

    def match_inmediato(self, paciente: DONANTE):
        
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
            self.procedimiento.append(self.lista_r[pos].DNI)
            self.procedimiento.append(paciente.DNI)
            self.transporte(paciente, pos4)
            aux = self.transporte()
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos4)

        elif (pos4 == -1 and pos3 != -1):
            self.procedimiento.append(self.lista_r[pos3].DNI)
            self.procedimiento.append(paciente.DNI)
            self.transporte(paciente, pos3)
            aux = self.transporte()
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos3)

        elif (pos4 == -1 and pos3 == -1 and pos2 != -1):
            self.procedimiento.append(self.lista_r[pos2].DNI)
            self.procedimiento.append(paciente.DNI)
            self.transporte(paciente, pos2)
            aux = self.transporte()
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos2)

        elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 != -1):
            self.procedimiento.append(self.lista_r[pos1].DNI)
            self.procedimiento.append(paciente.DNI)
            self.transporte(paciente, pos1)
            aux = self.transporte()
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos1)

        elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 == -1):
            print('No se ha encontrado una coincidencia')
        
        return

    def match_general(self):
        cont, pos4, pos3, pos2, pos1 = 0, -1, -1, -1, -1
        for d in self.lista_d:
            if cont != 0:
                posd = d
                break
            for k in d.organos:
                if pos1 != -1 or pos2 != -1 or pos3 != -1 or pos4 != -1:
                    cont +=1
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
                self.procedimiento.append(self.lista_r[pos4].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.transporte(d, pos4)
                aux = self.transporte()
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos4)

            elif (pos4 == -1 and pos3 != -1):
                self.procedimiento.append(self.lista_r[pos3].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.transporte(d, pos3)
                aux = self.transporte()
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos3)

            elif (pos4 == -1 and pos3 == -1 and pos2 != -1):
                self.procedimiento.append(self.lista_r[pos2].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.transporte(d, pos2)
                aux = self.transporte()
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos2)
                
            elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 != -1):
                self.procedimiento.append(self.lista_r[pos1].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.transporte(d, pos1)
                aux = self.transporte()
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos1)

            elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 == -1):
                print('No se ha encontrado una coincidencia')
        return                  

    def transporte(self, paciente: DONANTE, posicion: int):

        p_centro_donante = p_centro_receptor = - 1
        condicion1 = (self.lista_c[p_centro_donante].provincia != self.lista_c[p_centro_receptor].provincia)
        condicion2 =(self.lista_c[p_centro_donante].partido != self.lista_c[p_centro_receptor].partido)
        cond_avion = (i.tipo == "Avion" and i.centro == self.lista_c[p_centro_donante].nombre and self.dispo == 1)
        cond_helicoptero = (i.tipo == "Helicoptero" and i.centro == self.lista_c[p_centro_donante].nombre and self.dispo == 1)
        cond_ambulancia = (i.tipo == "Ambulancia" and i.centro == self.lista_c[p_centro_donante].nombre and self.dispo == 1)
        contv=0

        if (condicion1==True):
            for i in self.lista_c[p_centro_donante].vehiculos:
                if(cond_avion == True):
                    self.procedimiento.append(i)
                    self.lista_c[p_centro_donante].vehiculos[i].dispo = 0
                    contv+=1
                    break

        elif (condicion2==True and condicion1==False): 
            for i in self.lista_c[p_centro_donante].vehiculos:
                if(cond_avion == False and cond_helicoptero == True):
                    self.procedimiento.append(i)
                    self.lista_c[p_centro_donante].vehiculos[i].dispo = 0
                    contv+=1
                    break

        elif (condicion2==False and condicion1==False): 
            for i in self.lista_c[p_centro_donante].vehiculos:
                if(cond_avion == False and cond_helicoptero == False and cond_ambulancia == True):
                    self.procedimiento.append(i)
                    self.lista_c[p_centro_donante].vehiculos[i].dispo = 0
                    contv+=1
                    break

        if (contv == 0):
            print('No se encontraron vehiculos disponibles para el transporte.')
            self.procedimiento.clear()
            return True

        ############
    
        for i in self.lista_c[self.procedimiento[3]].cirujanos:

            if( i.dispo == 1 and i.especialidad ==  "Gastroenterolo" and (self.procedimiento[2] == "Intestinos" or self.procedimiento[2] == "Riñon" or self.procedimiento[2] == "Higado" or self.procedimiento[2] == "Pancreas")):
                self.procedimiento.append("Si")
                self.procedimiento.append(i)
                i.dispo = 0
                break
            if( i.dispo == 1 and i.especialidad ==  "Traumatologo" and (self.procedimiento[2] == "Hueso")):
                self.procedimiento.append("Si")
                self.procedimiento.append(i)
                i.dispo = 0
                break
            if(i.dispo == 1 and i.especialidad ==  "Cardiovascular" and (self.procedimiento[2] == "Corazon")):
                self.procedimiento.append("Si")
                self.procedimiento.append(i)
                i.dispo = 0
                break
            if(i.dispo == 1 and i.especialidad ==  "Pulmonar" and (self.procedimiento[2] == "Pulmones")):
                self.procedimiento.append("Si")
                self.procedimiento.append(i)
                i.dispo = 0
                break
            if(i.dispo == 1 and i.especialidad ==  "Plastico" and (self.procedimiento[2] == "Piel" or self.procedimiento[2] == "Corneas")):
                self.procedimiento.append("Si")
                self.procedimiento.append(i)
                i.dispo = 0
                break
            if(i.dispo == 1 and i.especialidad ==  "General"):
                self.procedimiento.append("Si")
                self.procedimiento.append(i)
                i.dispo = 0
                break
            else:
                print("no se ha podido encontrar un doctor disponible")
                self.procedimiento.clear()
                return True
               
        return 

    def viaje(self):

        self.procedimiento.append(datetime.now().date())
        self.procedimiento.append(datetime.now().time())
    
        if self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].tipo == 'Ambulancia':
            trafico = random.randint(0,40)
            distancia = random.randint(60,150)
            tiempo = (distancia + trafico)/self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].velocidad

        elif self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].tipo == 'Helicoptero':
            distancia = random.randint(150, 350)
            tiempo = distancia/self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].velocidad

        elif self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].tipo == 'Avion':
            distancia = random.randint(350, 1000)
            tiempo = distancia / self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].velocidad

        viaje = VIAJES(self.procedimiento[2], distancia, self.procedimiento[7])
        self.lista_c[self.procedimiento[3]].vehiculos[self.procedimiento[5]].registro.append(viaje)

        return tiempo

    def operar(self, tiempo: int , posicion: int):
        
        hora_cirugia = datetime.combine(datetime.today(), self.procedimiento[9]) + timedelta(hours = 20)
        hora_llegada = datetime.combine(datetime.today(), self.procedimiento[9]) + timedelta(hours = tiempo)
        
        if hora_llegada > hora_cirugia:
            print('La ablacion ha superado las 20 horas.')

        else:
            exito = random.randint(1,10)
            if (self.procedimiento[4] == 'Si'):
                if exito > 2:
                    print('La operacion de ', self.procedimiento[2] ,' del paciente ', self.procedimiento[0] ,'se realizo exitosamente.')
                    del(self.lista_r[posicion])
                else:
                    print('La operacion de ', self.procedimiento[2] ,' del paciente ', self.procedimiento[0] ,'no se realizo exitosamente.')
                    self.lista_r[posicion].prioridad = 4
                    self.lista_r[posicion].estado = "inestable"
            else: 
                if exito > 5:
                    print('La operacion de ', self.procedimiento[2] ,' del paciente ', self.procedimiento[0] ,'se realizo exitosamente.')
                    del(self.lista_r[posicion])

                else:
                    print('La operacion de ', self.procedimiento[2] ,' del paciente ', self.procedimiento[0] ,'no se realizo exitosamente.')
                    self.lista_r[posicion].prioridad = 4
                    self.lista_r[posicion].estado = "inestable"

        self.lista_c[self.procedimiento[3]].cirujanos[self.procedimiento[7]].dispo = 1
        for i in self.lista_d:
            if i.DNI == self.procedimiento[1]:
                posd = i
                break
        for i in self.lista_d[posd].organos:
            if i == self.procedimiento[2]:
                pos_org = i

        del(self.lista_d[posd].organos[pos_org])
        if len(self.lista_d[posd].organos) == 0:
            del (self.lista_d[posd])
        self.procedimiento.clear() 
        #posicion del centro en la lista de centros del donante, entonces entro al centro y busco el cirujano
        # 
        #posicion del organo en el array de donantes y borrarlo
        #posicion del organo en el array de organos de ese donante

        return
