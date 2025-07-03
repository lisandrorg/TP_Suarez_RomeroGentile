from abc import abstractmethod



class Paciente:

    '''
    Esta clase posee todos los datos necesarios
    para registrar un paciente. 
    '''

    def __init__(self, nombre: str, DNI: int, nacimiento: int, sexo: str, telefono: int, tipo_de_sangre: str, centro_de_salud: str):
        self.nombre = nombre 
        self.DNI = DNI
        self.nacimiento = nacimiento 
        self.sexo = sexo
        self.telefono = telefono
        self.tipo_de_sangre = tipo_de_sangre
        self.centro_de_salud = centro_de_salud

    def __str__(self) -> str:
        
        '''
            Se unen todos los datos del paciente en un str.
        PARAMETROS:
            -No recibe nada
        RETURNS:
            -Returna una variable str la cual posee 
            todos los datos del receptor en un str.
        '''
        
        return f"\n{self.nombre} - {self.DNI} - {self.nacimiento} - {self.sexo} - {self.telefono} - {self.tipo_de_sangre} - {self.centro_de_salud}"
