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
            
            print("\n Menú:")
            print("1. Registrar paciente")
            print("2. Registrar centro de salud")
            print("3. Registrar vehiculo")
            print("4. Registrar cirujano")
            print("5. Inicializar programa") #preguntar el sentido de esto.
            print("6. Imprimir lista de pacientes registrados") #hay que hacerla con lo del metodo magico
            print("0. Salir")
            eleccion = input("Elige una opción:")

            if (eleccion == "1"):

                nombre = str(input('Ingrese el nombre del paciente: '))
                dni = int(input('Ingrese el DNI del paciente: '))
                nacimiento = str(input('Ingrese la fecha de nacimiento del paciente (Ejemplo: 1990-05-12): ')) #que hacemos si lo ingresan en otro formato
                sexo = str(input('Ingrese el sexo del paciente: '))
                telefono = str(input('Ingrese el telefono del paciente (Ejemplo: 1123456789): '))
                sangre = str(input('Ingrese el tipo de sangre del paciente (Ejemplo: O+): '))
                centro = str(input('Ingrese nombre del centro al que pertenece el paciente: '))
                
                aux = incucai.buscar_centro(centro)
                if aux == False:
                    print("El centro no se encuentra registrado aun")

                else:
                    l = 0
                    while l == 0:
                        print('Ingrese que tipo de paciente desea registrar: ')
                        print('1. Donante')
                        print('2. Receptor')
                        opcion = str(input('Ingrese su respuesta: '))
                        if opcion == '1':
                            k = 0
                            org = []
                            while k == 0:
                                print('Seleccione que organos tiene disponibles para donar el paciente:')
                                print('1. Corazon')
                                print('2. Pulmon')
                                print('3. Piel')
                                print('4. Cornea')
                                print('5. Riñon')
                                print('6. Higado')
                                print('7. Huesos')
                                print('8. Intestino')
                                print('9. Pancreas')
                                print('0. Ya he ingresado todos los organos')
                                opcion_org = str(input('Ingrese su respuesta: '))

                                if opcion_org == '1':
                                    org.append('Corazon')
                                if opcion_org == '2':
                                    org.append('Pulmon')
                                if opcion_org == '3':
                                    org.append('Piel')
                                if opcion_org == '4':
                                    org.append('Cornea')
                                if opcion_org == '5':
                                    org.append('Riñon')
                                if opcion_org == '6':
                                    org.append('Higado')
                                if opcion_org == '7':
                                    org.append('HUesos')
                                if opcion_org == '8':
                                    org.append('Intestino')
                                if opcion_org == '9':
                                    org.append('Pancreas')
                                else:
                                    k=1
                            org = set(org) #esta funcion hace que se borren los elementos repetido
                            donante = DONANTE(nombre, dni, nacimiento, sexo, telefono, sangre, centro, org)
                            incucai.registrar_paciente(donante)
                            l=1
                        elif opcion == '2':
                            espera = int(input('Ingrese la fecha de espera del paciente (si la fecha es 25/04/2025 ingrese 20250425): ')) #verificar como podemos hacer que se respete el formato
                            k=0
                            while k == 0:
                                prioridad = int(input('Ingrese la prioridad del paciente (1,2 o 3): '))
                                if prioridad != (1 or 2 or 3):
                                    print('No se registro su respuesta')
                                else:
                                    k=1
                            print('Ingrese cual es el organo que necesita recibir el paciente: ')
                            k=0
                            while k==0:
                                print('1. Corazon')
                                print('2. Pulmon')
                                print('3. Piel')
                                print('4. Cornea')
                                print('5. Riñon')
                                print('6. Higado')
                                print('7. Huesos')
                                print('8. Intestino')
                                print('9. Pancreas')
                                org = str(input('Ingrese su respuesta: '))
                                if org != ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9'):
                                    print('No se reconocio su respuesta')
                                else:
                                    k=1
                                    if org == '1':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Corazon', espera, prioridad)
                                    elif org == '2':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Pulmon', espera, prioridad)
                                    elif org == '3':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Piel', espera, prioridad)
                                    elif org == '4':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Cornea', espera, prioridad)
                                    elif org == '5':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Riñon', espera, prioridad)
                                    elif org == '6':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Higado', espera, prioridad)
                                    elif org == '7':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Huesos', espera, prioridad)
                                    elif org == '8':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Intestino', espera, prioridad)
                                    elif org == '9':
                                        paciente = RECEPTOR(nombre, dni, nacimiento, sexo, telefono, sangre, centro, 'Pancreas', espera, prioridad)
                                    incucai.registrar_paciente(paciente)
                        else: 
                            print('No se reconocio su respuesta.')

            elif (eleccion == "2"):

                nombre = str(input('Ingrese el nombre del centro: '))
                direccion = str(input('Ingrese la direccion del centro (Ejemplo: "Av. de la Salud 1234, Ciudad Central"): '))
                partido = str(input('Ingrese el partido al que pertenece el centro: '))
                provincia = str(input('Ingrese la provincia a la que pertenece el centro: '))
                centro = CENTRO(nombre, direccion, partido, provincia)
                incucai.registrar_centro(centro)
                #menu para registrar centros de salud
            
            elif (eleccion == "3"):
                centro = CENTRO()
                l = 0
                while l == 0:
                    print('Ingrese que tipo de vehiculo desea registrar: ')
                    print('1. Ambulancia')
                    print('2. Helicoptero')
                    print('3. Avion')
                    opcion = str(input('Ingrese su respuesta: '))

                    if opcion == ('1' or '2' or '3'):
                        patente = str(input('Ingrese la patente del vehiculo: '))
                        velocidad = int(input('Ingrese la velocidad maxima del vehiculo: '))
                        centro = str(input('Ingrese el nombre del centro al que pertenece el vehiculo:'))
                        
                        aux = incucai.buscar_centro(centro)
                        if aux == False:
                            print("El centro no se encuentra registrado aun")
                            l=1
                        else:  
                            if opcion == '1':
                                vehiculo = VEHICULO('Ambulancia', velocidad, patente, centro)
                                incucai.lista_c[aux].registrar_vehiculos(vehiculo)
                            elif opcion == '2':
                                vehiculo = VEHICULO('Helicoptero', velocidad, patente, centro)
                                incucai.lista_c[aux].registrar_vehiculos(vehiculo)
                            else: 
                                vehiculo = VEHICULO('Avion', velocidad, patente, centro)
                                incucai.lista_c[aux].registrar_vehiculos(vehiculo)
                    else:
                        print('No se reconocio su respuesta.')

                #menu para registrar vehiculos
            
            elif (eleccion == "4"):
                centro = CENTRO()
                matricula = str(input('Ingrese el numero de matricula del cirujano:'))
                especialidad = str(input("Ingrese la especialidad del cirujano:"))
                centro = str(input('Ingrese nombre del centro donde trabaja el cirujano:'))
                
                aux = incucai.buscar_centro(centro)
                if aux == False:
                    print("El centro no se encuentra registrado aun.")
                else:
                    cirujano = CIRUJANO(matricula, especialidad, centro)
                    for i in incucai.lista_c:
                        if i == incucai.lista_c[aux]:
                            centro.registrar_cirujano(cirujano)
                            
                 #menu para registrar cirujanos
            
            elif (eleccion == "5"):                
                hospital_central = CENTRO(
                nombre="Hospital Central",
                direccion="Av. de la Salud 1234, Ciudad Central",
                partido="Partido Central",
                provincia="Buenos Aires")
                incucai.registrar_centro(hospital_central)
                hospital_norte = CENTRO(
                nombre="Hospital Norte",
                direccion="Av. de la Salud 5678, Ciudad Norte",
                partido="Partido Norte",
                provincia="Buenos Aires")
                incucai.registrar_centro(hospital_norte)

                cirujano1 = CIRUJANO( 1, 'General',"Hospital Norte" )
                incucai.lista_c[1].registrar_cirujano(cirujano1)
                cirujano2 = CIRUJANO(2, "Gastroenterologo", "Hospital Central")
                incucai.lista_c[0].registrar_cirujano(cirujano2)
                cirujano3 = CIRUJANO( 3,"Plastico", "Hospital Norte")
                incucai.lista_c[1].registrar_cirujano(cirujano3)
                cirujano4 = CIRUJANO(4,"Pulmonar", "Hospital Central")
                incucai.lista_c[0].registrar_cirujano(cirujano4)
                cirujano5 = CIRUJANO(5, "Cardiovascular", "Hospital Norte")
                incucai.lista_c[1].registrar_cirujano(cirujano5)
                cirujano6 = CIRUJANO(6, "Traumatologo", "Hospital Central")
                incucai.lista_c[0].registrar_cirujano(cirujano6)
                #registrar 30

                ambulancia = VEHICULO(
                    "Ambulancia", 'AC473FF', 100, "Hospital Central" 
                )
                incucai.lista_c[0].registrar_vehiculo(ambulancia)
                helicoptero = VEHICULO(
                    "Helicoptero", 'KLI994', 250, "Hospital Norte"
                )
                incucai.lista_c[1].registrar_vehiculo(helicoptero)
                avion = VEHICULO(
                    "Avion", 'AA088OM', 400, "Hospital Central"
                )
                incucai.lista_c[0].registrar_vehiculo(avion)
                #registrar uno de cada para cada centro

                paciente2 = RECEPTOR(
                nombre="Lucia Gómez",
                DNI=21836338,
                nacimiento="1987-07-25",
                sexo="F",
                telefono="1133344455",
                tipo_de_sangre="A+",
                centro_de_salud="Hospital Norte",
                organo="Riñon",
                espera=20250425,
                prioridad="Medio")
                incucai.registrar_paciente(paciente2) 


                paciente1 = DONANTE(
                nombre="Valentin Perez",
                DNI=46962303,
                nacimiento="1990-05-12",
                sexo="M",
                telefono="1123456789",
                tipo_de_sangre="O+",
                centro_de_salud="Hospital Central",
                organos= ["Riñon","Piel","Intestino"]) 
                incucai.registrar_paciente(paciente1) 
    
            elif (eleccion == "0"):
                return
            
            else:
                print("No se registro su respuesta, porfavor reingrese nuevamente una opcion.")
    

if __name__ == "__main__":
    main()