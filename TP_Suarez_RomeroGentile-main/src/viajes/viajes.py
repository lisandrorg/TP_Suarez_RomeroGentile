class Viajes:

    '''
    Esta clase posee los datos necesarios
    para registrar un viaje.
    '''

    def __init__(self, organo: str, distancia: int, fecha: str):
        self.organo = organo 
        self.distancia = distancia 
        self.fecha = fecha

    def __str__(self):
        
        '''
            Se unen todos los datos del viaje en un str.
        PARAMETROS:
            -No recibe nada
        RETURNS:
            -Returna una variable str la cual posee 
            todos los datos del viaje en un str.
        '''

        return f"Organo: {self.organo} - Distancia: {self.distancia} Km - Fecha: {self.fecha}\n"