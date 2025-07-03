from paciente.receptor import Receptor
from paciente.donante import Donante
from centro.centro import Centro
from vehiculo.avion import Avion
from vehiculo.ambulancia import Ambulancia
from vehiculo.helicoptero import Helicoptero
from datetime import datetime
import random
from datetime import datetime, timedelta



class Incucai:

    '''
    Esta clase se encarga de llevar a cabo los procedimientos 
    necesarios para que se realize una coincidecia de pacientes,
    transporte de organo y posterior operacion.
    '''

    def __init__(self):
        self.lista_c = [] 
        self.__procedimiento = [] #[0=DNI R, 1=DNI D, 2=Organo, 3=Posicion CD, 4=Posicion CR, 5=Posicion V en CD, 6=Especialidad Cirujano, 7=Posicion Ci en CD, 8=Fecha Ablacion, 9=Hora Ablacion]
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

    def buscar_donante(self, DNI: str) -> int:
        
        '''
            Permite saber la posicion de un donante en la lista de donantes
        PARAMETROS:
            -DNI: una variable de tipo string en el cual se 
            recibe el DNI de un donante
        RETURNS:
            -Retorna un entero, igual a -1 en caso del donante no estar en la lista
            de los donantes registrados, caso contrario, devuelve la
            posicion de dicho donante en la lista
        '''
        
        for i in range(len(self.lista_c)):
            if self.__lista_d[i].DNI == DNI:
                return i 
        return -1

    def buscar_receptor(self, DNI: str) -> int:
        
        '''
            Permite saber la posicion de un receptor en la lista de receptores
        PARAMETROS:
            -DNI: una variable de tipo string en el cual se 
            recibe el DNI de un receptor
        RETURNS:
            -Retorna un entero, igual a -1 en caso del receptor no estar en la lista
            de los receptores registrados, caso contrario, devuelve la
            posicion de dicho receptor en la lista.
        '''
        
        for i in range(len(self.lista_c)):
            if self.__lista_r[i].DNI == DNI:
                return i 
        return -1

    def registrar_paciente(self, paciente: Receptor|Donante) -> None: 
        
        '''
            Se puede registrar un paciente, este es filtrado dependiendo de 
            si es receptor o donante, pero antes se verifica que no esté previamente 
            registrado y que este asociado a un centro de salud registrado en el 
            sistema. En caso de encontrar un paciente ya registrado se muestra
            un mensaje en pantalla dando a conocer esto, en caso de registrarse 
            correctamente al paciente tambien se muestra un mensaje en pantalla 
            y si el paciente era donante se busca un match inmediatamente.
        PARAMETROS:
            -paciente: una variable de tipo Receptor o Donante 
        RETURNS:
            -No retorna nada.
        '''

        for i in self.__lista_d + self.__lista_r:
            if(i.DNI.__eq__(paciente.DNI) or i.DNI.__eq__(paciente.DNI)):
                print("El paciente con DNI:", paciente.DNI ,"ya se encuentra registrado.")
                return

        cont = 0
        for i in self.lista_c: 
            cont = self.buscar_centro(i.nombre)
            if cont != -1:
                break

        if cont.__eq__(-1):
            print("El paciente con DNI:", paciente.DNI, "pertenece a un centro de salud no registrado.")
            return
        
        if type(paciente) == Donante: 
            self.__lista_d.append(paciente)
            print("Se ha registrado al paciente exitosamente.")
            self.__match_por_ingreso_inmediato(paciente)
        elif type(paciente) == Receptor:
            self.__lista_r.append(paciente)
            print("Se ha registrado al paciente exitosamente.")
        else: 
            print('No se ha podido registrar al paciente, intente nuevamente.')
            return

    def registrar_centro(self, centro: Centro) -> None:
        
        '''
            Se puede registrar un centro, verifica que no esté previamente 
            registrado y en caso que no lo este se lo añade a la lista. 
            Imprime en pantalla un mensaje indicando que ocurrio.
        PARAMETROS:
            -centro: un argumento de tipo CENTRO
        RETURNS:
            -No retorna nada.
        '''

        if type(centro) == Centro:
            for i in self.lista_c: 
                if(i.nombre.__eq__(centro.nombre)):
                    print("El centro:", centro.nombre ,"ya se encuentra registrado.")
                    return
            self.lista_c.append(centro)
            print("Se ha registrado el centro.")

        else: 
            print("No se ha podido registrar el centro, intente nuevamente.")
            return

    def __match_por_ingreso_inmediato(self, paciente: Donante) -> None:
        
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
            p = [pos4, pos3, pos2, pos1]
            cont = self.__detectar_paciente(p, paciente)
        if cont==0:
            print('No se han encontrado coincidencias.')
            return

    def match_por_llamado_del_menu (self) -> None:
        
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
        for d in range(len(self.__lista_d)):  
            pos4 = pos3 = pos2 = pos1 = -1
            if cont == 1:
                break
            for k in self.__lista_d[d].organos:
                if pos1.__ne__(-1) or pos2.__ne__(-1) or pos3.__ne__(-1) or pos4.__ne__(-1):
                    break
                pos4 = self.__buscar_prioridad(4, k, self.__lista_d[d].tipo_de_sangre)
                pos3 = self.__buscar_prioridad(3, k, self.__lista_d[d].tipo_de_sangre)
                pos2 = self.__buscar_prioridad(2, k, self.__lista_d[d].tipo_de_sangre)
                pos1 = self.__buscar_prioridad(1, k, self.__lista_d[d].tipo_de_sangre)
                p = [pos4, pos3, pos2, pos1]
                cont = self.__detectar_paciente(p, self.__lista_d[d])
        if cont==0:
            print('No se han encontrado coincidencias.')
            return
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
        d = self.buscar_donante(self.__procedimiento[1])
        pcd = self.buscar_centro(self.__lista_d[d].centro_de_salud) 
        self.__procedimiento.append(pcd)

        pcr = self.buscar_centro(self.__lista_r[posicion].centro_de_salud)
        self.__procedimiento.append(pcr)
        condicion1 = (self.lista_c[pcd].provincia != self.lista_c[pcr].provincia)
        condicion2 =(self.lista_c[pcd].partido != self.lista_c[pcr].partido)

        if (condicion1==True):
            pos = self.lista_c[pcd].buscar_vehiculo(Avion)
        elif condicion2==True: 
            pos = self.lista_c[pcd].buscar_vehiculo(Helicoptero)
        else: 
            pos = self.lista_c[pcd].buscar_vehiculo(Ambulancia)
        if pos.__eq__(-1):
            print('No se encontraron vehiculos disponibles para el transporte.')
            self.__procedimiento.clear()
            return True
        else:
            self.__procedimiento.append(pos)

        i=-1
        if self.__procedimiento[2] in ("Intestino" or  "Riñon" or  "Higado" or "Pancreas"):
            i = self.lista_c[pcd].buscar_cirujano('Gastroenterologo')
            self.__verificar_especialidad(i)
        elif self.__procedimiento[2] == 'Huesos':
            i = self.lista_c[pcd].buscar_cirujano('Traumatologo')
            self.__verificar_especialidad(i)
        elif self.__procedimiento[2] == "Corazon":
            i = self.lista_c[pcd].buscar_cirujano('Cardiovascular')
            self.__verificar_especialidad(i)
        elif self.__procedimiento[2] == "Pulmon":
            i = self.lista_c[pcd].buscar_cirujano('Pulmonar')
            self.__verificar_especialidad(i)
        elif self.__procedimiento[2] in ("Piel" or "Cornea"):
            i = self.lista_c[pcd].buscar_cirujano('Plastico')
            self.__verificar_especialidad(i)
        else:
            i = self.lista_c[pcd].buscar_cirujano('General')
            self.__procedimiento.append('No')
            self.__procedimiento.append(i)

        if (i == -1):
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
        tiempo = self.lista_c[self.__procedimiento[3]].vehiculos[self.__procedimiento[5]].calcular_distancia(self.__procedimiento[2], self.__procedimiento[8]) #Accedo a la posicion del vehiculo en en el array de vehiculos de su centor y calculo distancia con el metodo propio del vehiculo
        return tiempo

    def __operar(self, tiempo: int , posicion: int) -> None:
        
        '''
            Se fija una hora de cirugia y llegada,
        PARAMETROS:
            -tiempo: una variable de tipo int que
            contiene las horas de viaje del transporte
            -posicion: una variable de tipo int que contiene
            la posicion del receptor en la lista de receptores
        RETURNS:
            -No retorna nada.
        '''
        
        hora_cirugia = datetime.combine(datetime.today(), self.__procedimiento[9]) + timedelta(hours = 20)
        hora_llegada = datetime.combine(datetime.today(), self.__procedimiento[9]) + timedelta(hours = tiempo)
        
        if hora_llegada > hora_cirugia:
            print('La ablacion ha superado las 20 horas.')
            self.__procedimiento(2,1,posicion)
        else:
            valor = random.randint(1,10)
            if (self.__procedimiento[4] == 'Si'):
                self.__operacion(2, valor, posicion)
            else: 
                self.__operacion(5, valor, posicion)

        self.__borrar_organo_donado()

    def print_pantalla(self) -> None:
        
        '''
            Se imprime en pantalla las listas tanto de 
            receptores como de donantes.
        PARAMETROS:
            -No recibe parametros
        RETURNS:
            -No retorna nada.
        '''
        
        print("\nLista de Receptores: ")
        for i in range(len(self.__lista_r)):
            print(self.__lista_r[i].__str__())
        
        print("\n Lista de Donantes: ")
        for i in range(len(self.__lista_d)):
            print(self.__lista_d[i].__str__())
        return

    def __buscar_prioridad(self, prioridad: int, organo: str, sangre: str) -> int:
        
        '''
            Se imprime en pantalla las listas tanto de 
            receptores como de donantes.
        PARAMETROS:
            -prioridad: una variable int que contiene 
            la prioridad del paciente a buscar
            -organo: una variable str que contiene el
            organo a donar
            -sangre: una variable str que contiene el 
            tipo de sangre que posee el donante
        RETURNS:
            -Returna una variable pos de tipo int
            que contiene la posicion del receptor en
            el array de receptores. En caso de no 
            encontrar a un receptor devuelve un -1.
        '''

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
                    pos = i
        return pos

    def __detectar_paciente (self, pos: list, paciente: Donante) -> None:
        
        '''
            Se verifica la posicion del receptor elegido
            para llevar a cabo la cirugia, posteriormente 
            se llama a las funciones encargadas de las demas
            tareas.
        PARAMETROS:
            -pos: una lista que contiene variables de tipo 
            int con las posiciones de los posibles receptores
            -paciente: una variable del tipo Donante que posee 
            al donante que entregara su organo para la cirugia
        RETURNS:
            -No retorna nada.
        '''

        cont = 0
        for i in pos:
            if (i != -1):
                cont = 1
                self.__procedimiento.append(self.__lista_r[i].DNI)
                self.__procedimiento.append(paciente.DNI)
                self.__procedimiento.append(self.__lista_r[i].organo)
                aux = self.__transporte(i)
                if(aux == True): 
                    return
                tiempo=self.__viaje()
                self.__operar(tiempo, i)
                break
        return cont

    def __verificar_especialidad(self, pos: int) -> None:
        
        '''
            Se verifica si el cirujano elegido previamente
            es especializado en el organo a operar. Se guarda
            un string 'Si' en caso de que haya un cirujano 
            asignado y se guarda su posicion en su lista.
        PARAMETROS:
            -pos: una variable int que contiene la posicion 
            del cirujano en el array de cirujano dentro de 
            la lista de cirujanos de su centro de salud.
        RETURNS:
            -No retorna nada.
        '''

        if pos != -1:
            self.__procedimiento.append('Si')
            self.__procedimiento.append(pos)
        return

    def __operacion (self, exito: int, valor: int, posicion: int) -> None:
        
        '''
            Se verifica si la operacion fue exitosa o no,
            y se imprime en pantalla un mensaje para que
            el usuario conozca el resultado.
        PARAMETROS:
            -exito: una variable de tipo int que contiene
            el valor al cual hay que superar para que la 
            operacion se realice exitosamente.
            -valor: una variable de tipo int que contiene
            el valor obtenido con el que se comparara para 
            saber si la operacion fue exitosa o no.
            -posicion: una variable int que posee la 
            posicion del receptor en la lista de receptores.
        RETURNS:
            -No retorna nada.
        '''

        if valor > exito:
            print('La operacion de ', self.__procedimiento[2] ,' del paciente ', self.__lista_r[posicion].nombre ,' se realizo exitosamente.')
            del(self.__lista_r[posicion])
        else:
            print('La operacion de ', self.__procedimiento[2] ,' del paciente ', self.__lista_r[posicion].nombre ,'no fue exitosa.')
            self.__lista_r[posicion].prioridad = 4
        return

    def __borrar_organo_donado(self) -> None:
        
        '''
            Se elimina el organo donado en la lista de
            organos del donante, y se verifica que aun 
            posea organos disponibles para donar. En 
            caso que no hayan mas organos disponibles 
            se elimina al donante de la lista de donantes
        PARAMETROS:
            -No se reciben parametros.
        RETURNS:
            -No retorna nada.
        '''

        pos_org = -1
        posd= self.buscar_donante(self.__procedimiento[1])
        
        for i in range(len(self.__lista_d[posd].organos)):
            if self.__lista_d[posd].organos[i] == self.__procedimiento[2]:
                pos_org = i
                break
        
        del(self.__lista_d[posd].organos[pos_org])
        if len(self.__lista_d[posd].organos).__eq__(0):
            print('El donante ', self.__lista_d[posd].nombre ,' ha sido eliminado, ya que ha donado todos sus organos.')
            del (self.__lista_d[posd])
        self.__procedimiento.clear() 
        return
