class ORGANOS():

    def __init__(self, organo: str, fecha: str, hora: str):
        self.organo = organo
        self.fecha = fecha
        self.hora = hora
    
    def __str__(self):

        return f"{self.organo}"