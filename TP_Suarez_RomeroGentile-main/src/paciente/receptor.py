from paciente.paciente import Paciente
from typing import override



class Receptor(Paciente):

    '''
    Esta clase es hija de Paciente y, por ende,
    posee los mismos datos y ademas se instancia
    una una variable entera con la fecha desde la
    cual lleva esperando el paciente, y dos variables
    str con el organo que nesecita el paciente y la 
    prioridad del mismo.
    '''

    def __init__(self, nombre: str, DNI: int , nacimiento: int , sexo: str,  telefono: int, tipo_de_sangre: str, centro_de_salud: str, organo: str, espera: int, prioridad: int):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.organo = organo
        self.espera = espera
        self.prioridad = prioridad 

    @override
    def __str__(self) -> str:
        
        '''
            Se unen todos los datos del receptor en un str.
        PARAMETROS:
            -No recibe nada
        RETURNS:
            -Returna una variable str la cual posee 
            todos los datos del receptor en un str.
        '''
        
        return super().__str__() + f" - Organo: {self.organo} - Tiempo de espera: {self.espera} - Prioridad: {self.prioridad}"