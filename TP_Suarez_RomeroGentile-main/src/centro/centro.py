from vehiculo.vehiculo import Vehiculo
from cirujano.cirujano import Cirujano
from vehiculo.avion import Avion
from vehiculo.ambulancia import Ambulancia
from vehiculo.helicoptero import Helicoptero



class Centro:

    '''
    Esta clase posee todos los datos necesarios
    para registrar un centro. Ademas, es capaz de
    registrar cirujano y vehiculos.
    '''

    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.cirujanos = []
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo: Vehiculo) -> None:
        
        '''
            Se recibe un vehiculo, en caso de ya estar 
            registrado se imprime un mensaje en pantalla
            antes de retornar. Caso contrario, se lo agrega
            a la lista de vehiculos y se imprime un mensaje
            en pantalla. 
        PARAMETROS:
            -vehiculo: una variable de tipo Vehiculo
        RETURNS:
            -No retorna nada.
        '''

        for i in self.vehiculos: 
            if(i.patente == vehiculo.patente):
                print("El vehiculo ya se encontraba registrado")
                return
        self.vehiculos.append(vehiculo)
        print("El vehiculo se ha registrado con exito.")

    def registrar_cirujano(self, cirujano: Cirujano) -> None:
        
        '''
            Se recibe un cirujano, en caso de ya estar 
            registrado se imprime un mensaje en pantalla
            antes de retornar. Caso contrario, se lo agrega
            a la lista de cirujanos y se imprime un mensaje
            en pantalla.
        PARAMETROS:
            -vehiculo: una variable de tipo Vehiculo
        RETURNS:
            -No retorna nada.
        '''
        
        for i in self.cirujanos:
            if(i.matricula == cirujano.matricula):
                print("El cirujano ya se encontraba registrado")
                return
        self.cirujanos.append(cirujano)
        print("El cirujano se ha registrado con exito.")

    def buscar_vehiculo (self, tipo: Avion|Ambulancia|Helicoptero) -> int:
        
        '''
            Se busca un vehiculo del tipo necesario y disponible,
            en caso de hallarlo se modifica su disponibilidad y se
            guarda su posicion en el array de vehiculos.
        PARAMETROS:
            -tipo: una variable hija de Vehiculo que determina que 
            tipo de vehiculo se necesita para transportar el organo
        RETURNS:
            -Retorna un entero, igual a -1 en caso de no encontrar un
            vehiculo en la lista de los vehiculos registrados, caso 
            contrario, devuelve la posicion del vehiculo en la lista.
        '''
        
        pos=-1
        for i in range(len(self.vehiculos)):
            if(type(self.vehiculos[i]) == tipo and self.vehiculos[i].dispo == 1):
                self.vehiculos[i].dispo = 0
                pos = i
                break
        return pos

    def buscar_cirujano (self, especialidad: str) -> int:
        
        '''
            Se busca un cirujano del tipo necesario y disponible,
            en caso de hallarlo se modifica su disponibilidad y se
            guarda su posicion en el array de cirujanos.
        PARAMETROS:
            -especialidad: una variable de tipo str que contiene 
            la especialidad del cirujano para operar
        RETURNS:
            -Retorna un entero, igual a -1 en caso de no encontrar un
            cirujano en la lista de los vehiculos registrados, caso 
            contrario, devuelve la posicion del cirujano en la lista.
        '''

        pos = -1
        for i in range(len(self.cirujanos)):
            if self.cirujanos[i].especialidad == especialidad and self.cirujanos[i].dispo == 1:
                self.cirujanos[i].dispo == 0
                pos=i                    
                break
        return pos
