from Paciente.receptor import RECEPTOR
from Paciente.donante import DONANTE
from Centro.centro import CENTRO
from Paciente.paciente import PACIENTE
from Vehiculo.vehiculo import VEHICULO
from Cirujano.cirujano import CIRUJANO
from datetime import datetime
from Viajes.viajes import VIAJES
import random
from datetime import datetime, timedelta
import time



class INCUCAI:


    '''
    Esta clase se encarga de llevar a cabo los procedimientos 
    necesarios para que se realize una coincidecia de pacientes,
    transporte de organo y posterior operacion.
    '''

    def __init__(self):
        self.lista_c = [] 
        self.__procedimiento = [] #[dni r, dni d, organo, posicion centro donante, posicion centro receptor, posicion v en centro, especialidad si o no, posicion ci en centro, fecha ablacion, hora ablacion]
        self.__lista_r = []
        self.__lista_d = []

    def buscar_centro(self, nombre: str) -> int:
        
        '''
            Permite saber la posicion de un centro de salud en la lista de centros

        PARAMETROS:
            -nombre: una variable de tipo string en el cual se 
            recibe el nombre de un centro de salud
        RETURNS:
            -Retorna un entero, igual a -1 en caso del centro no estar en la lista
            de los centros de salud registrados, caso contrario, devuelve la
            posicion de dicho centro en la lista
        '''
        
        for i in range(len(self.lista_c)):
            if self.lista_c[i].nombre == nombre:
                return i 
        return -1

    def registrar_paciente(self, paciente: RECEPTOR|DONANTE) -> None: 
        
        '''
            Se puede registrar un paciente, y es filtrado dependiendo de 
        si es receptor o donante, pero verifica que no esté previamente registrado 
        y que este asociado a un centro de salud registrado en el sistema.
        En caso de encontrar un paciente ya registrado se muestra
        un mensaje en pantalla dando a conocer esto, en caso de 
        registrarse correctamente al paciente tambien se muestra un
        mensaje en pantalla y si el paciente era donante se busca un
        match inmediatamente.

        PARAMETROS:
            -paciente: una variable de tipo RECEPTOR o DONANTE 
        RETURNS:
            -No retorna nada.
        '''
        for i in self.__lista_d + self.__lista_r: #verifico que el paciente no este registrado ya
            if(i.DNI.__eq__(paciente.DNI) or i.DNI.__eq__(paciente.DNI)):
                print("El paciente con DNI:", paciente.DNI ,"ya se encuentra registrado.")
                return

        cont = 0
        for i in self.lista_c:   #verifico que el centro del paciente este registrado
            if(i.nombre.__eq__(paciente.centro_de_salud)):
                cont = cont+1
                break

        if cont.__eq__(0):
            print("El paciente con DNI:", paciente.DNI, "pertenece a un centro de salud no registrado.")
            return
        
        if type(paciente) == DONANTE: #si es donante guardo en lista de donantes y busco match 
            self.__lista_d.append(paciente)
            print("Se ha registrado al paciente exitosamente.")
            self.__match_inmediato(paciente)
        elif type(paciente) == RECEPTOR: #si es receptor guardo en lista de receptor y vuelvo al menu
            self.__lista_r.append(paciente)
            print("Se ha registrado al paciente exitosamente.")
        else: #si no es un objeto del tipo receptor o donante, entonces no guardo, muestro un mensaje y vuelvo al menu
            print('No se ha podido registrar al paciente, intente nuevamente.')
            return

    def registrar_centro(self, centro: CENTRO) -> None:
        
        '''
            Se puede registrar un centro, verifica que no esté previamente 
            registrado y en caso que no lo este se lo añade a la lista. 
            Imprime en pantalla un mensaje indicando que ocurrio.

        PARAMETROS:
            -centro: un argumento de tipo CENTRO
        RETURNS:
            -No retorna nada.
        '''


        if type(centro) == CENTRO:
            for i in self.lista_c: 
                if(i.nombre.__eq__(centro.nombre)):
                    print("El centro:", centro.nombre ,"ya se encuentra registrado.")
                    return
            self.lista_c.append(centro)
            print("Se ha registrado el centro.")

        else: 
            print("No se ha podido registrar el centro, intente nuevamente.")
            return

    def __match_inmediato(self, paciente: DONANTE) -> None:
        
        '''
            Se recibe un paciente donante, sobre el cual se va a buscar 
            un receptor en base a que organos se encuentran disponibles.
            Posteriorimente se llaman a las funciones encargadas de las
            demas tareas.

        PARAMETROS:
            -paciente: una variable de tipo DONANTE
        RETURNS:
            -No retorna nada.
        '''
        
        pos4 = pos3 = pos2 = pos1 = -1
        for k in paciente.organos:
            if pos1.__ne__(-1) or pos2.__ne__(-1) or pos3.__ne__(-1) or pos4.__ne__(-1):
                break
            pos4 = self.__buscar_prioridad(4, k, paciente.tipo_de_sangre)
            pos3 = self.__buscar_prioridad(3, k, paciente.tipo_de_sangre)
            pos2 = self.__buscar_prioridad(2, k, paciente.tipo_de_sangre)
            pos1 = self.__buscar_prioridad(1, k, paciente.tipo_de_sangre)
        
        if (pos4.__ne__(-1)): 
            self.__procedimiento.append(self.__lista_r[pos4].DNI)
            self.__procedimiento.append(paciente.DNI)
            self.__procedimiento.append(self.__lista_r[pos4].organo)
            aux = self.__transporte(pos4)
            if(aux==True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos4)
            return

        elif (pos4.__eq__(-1) and pos3.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos3].DNI)
            self.__procedimiento.append(paciente.DNI)
            self.__procedimiento.append(self.__lista_r[pos3].organo)
            aux = self.__transporte(pos3)
            if(aux==True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos3)
            return

        elif (pos4.__eq__(-1) and pos3.__eq__(-1) and pos2.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos2].DNI)
            self.__procedimiento.append(paciente.DNI)
            self.__procedimiento.append(self.__lista_r[pos2].organo)
            aux = self.__transporte(pos2)
            if(aux==True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos2)
            return

        elif (pos4.__eq__(-1) and pos3.__eq__(-1) and pos2.__eq__(-1) and pos1.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos1].DNI)
            self.__procedimiento.append(paciente.DNI)
            self.__procedimiento.append(self.__lista_r[pos1].organo)
            aux = self.__transporte(pos1)
            if(aux==True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos1)
            return

        elif (pos4.__eq__(-1) and pos3.__eq__(-1) and pos2.__eq__(-1) and pos1.__eq__(-1)):
            print('No se ha encontrado una coincidencia')
            return

    def match_general(self) -> None:
        
        '''
            No se recibe nada, se recorre la lista de donante, sobre la 
            cual se va a buscar un receptor en base a que organos se encuentran 
            disponibles de cada donante. Posteriorimente se llaman a las funciones 
            encargadas de las demas tareas.

        PARAMETROS:
            -paciente: una variable de tipo DONANTE
        RETURNS:
            -No retorna nada.
        '''
        random.shuffle(self.__lista_d)
        cont = -1
        posd = pos4= pos3= pos2= pos1 = -1
        for d in range(len(self.__lista_d)): 
            
            if cont != -1: 
                posd = d 
                break
            for k in self.__lista_d[d].organos: 
                if pos1 != -1 or pos2 != -1 or pos3 != -1 or pos4 != -1: 
                    cont.__add__(1)
                    break
                pos4 = self.__buscar_prioridad(4, k, self.__lista_d[d].tipo_de_sangre)
                pos3 = self.__buscar_prioridad(3, k, self.__lista_d[d].tipo_de_sangre)
                pos2 = self.__buscar_prioridad(2, k, self.__lista_d[d].tipo_de_sangre)
                pos1 = self.__buscar_prioridad(1, k, self.__lista_d[d].tipo_de_sangre)

        if (pos4.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos4].DNI)
            self.__procedimiento.append(self.__lista_d[posd].DNI)
            self.__procedimiento.append(self.__lista_r[pos4].organo)
            aux = self.__transporte(pos4)
            if(aux == True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos4)

        elif (pos4.__eq__(-1) and pos3.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos3].DNI)
            self.__procedimiento.append(self.__lista_d[posd].DNI)
            self.__procedimiento.append(self.__lista_r[pos3].organo)
            aux = self.__transporte(pos3)
            if(aux == True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos3)

        elif (pos4.__eq__(-1) and pos3.__eq__(-1) and pos2.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos2].DNI)
            self.__procedimiento.append(self.__lista_d[posd].DNI)
            self.__procedimiento.append(self.__lista_r[pos2].organo)
            aux = self.__transporte(pos2)
            if(aux == True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos2)
            
        elif (pos4.__eq__(-1) and pos3.__eq__(-1) and pos2.__eq__(-1) and pos1.__ne__(-1)):
            self.__procedimiento.append(self.__lista_r[pos1].DNI)
            self.__procedimiento.append(self.__lista_d[posd].DNI)
            self.__procedimiento.append(self.__lista_r[pos1].organo)
            aux = self.__transporte(pos1)
            if(aux == True): 
                return
            tiempo=self.__viaje()
            self.__operar(tiempo, pos1)

        elif (pos4.__eq__(-1) and pos3.__eq__(-1) and pos2.__eq__(-1) and pos1.__eq__(-1)):
            print('No se ha encontrado una coincidencia')
            return                  

    def __transporte(self, posicion: int) -> None|bool:
        
        '''
            Se busca un vehiculo perteniciente al centro del 
            donante el cual este disponible para el transporte.
            A su vez, se busca un cirujano perteneciente al 
            centro del donante el cual este disponible para
            llevar a cabo la operacion.

        PARAMETROS:
            -posicion: una variable de tipo int que contiene
            la posicion del receptor en la lista de receptores
        RETURNS:
            -En caso de no encontrar un cirujano o un vehiculo 
            disponible retorna un booleano True, en caso que
            los encuentre no retorna nada.
        '''
        
        d=0
        for x in range(len(self.__lista_d)):
            if self.__lista_d[x].DNI == self.__procedimiento[1]:
                d=x
                break
        p_centro_donante = self.buscar_centro(self.__lista_d[d].centro_de_salud) 
        self.__procedimiento.append(p_centro_donante)
        p_centro_receptor = self.buscar_centro(self.__lista_r[posicion].centro_de_salud)
        self.__procedimiento.append(p_centro_receptor)
        condicion1 = (self.lista_c[p_centro_donante].provincia != self.lista_c[p_centro_receptor].provincia)
        condicion2 =(self.lista_c[p_centro_donante].partido != self.lista_c[p_centro_receptor].partido)
        contv=0

        if (condicion1==True):
            for i in range(len(self.lista_c[p_centro_donante].vehiculos)):
                if(self.lista_c[p_centro_donante].vehiculos[i].tipo == "Avion" and self.lista_c[p_centro_donante].vehiculos[i].centro == self.lista_c[p_centro_donante].nombre and self.lista_c[p_centro_donante].vehiculos[i].dispo == 1):
                    self.__procedimiento.append(i)
                    self.lista_c[p_centro_donante].vehiculos[i].dispo = 0
                    contv += 1
                    break

        elif (condicion2==True and condicion1==False): 
            for i in range(len(self.lista_c[p_centro_donante].vehiculos)):
                if(self.lista_c[p_centro_donante].vehiculos[i].tipo == "Helicoptero" and self.lista_c[p_centro_donante].vehiculos[i].centro == self.lista_c[p_centro_donante].nombre and self.lista_c[p_centro_donante].vehiculos[i].dispo == 1):
                    self.__procedimiento.append(i)
                    self.lista_c[p_centro_donante].vehiculos[i].dispo = 0
                    contv += 1
                    break

        elif (condicion2 == False and condicion1 == False): 
            for i in range(len(self.lista_c[p_centro_donante].vehiculos)):
                if(self.lista_c[p_centro_donante].vehiculos[i].tipo == "Ambulancia" and self.lista_c[p_centro_donante].vehiculos[i].centro == self.lista_c[p_centro_donante].nombre and self.lista_c[p_centro_donante].vehiculos[i].dispo == 1):
                    self.__procedimiento.append(i)
                    self.lista_c[p_centro_donante].vehiculos[i].dispo = 0
                    contv += 1
                    break

        if (contv.__eq__(0)):
            print('No se encontraron vehiculos disponibles para el transporte.')
            self.__procedimiento.clear()
            return True

        for i in range(len(self.lista_c[self.__procedimiento[3]].cirujanos)):

            if( self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo.__eq__(1) and (self.lista_c[self.__procedimiento[3]].cirujanos[i].especialidad ==  "Gastroenterolo" or (self.__procedimiento[2] == "Intestinos" or self.__procedimiento[2] == "Riñon" or self.__procedimiento[2] == "Higado" or self.__procedimiento[2] == "Pancreas"))):
                self.__procedimiento.append("Si")
                self.__procedimiento.append(i)
                self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo = 0
                break
            elif( self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo.__eq__(1) and self.lista_c[self.__procedimiento[3]].cirujanos[i].especialidad ==  "Traumatologo" and (self.__procedimiento[2] == "Hueso")):
                self.__procedimiento.append("Si")
                self.__procedimiento.append(i)
                self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo = 0
                break
            elif(self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo.__eq__(1) and self.lista_c[self.__procedimiento[3]].cirujanos[i].especialidad ==  "Cardiovascular" and (self.__procedimiento[2] == "Corazon")):
                self.__procedimiento.append("Si")
                self.__procedimiento.append(i)
                self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo = 0
                break
            elif(self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo.__eq__(1) and self.lista_c[self.__procedimiento[3]].cirujanos[i].especialidad ==  "Pulmonar" and (self.__procedimiento[2] == "Pulmones")):
                self.__procedimiento.append("Si")
                self.__procedimiento.append(i)
                self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo = 0
                break
            elif(self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo.__eq__(1) and self.lista_c[self.__procedimiento[3]].cirujanos[i].especialidad ==  "Plastico" and (self.__procedimiento[2] == "Piel" or self.__procedimiento[2] == "Corneas")):
                self.__procedimiento.append("Si")
                self.__procedimiento.append(i)
                self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo = 0
                break
            elif(self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo.__eq__(1) and self.lista_c[self.__procedimiento[3]].cirujanos[i].especialidad ==  "General"):
                self.__procedimiento.append("No")
                self.__procedimiento.append(i)
                self.lista_c[self.__procedimiento[3]].cirujanos[i].dispo = 0
                break
            else:
                print("No se ha podido encontrar un doctor disponible")
                self.__procedimiento.clear()
                return True
        return 

    def __viaje(self) -> int:

        '''
            Se fija una fecha y hora de ablacion, ademas que se obtiene 
            el tiempo necesario de viaje para el medio de transporte 
            establecido.

        PARAMETROS:
            -No recibe parametros
        RETURNS:
            -Retorna una variable int la cual contiene el tiempo de viaje
            expresado en horas.
        '''

        self.__procedimiento.append(datetime.now().date())
        self.__procedimiento.append(datetime.now().time())
    
        if self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].tipo == 'Ambulancia':
            trafico = random.randint(0,40)
            distancia = random.randint(60,150)
            tiempo = (distancia +trafico)/self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].velocidad

        elif self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].tipo == 'Helicoptero':
            distancia = random.randint(150, 350)
            tiempo = distancia/self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].velocidad

        elif self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].tipo == 'Avion':
            distancia = random.randint(350, 1000)
            tiempo = distancia / self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].velocidad

        viaje = VIAJES(self.__procedimiento[2], distancia, self.__procedimiento[8])
        self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].registro.append(viaje)

        return tiempo

    def __operar(self, tiempo: int , posicion: int) -> None:
        
        hora_cirugia = datetime.combine(datetime.today(), self.__procedimiento[9]) + timedelta(hours = 20)
        hora_llegada = datetime.combine(datetime.today(), self.__procedimiento[9]) + timedelta(hours = tiempo)
        
        if hora_llegada > hora_cirugia:
            print('La ablacion ha superado las 20 horas.')
            time.sleep(1)

        else:
            exito = random.randint(1,10)
            if (self.__procedimiento[4] == 'Si'):
                if exito > 2:
                    print('La operacion de ', self.__procedimiento[2] ,' del paciente ', self.__procedimiento[0] ,'se realizo exitosamente.')
                    time.sleep(1)
                    del(self.__lista_r[posicion])
                else:
                    print('La operacion de ', self.__procedimiento[2] ,' del paciente ', self.__procedimiento[0] ,'no se realizo exitosamente.')
                    time.sleep(1)
                    self.__lista_r[posicion].prioridad = 4
                    
            else: 
                if exito > 5:
                    print('La operacion de ', self.__procedimiento[2] ,' del paciente ', self.__procedimiento[0] ,'se realizo exitosamente.')
                    time.sleep(1)
                    del(self.__lista_r[posicion])

                else:
                    print('La operacion de ', self.__procedimiento[2] ,' del paciente ', self.__procedimiento[0] ,'no se realizo exitosamente.')
                    time.sleep(1)
                    self.__lista_r[posicion].prioridad = 4
                    
        pos_org = posd = -1
        self.lista_c[self.__procedimiento[3]].cirujanos[self.__procedimiento[7]].dispo = 1
        for i in range(len(self.__lista_d)):
            if self.__lista_d[i].DNI == self.__procedimiento[1]:
                posd = i
                break
        for i in range(len(self.__lista_d[posd].organos)):
            if self.__lista_d[posd].organos[i] == self.__procedimiento[2]:
                pos_org = i
                break

        del(self.__lista_d[posd].organos[pos_org])
        if len(self.__lista_d[posd].organos).__eq__(0):
            print('El donante de DNI:', self.__procedimiento[1] ,'ha sido eliminado, ya que ha donado todos sus organos.')
            del (self.__lista_d[posd])
        self.__procedimiento.clear() 
        return

    def print_pantalla (self) -> None:
        
        '''
            Se imprime en pantalla las listas tanto de 
            receptores como de donantes.

        PARAMETROS:
            -No recibe parametros
        RETURNS:
            -No retorna nada.
        '''
        
        print("Lista de Receptores: ")
        for i in range(len(self.__lista_r)):
            print(self.__lista_r[i].__str__())
        
        print("Lista de Donantes: ")
        for i in range(len(self.__lista_d)):
            print(self.__lista_d[i].__str__())
        return

    def __buscar_prioridad(self, prioridad, organo, sangre):
        pos = cont = -1
        for i in range(len(self.__lista_r)):
            if (self.__lista_r[i].prioridad.__eq__(prioridad) and self.__lista_r[i].organo == organo and self.__lista_r[i].tipo_de_sangre == sangre): 
                espera = self.__lista_r[i].espera 
                if cont.__eq__(-1):
                    fmin=espera
                    pos = i
                    cont = cont + 1
                elif (espera < fmin):
                    fmin=espera
                    pos =i
        return pos