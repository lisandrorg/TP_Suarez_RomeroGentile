from paciente.paciente import Paciente
from typing import override



class Donante(Paciente):

    '''
    Esta clase es hija de Paciente y, por ende,
    posee los mismos datos y ademas se instancia
    una lista de  str con los organos disponibles 
    para donar.
    '''

    def __init__(self, nombre: str , DNI: int, nacimiento: int, sexo: str, telefono: int, tipo_de_sangre: str, centro_de_salud: str, organos: str):
        super().__init__(nombre, DNI, nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.organos = organos
    
    @override
    def __str__(self) -> str:
        
        '''
            Se unen todos los datos del donante, y 
            se une el array de organos en una unica
            variable de tipo str, con cada posicion 
            separada por ' - '.
        PARAMETROS:
            -No recibe nada
        RETURNS:
            -Returna una variable str la cual posee 
            todos los datos del donante en un str.
        '''

        organos_str = " - ".join(str(a) for a in self.organos)
        return super().__str__() + f" - Órganos: {organos_str}"