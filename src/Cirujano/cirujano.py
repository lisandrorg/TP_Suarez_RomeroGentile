class Cirujano:

    '''
    Esta clase posee los datos necesarios
    para registrar un cirujano.
    '''

    def __init__(self, matricula: int, especialidad: str, centro ):
        self.matricula = matricula
        self.especialidad = especialidad 
        self.centro = centro
        self.dispo = 1