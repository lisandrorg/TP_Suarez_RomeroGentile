from centro_de_salud import CENTRO
from cirujano import CIRUJANO
from donante import DONANTE
from receptor import RECEPTOR
from vehiculo import VEHICULO
from INCUCAI import INCUCAI
from paciente import PACIENTE
from organo import ORGANOS

def main():
    incucai = INCUCAI()
    i=0
    while i == 0:
            print("\nMenú:")
            print("1. Registrar Paciente")
            print("2. Registrar centro de atencion")
            print("3. Registrar vehiculo")
            print("4. Registrar cirujano")
            print("0. Salir")
            eleccion = input("Elige una opción:")
            
            if (eleccion == 1):
                paciente1 = DONANTE(
                nombre="Valentin Perez",
                DNI=46962303,
                nacimiento="1990-05-12",
                sexo="M",
                telefono="1123456789",
                tipo_de_sangre="O+",
                centro_de_salud="Hospital Central",
                fecha_muerte="2025-01-01",
                hora_muerte="15:30",
                fecha_ablacion="2025-01-02",
                hora_ablacion="16:00", 
                organos= ["Riñon","Piel","Intestino"]) #acordarse que falta los organos que puede donar (habria que hacer un array de organos disponibles con la funcion enum)
                
                incucai.registrar_paciente(paciente1)  # Ahora pasamos el objeto paciente1 del tipo DONANTE
                
                paciente2 = RECEPTOR(
                nombre="Lucia Gómez",
                DNI=21836338,
                nacimiento="1987-07-25",
                sexo="F",
                telefono="1133344455",
                tipo_de_sangre="A+",
                centro_de_salud="Hospital Norte",
                organo="Riñon",
                espera="2025-04-25",
                prioridad="Medio",
                patologia="Insuficiencia renal",
                estado="Estable")
                incucai.registrar_paciente(paciente2)  # Ahora pasamos el objeto paciente2 del tipo RECEPTOR
            elif (eleccion == 2):
                hospital_central = CENTRO(
                nombre="Hospital Central",
                direccion="Av. de la Salud 1234, Ciudad Central",
                partido="Partido Central",
                provincia="Provincia Central")
                incucai.registrar_centro(hospital_central)
                
                hospital_norte = CENTRO(
                nombre="Hospital Norte",
                direccion="Av. de la Salud 5678, Ciudad Norte",
                partido="Partido Norte",
                provincia="Provincia Norte")
                incucai.registrar_centro(hospital_norte)
            elif (eleccion == 3):
                ambulancia = VEHICULO(
                    "Ambulancia", 'AC473FF', 100, "Hospital Central" 
                )
                incucai.registrar_vehiculo(ambulancia)
                helicoptero = VEHICULO(
                    "Helicoptero", 'KLI994', 250, "Hospital Norte"
                )
                incucai.registrar_vehiculo(helicoptero)
                avion = VEHICULO(
                    "Avion", 'AA088OM', 400, "Hospital Central"
                )
                incucai.registrar_vehiculo(avion)
            
            elif (eleccion == 4):
                cirujano1 = CIRUJANO( 1, 'General',"Hospital Norte" )
                incucai.registrar_cirujano(cirujano1)
                cirujano2 = CIRUJANO(2, "Gastroenterologo", "Hospital Central")
                incucai.registrar_cirujano(cirujano2)
                cirujano3 = CIRUJANO( 3,"Plastico", "Hospital Norte")
                incucai.registrar_cirujano(cirujano3)
                cirujano4 = CIRUJANO(4,"Pulmonar", "Hospital Central")
                incucai.registrar_cirujano(cirujano4)
                cirujano5 = CIRUJANO(5, "Cardiovascular", "Hospital Norte")
                incucai.registrar_cirujano(cirujano5)
                cirujano6 = CIRUJANO(6, "Traumatologo", "Hospital Central")
                incucai.registrar_cirujano(cirujano6)
            elif (eleccion == 0):
                break
            else:
                print("no se registro su respuesta, porfavor reingrese nuevamente una opcion.")

    if __name__ == "__main__":
        main()