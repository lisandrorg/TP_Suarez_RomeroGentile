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

    def buscar_centro(self, nombre: str): #busco posicion de centro, si no esta registrado devuelvo -1, si esta registrado devuelvo su posicion en el array de centros registrados
        for i in range(len(self.lista_c)):
            if self.lista_c[i].nombre == nombre:
                return i 
            else:
                return -1

    def registrar_paciente(self, paciente:RECEPTOR|DONANTE): 
        for i in self.lista_d + self.lista_r: #verifico que el paciente no este registrado ya
            if(i.DNI == paciente.DNI or i.DNI == paciente.DNI):
                print("El paciente con DNI:", paciente.DNI ,"ya se encuentra registrado.")
                return

        cont = 0
        for i in self.lista_c:   #verifico que el centro del paciente este registrado
            if(i.nombre == paciente.centro_de_salud):
                cont +=1
                break

        if cont == 0:
            print("El paciente con DNI:", paciente.DNI, "pertenece a un centro de salud no registrado.")
            return
        
        if type(paciente) == DONANTE: #si es donante guardo en lista de donantes y busco match 
            self.lista_d.append(paciente)
            print("Se ha registrado al paciente exitosamente.")
            self.match_inmediato(paciente)
            return 
        
        if type(paciente) == RECEPTOR: #si es receptor guardo en lista de receptor y vuelvo al menu
            self.lista_r.append(paciente)
            print("Se ha registrado al paciente exitosamente.")
            return
        
        else: #si no es un objeto del tipo receptor o donante, entonces no guardo, muestro un mensaje y vuelvo al menu
            print('No se ha podido registrar al paciente, intente nuevamente.')
            return

    def registrar_centro(self, centro: CENTRO):
        
        if type(centro) == CENTRO:
            for i in self.lista_c: 
                if(i.nombre == centro.nombre):
                    print("El centro:", centro.nombre ,"ya se encuentra registrado.")
                    return
            self.lista_c.append(centro)
            print("Se ha registrado el centro.")

        else: 
            print("No se ha podido registrar el centro, intente nuevamente.")
            return

    def match_inmediato(self, paciente: DONANTE):
        pos4= pos3= pos2= pos1 = -1
        for k in paciente.organos: #recibo un objeto donante e inmediatamente recorro su lista de organos disponibles
            if pos1 != -1 or pos2 != -1 or pos3 != -1 or pos4 != -1: #en caso de detectar cambios significaria que se a encontrado algun posible receptor 
                break
            for i in self.lista_r:
                if (i.prioridad==4 and i.organo == k.organo and i.tipo_de_sangre == k.tipo_de_sangre): #condiciones necesarias, tengo en cuenta que receptor lleva mas tiempo de espera para priorizarlo
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
                    
        if (pos4 != -1): #verifico si encontro un receptor de mayor prioridad, y unicamente hago su match antes de volver al menu
            self.procedimiento.append(self.lista_r[pos4].DNI)
            self.procedimiento.append(paciente.DNI)
            self.procedimiento.append(self.lista_r[pos4].organo)
            aux = self.transporte(pos4)
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos4)

        elif (pos4 == -1 and pos3 != -1):
            self.procedimiento.append(self.lista_r[pos3].DNI)
            self.procedimiento.append(paciente.DNI)
            self.procedimiento.append(self.lista_r[pos3].organo)
            aux = self.transporte(pos3)
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos3)

        elif (pos4 == -1 and pos3 == -1 and pos2 != -1):
            self.procedimiento.append(self.lista_r[pos2].DNI)
            self.procedimiento.append(paciente.DNI)
            self.procedimiento.append(self.lista_r[pos2].organo)
            aux = self.transporte(pos2)
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos2)

        elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 != -1):
            self.procedimiento.append(self.lista_r[pos1].DNI)
            self.procedimiento.append(paciente.DNI)
            self.procedimiento.append(self.lista_r[pos1].organo)
            aux = self.transporte(pos1)
            if(aux): 
                return
            tiempo=self.viaje()
            self.operar(tiempo, pos1)

        elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 == -1):
            print('No se ha encontrado una coincidencia')
            return

    def match_general(self):
        cont = 0
        pos4= pos3= pos2= pos1 = -1
        for d in self.lista_d: #recorro array de donantes
            
            if cont != 0: #si detecto cambios guardo posicion del donante y salgo del bucle(pero esto no tendria sentido, porque obligatoriamente guarda la primera posicionm ya que se inicializa en 0)
                posd = d 
                break
            for k in d.organos: #recorro cada organo del donante
                if pos1 != -1 or pos2 != -1 or pos3 != -1 or pos4 != -1: #si detecto cambios, aumento el contador y vuelvo al for anterior
                    cont +=1
                    break
                for i in self.lista_r: #busco un posible receptor
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
                self.procedimiento.append(self.lista_r[pos4].organo)
                self.transporte(pos4)
                aux = self.transporte()
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos4)

            elif (pos4 == -1 and pos3 != -1):
                self.procedimiento.append(self.lista_r[pos3].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.procedimiento.append(self.lista_r[pos3].organo)
                aux = self.transporte(pos3)
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos3)

            elif (pos4 == -1 and pos3 == -1 and pos2 != -1):
                self.procedimiento.append(self.lista_r[pos2].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.procedimiento.append(self.lista_r[pos2].organo)
                aux = self.transporte(pos2)
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos2)
                
            elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 != -1):
                self.procedimiento.append(self.lista_r[pos1].DNI)
                self.procedimiento.append(self.lista_d[posd].DNI)
                self.procedimiento.append(self.lista_r[pos1].organo)
                aux = self.transporte(pos1)
                if(aux == True): 
                    return
                tiempo=self.viaje()
                self.operar(tiempo, pos1)

            elif (pos4 == -1 and pos3 == -1 and pos2 == -1 and pos1 == -1):
                print('No se ha encontrado una coincidencia')
                return                  

    def transporte(self, posicion: int):
        
        for i in self.lista_d:
            if i.DNI == self.procedimiento[2]:
                d=i
                break
        
        p_centro_donante = self.buscar_centro(self.lista_d[d].centro_de_salud) 
        p_centro_receptor = self.buscar_centro(self.lista_r[posicion].centro_de_salud)
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
                break

        del(self.lista_d[posd].organos[pos_org])
        if len(self.lista_d[posd].organos) == 0:
            del (self.lista_d[posd])
        self.procedimiento.clear() 
        return
