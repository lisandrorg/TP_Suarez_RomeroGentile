from centro.centro import Centro
from cirujano.cirujano import Cirujano
from paciente.donante import Donante
from paciente.receptor import Receptor
from vehiculo.ambulancia import Ambulancia
from vehiculo.avion import Avion
from vehiculo.helicoptero import Helicoptero
from incucai.incucai import Incucai



class Menu:

    def __init__(self):
        self.incucai = Incucai()

    def mostrar_menu(self):
        i=0
        while i == 0:
                
                print("\n Menú:")
                print("1. Registrar paciente")
                print("2. Registrar centro de salud")
                print("3. Registrar vehiculo")
                print("4. Registrar cirujano")
                print("5. Inicializar programa") 
                print("6. Buscar coincidencia")
                print("7. Imprimir lista de pacientes registrados")
                print("8. Ver registro de viajes de un vehiculo")
                print("0. Salir")
                eleccion = input("Elige una opción:")

                if (eleccion == "1"):
                    l = 0
                    while l == 0:
                        try:
                            DNI = int(input("Ingrese el DNI del paciente: "))
                            if DNI <= 0 or len(str(DNI)) > 8:
                                print('Ingrese su respuesta en el formato adecuado.')
                                continue
                            else:
                                l=1
                        except ValueError:
                                    print("Por favor, ingrese su respuesta en el formato correcto.")
                    l=0
                    cont = 0
                    while l==0:
                        nombre = input("Ingrese nombre del paciente: ")
                        for letra in nombre: 
                            ascii_valor = ord(letra) 
                            if not ((65 <= ascii_valor <= 90) or (97 <= ascii_valor <= 122) or ascii_valor == 32):
                                print("Ingrese su respuesta en el formato correcto.")
                                cont=1
                                break    
                        if cont == 1:
                            l = 0
                            cont=0
                        elif cont == 0: 
                            l = 1

                    l=0
                    while l==0:
                            try:
                                nacimiento = int(input('Ingrese la fecha de nacimiento del paciente (Ejemplo: 17052025, si nacio el 17/05/2025): '))
                                if (7>len(str(nacimiento)) or len(str(nacimiento))<8 or nacimiento<0 or nacimiento > 31122025):
                                    print('Ingrese su respuesta en el formato correcto.')
                                else:
                                    l = 1
                            except ValueError:
                                print("Por favor, ingrese su respuesta en el formato correcto.")
                                continue                
                    
                    l=0
                    while l == 0:
                        sexo = str(input("Ingrese el sexo de su paciente(M/F): "))
                        if sexo != "M" and sexo != "F":
                            print("Por favor, ingrese su sexo en el formato correcto.")
                            continue
                        else:
                            l=1

                    l=0
                    while l==0:
                        try:
                            telefono = int(input('Ingrese el telefono del paciente, sin el codigo de area (Ejemplo: 1123456789): '))
                            if len(str(telefono)) != 10:
                                print('Por favor, ingrese su respuesta en el formato correcto.')
                                l=0
                            else: 
                                l=1
                        except ValueError:
                            print("Por favor ingrese su telefono en el formato correcto.")
                            continue
                    
                    l=0
                    while l==0:
                        sangre = str(input('Ingrese el tipo de sangre del paciente, en mayusculas (Ejemplo: O+): '))
                        if sangre != "A+" and sangre != "A-" and sangre != "B+" and sangre != "B-" and sangre != "0+" and sangre != "0-" and sangre != "AB+" and sangre != "AB-":
                            print("Por favor, ingrese su tipo de sangre en el formato correcto.")
                            continue
                        l=1

                    l=0
                    while l==0:
                        centro = str(input('Ingrese nombre del centro al que pertenece el paciente: ')) 
                        aux = self.incucai.buscar_centro(centro)
                        l=1
                        if aux == -1:
                            print("El centro no se encuentra registrado aun")
                            l=0

                    else:
                        l = 0
                        while l == 0:
                            try:
                                print('Ingrese que tipo de paciente desea registrar: ')
                                print('1. Donante')
                                print('2. Receptor')
                                opcion = str(input('Ingrese su respuesta: '))
                                if opcion == '1':
                                    k = 0
                                    org = []
                                    while k == 0:
                                        try:
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
                                            opcion_org = int(input('Ingrese su respuesta: '))
                                            if opcion_org == 1:
                                                org.append('Corazon')
                                            elif opcion_org == 2:
                                                org.append('Pulmon')
                                            elif opcion_org == 3:
                                                org.append('Piel')
                                            elif opcion_org == 4:
                                                org.append('Cornea')
                                            elif opcion_org == 5:
                                                org.append('Riñon')
                                            elif opcion_org == 6:
                                                org.append('Higado')
                                            elif opcion_org == 7:
                                                org.append('Huesos')
                                            elif opcion_org == 8:
                                                org.append('Intestino')
                                            elif opcion_org == 9:
                                                org.append('Pancreas')
                                            elif opcion_org == 0:
                                                if (len(org)!=0):
                                                    org = set(org) 
                                                    org = list(org)
                                                    donante = Donante(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, org)
                                                    self.incucai.registrar_paciente(donante)
                                                    k = l = 1
                                                else:
                                                    print('Por favor ingrese una respuesta.')
                                            else :
                                                print("No se reconocio su respuesta.")
                                        except ValueError:
                                            print('No se reconocio su respuesta.')
                                            continue

                                elif opcion == '2':
                                    l=0
                                    while l==0:
                                        try:
                                            espera = int(input('Ingrese la fecha de espera del paciente (si la fecha es 25/04/2025 ingrese 20250425): ')) #verificar como podemos hacer que se respete el formato
                                            if espera <= 0 or espera > 20251231 or len(str(espera)) != 8:
                                                print('No se reconocio su respuesta')
                                                continue
                                            else:
                                                l=1
                                        except ValueError:
                                            print('No se reconocio su respuesta.')
                                            continue
                                    
                                    k=0
                                    while k == 0:
                                        try:
                                            prioridad = int(input('Ingrese la prioridad del paciente (1,2 o 3): '))
                                            if prioridad not in (1,2,3):
                                                print('No se registro su respuesta')
                                            else:
                                                k=1
                                        except ValueError:
                                            print('No se reconocio su resuesta')
                                            continue
                                    
                                    print('Ingrese cual es el organo que necesita recibir el paciente: ')
                                    k=0
                                    while k==0:
                                        try:
                                            print('1. Corazon')
                                            print('2. Pulmon')
                                            print('3. Piel')
                                            print('4. Cornea')
                                            print('5. Riñon')
                                            print('6. Higado')
                                            print('7. Huesos')
                                            print('8. Intestino')
                                            print('9. Pancreas')
                                            org = int(input('Ingrese su respuesta: '))
                                            if (org != 1) and (org != 2) and (org != 3) and (org != 4) and (org != 5) and (org != 6) and (org != 7) and (org != 8) and (org != 9):
                                                print('No se reconocio su respuesta')
                                            else:
                                                k = l = 1
                                                if org == 1:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Corazon', espera, prioridad)
                                                elif org == 2:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Pulmon', espera, prioridad)
                                                elif org == 3:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Piel', espera, prioridad)
                                                elif org == 4:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Cornea', espera, prioridad)
                                                elif org == 5:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Riñon', espera, prioridad)
                                                elif org == 6:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Higado', espera, prioridad)
                                                elif org == 7:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Huesos', espera, prioridad)
                                                elif org == 8:
                                                    receptor = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Intestino', espera, prioridad)
                                                elif org == 9:
                                                    receptor  = Receptor(nombre, DNI, nacimiento, sexo, telefono, sangre, centro, 'Pancreas', espera, prioridad)
                                                self.incucai.registrar_paciente(receptor)
                                        except ValueError:
                                            print('No se reconocio su respuesta.')
                                            continue
                                else: 
                                    print('No se reconocio su respuesta.')
                            except:
                                print('No se reconocio su respuesta.')
                                continue

                elif (eleccion == "2"):

                    nombre = str(input('Ingrese el nombre del centro: '))
                    direccion = str(input('Ingrese la direccion del centro (Ejemplo: "Av. de la Salud 1234, Ciudad Central"): '))
                    partido = str(input('Ingrese el partido al que pertenece el centro: '))
                    provincia = str(input('Ingrese la provincia a la que pertenece el centro: '))
                    centro = Centro(nombre, direccion, partido, provincia)
                    self.incucai.registrar_centro(centro)
                
                elif (eleccion == "3"):
                    
                    l = 0
                    while l == 0:
                        print('Ingrese que tipo de vehiculo desea registrar: ')
                        print('1. Ambulancia')
                        print('2. Helicoptero')
                        print('3. Avion')
                        print('0. Volver al menu')
                        try:
                            opcion = int(input('Ingrese su respuesta: '))
                            if opcion == 0:
                                l=1
                                continue
                            if opcion == 1 or opcion == 2 or opcion == 3:
                                k=0
                                while k == 0:
                                    patente = str(input('Ingrese la patente del vehiculo: '))
                                    patente = patente.upper()
                                    a = patente.isalnum()
                                    if a == False:
                                        print('Ingrese una respuesta valida.')
                                    else:
                                        k = 1
                                k=0
                                while k==0:
                                    try:
                                        velocidad = int(input('Ingrese la velocidad maxima del vehiculo en km/h: '))
                                        if 650<velocidad or velocidad<=120:
                                            print('Ingrese una respuesta valida.')
                                            continue
                                        else:
                                            k=1
                                    except ValueError:
                                        print('Ingrese una respuesta valida.')
                                        continue
                                
                                centro = str(input('Ingrese el nombre del centro al que pertenece el vehiculo:'))
                                
                                aux = self.incucai.buscar_centro(centro)
                                if aux == -1:
                                    print("El centro no se encuentra registrado aun")
                                else:  
                                    if opcion == 1:
                                        vehiculo = Ambulancia(velocidad, patente, centro)
                                        self.incucai.lista_c[aux].registrar_vehiculo(vehiculo)
                                    elif opcion == 2:
                                        vehiculo = Helicoptero(velocidad, patente, centro)
                                        self.incucai.lista_c[aux].registrar_vehiculo(vehiculo)
                                    elif opcion == 3: 
                                        vehiculo = Avion(velocidad, patente, centro)
                                        self.incucai.lista_c[aux].registrar_vehiculo(vehiculo)
                            else:
                                print('No se reconocio su respuesta.')
                        except ValueError:
                            print('No se reconocio su respuesta.')
                            continue
                
                elif (eleccion == "4"):
                    k=l=0
                    while k == 0:
                        try:
                            matricula = int(input('Ingrese el numero de matricula del cirujano: ')) 
                            if matricula < 0:
                                print('Respuesta invalida')
                            else:
                                k=1
                        except ValueError:
                            print('Ingrese una respuesta valida')
                            continue

                    while l == 0:
                        print("Ingrese la especialidad del cirujano:")
                        print('1. Gastroenterologo')
                        print('2. Traumatologo')
                        print('3. Cardiovascular')
                        print('4. Plastico')
                        print('5. Pulmonar')
                        print('6. General')
                        try:
                            respuesta= int(input('Ingrese su respuesta: '))
                            if respuesta not in (1, 2, 3, 4, 5, 6):
                                print('Opcion invalida')
                                continue
                            else:
                                if respuesta == 1:
                                    especialidad = 'Gastroenterologo'
                                elif respuesta == 2:
                                    especialidad = 'Traumatologo'
                                elif respuesta == 3:
                                    especialidad = 'Cardiovascular'
                                elif respuesta == 4:
                                    especialidad = 'Plastico'
                                elif respuesta == 5:
                                    especialidad = 'Pulmonar'
                                elif respuesta == 6:
                                    especialidad = 'General'
                                l=1
                            centro = str(input('Ingrese nombre del centro donde trabaja el cirujano: '))
                            aux = self.incucai.buscar_centro(centro)
                            if aux == -1:
                                print("El centro no se encuentra registrado aun.")
                            else:
                                cirujano = Cirujano(matricula, especialidad, centro)
                                self.incucai.lista_c[aux].registrar_cirujano(cirujano)
                        except ValueError:
                            print('Respuesta invalida')
                            continue
                
                elif (eleccion == "5"):
                    nombres = ["Hospital Norte", "Hospital Central", "Hospital Sur", "Hospital Oeste", "Hospital Este"]
                    direccion = ["Av. de la Salud 1234", "Av. de la Salud 5678", "Av. de la Sangre 1382", "Gallo 1330", "Ferrer 1920"]
                    partido = ["Partido Norte", "Partido Central", "Partido Sur", "Capital Federal", "Ituzaingo"]
                    provincia =["Cordoba", "Buenos Aires", "CABA", "CABA", "Corrientes"]
                    for a in range(len(nombres)):
                        nombre=nombres[a]
                        direc=direccion[a]
                        par=partido[a]
                        pro=provincia[a]
                        centro = Centro(nombre, direc, par, pro)
                        self.incucai.registrar_centro(centro)
                
                    cirujano1 = Cirujano(
                        matricula = 1001,
                        especialidad = "Traumatologo",
                        centro = "Hospital Central"
                    )
                    cirujano2 = Cirujano(
                        matricula = 1002,
                        especialidad = "Cardiovascular",
                        centro = "Hospital Norte"
                    )
                    cirujano3 = Cirujano(
                        matricula = 1003,
                        especialidad = "Gastroenterologo",
                        centro = "Hospital Este"
                    )
                    cirujano4 = Cirujano(
                        matricula = 1004,
                        especialidad = "Plastico",
                        centro = "Hospital Oeste"
                    )
                    cirujano5 = Cirujano(
                        matricula = 1005,
                        especialidad = "Pulmonar",
                        centro = "Hospital Central"
                    )
                    cirujano6 = Cirujano(
                        matricula = 1006,
                        especialidad = "General",
                        centro = "Hospital Norte"
                    )
                    cirujano7 = Cirujano(
                        matricula = 1007,
                        especialidad = "Traumatologo",
                        centro = "Hospital Este"
                    )
                    cirujano8 = Cirujano(
                        matricula = 1008,
                        especialidad = "Cardiovascular",
                        centro = "Hospital Oeste"
                    )
                    cirujano9 = Cirujano(
                        matricula = 1009,
                        especialidad = "Gastroenterologo",
                        centro = "Hospital Central"
                    )
                    cirujano10 = Cirujano(
                        matricula = 1010,
                        especialidad = "Plastico",
                        centro = "Hospital Norte"
                    )
                    cirujano11 = Cirujano(
                        matricula = 1011,
                        especialidad = "Pulmonar",
                        centro = "Hospital Este"
                    )
                    cirujano12 = Cirujano(
                        matricula = 1012,
                        especialidad = "General",
                        centro = "Hospital Oeste"
                    )
                    cirujano13 = Cirujano(
                        matricula = 1013,
                        especialidad = "Traumatologo",
                        centro = "Hospital Central"
                    )
                    cirujano14 = Cirujano(
                        matricula = 1014,
                        especialidad = "Cardiovascular",
                        centro = "Hospital Norte"
                    )
                    cirujano15 = Cirujano(
                        matricula = 1015,
                        especialidad = "Gastroenterologo",
                        centro = "Hospital Este"
                    )
                    cirujano16 = Cirujano(
                        matricula = 1016,
                        especialidad = "Plastico",
                        centro = "Hospital Oeste"
                    )
                    cirujano17 = Cirujano(
                        matricula = 1017,
                        especialidad = "Pulmonar",
                        centro = "Hospital Central"
                    )
                    cirujano18 = Cirujano(
                        matricula = 1018,
                        especialidad = "General",
                        centro = "Hospital Norte"
                    )
                    cirujano19 = Cirujano(
                        matricula = 1019,
                        especialidad = "Traumatologo",
                        centro = "Hospital Este"
                    )
                    cirujano20 = Cirujano(
                        matricula = 1020,
                        especialidad = "Cardiovascular",
                        centro = "Hospital Oeste"
                    )
                    cirujano21 = Cirujano(
                        matricula = 1021,
                        especialidad = "Gastroenterologo",
                        centro = "Hospital Central"
                    )
                    cirujano22 = Cirujano(
                        matricula = 1022,
                        especialidad = "Plastico",
                        centro = "Hospital Norte"
                    )
                    cirujano23 = Cirujano(
                        matricula = 1023,
                        especialidad = "Pulmonar",
                        centro = "Hospital Este"
                    )
                    cirujano24 = Cirujano(
                        matricula = 1024,
                        especialidad = "General",
                        centro = "Hospital Oeste"
                    )
                    cirujano25 = Cirujano(
                        matricula = 1025,
                        especialidad = "Traumatologo",
                        centro = "Hospital Central"
                    )
                    Cirujanos = [cirujano1, cirujano2, cirujano3, cirujano4, cirujano5, cirujano6, cirujano7, cirujano8, cirujano9, cirujano10, 
                                cirujano11, cirujano12, cirujano13, cirujano14, cirujano15, cirujano16, cirujano17, cirujano18, cirujano19, cirujano20,
                                cirujano21, cirujano22, cirujano23, cirujano24, cirujano25]
                    for c in range(len(Cirujanos)):
                        pos = self.incucai.buscar_centro(Cirujanos[c].centro)
                        self.incucai.lista_c[pos].registrar_cirujano(Cirujanos[c])

                    vehiculo1 = Ambulancia(
                    velocidad = 95,
                    patente = 'AB123CD',
                    centro = "Hospital Central")
                    vehiculo2 = Helicoptero(
                        velocidad = 220,
                        patente = 'HE456FG',
                        centro = "Hospital Norte"
                    )
                    vehiculo3 = Avion(
                        velocidad = 650,
                        patente = 'AV789HI',
                        centro = "Hospital Este"
                    )
                    vehiculo4 = Ambulancia(
                        velocidad = 88,
                        patente = 'AM234JK',
                        centro = "Hospital Oeste"
                    )
                    vehiculo5 = Helicoptero(
                        velocidad = 180,
                        patente = 'HE567LM',
                        centro = "Hospital Central"
                    )
                    vehiculo6 = Ambulancia(
                        velocidad = 102,
                        patente = 'AB890NO',
                        centro = "Hospital Norte"
                    )
                    vehiculo7 = Avion(
                        velocidad = 720,
                        patente = 'AV345PQ',
                        centro = "Hospital Este"
                    )
                    vehiculo8 = Helicoptero(
                        velocidad = 195,
                        patente = 'HE678RS',
                        centro = "Hospital Oeste"
                    )
                    vehiculo9 = Ambulancia(
                        velocidad = 110,
                        patente = 'AM901TU',
                        centro = "Hospital Central"
                    )
                    vehiculo10 = Avion(
                        velocidad = 580,
                        patente = 'AV012VW',
                        centro = "Hospital Norte"
                    )
                    vehiculo11 = Helicoptero(
                        velocidad = 210,
                        patente = 'HE123XY',
                        centro = "Hospital Este"
                    )
                    vehiculo12 = Ambulancia(
                        velocidad = 92,
                        patente = 'AB456ZA',
                        centro = "Hospital Oeste"
                    )
                    vehiculo13 = Avion(
                        velocidad = 695,
                        patente = 'AV789BC',
                        centro = "Hospital Central"
                    )
                    vehiculo14 = Helicoptero(
                        velocidad = 165,
                        patente = 'HE234DE',
                        centro = "Hospital Norte"
                    )
                    vehiculo15 = Ambulancia(
                        velocidad = 105,
                        patente = 'AM567FG',
                        centro = "Hospital Este"
                    )
                    vehiculo16 = Avion(
                        velocidad = 740,
                        patente = 'AV890HI',
                        centro = "Hospital Oeste"
                    )
                    vehiculo17 = Helicoptero(
                        velocidad = 225,
                        patente = 'HE345JK',
                        centro = "Hospital Central"
                    )
                    vehiculo18 = Ambulancia(
                        velocidad = 87,
                        patente = 'AB678LM',
                        centro = "Hospital Norte"
                    )
                    vehiculo19 = Avion(
                        velocidad = 620,
                        patente = 'AV901NO',
                        centro = "Hospital Este"
                    )
                    vehiculo20 = Helicoptero(
                        velocidad = 190,
                        patente = 'HE012PQ',
                        centro = "Hospital Oeste"
                    )
                    vehiculo21 = Ambulancia(
                        velocidad = 98,
                        patente = 'AM345RS',
                        centro = "Hospital Central"
                    )
                    vehiculo22 = Avion(
                        velocidad = 680,
                        patente = 'AV456TU',
                        centro = "Hospital Norte"
                    )
                    vehiculo23 = Helicoptero(
                        velocidad = 175,
                        patente = 'HE789VW',
                        centro = "Hospital Este"
                    )
                    vehiculo24 = Ambulancia(
                        velocidad = 115,
                        patente = 'AB234XY',
                        centro = "Hospital Oeste"
                    )
                    vehiculo25 = Avion(
                        velocidad = 550,
                        patente = 'AV567ZA',
                        centro = "Hospital Central"
                    )
                    vehiculo26 = Helicoptero(
                        velocidad = 205,
                        patente = 'HE890BC',
                        centro = "Hospital Norte"
                    )
                    vehiculo27 = Ambulancia(
                        velocidad = 89,
                        patente = 'AM123DE',
                        centro = "Hospital Este"
                    )
                    vehiculo28 = Avion(
                        velocidad = 715,
                        patente = 'AV678FG',
                        centro = "Hospital Oeste"
                    )
                    vehiculo29 = Helicoptero(
                        velocidad = 185,
                        patente = 'HE901HI',
                        centro = "Hospital Central"
                    )
                    vehiculo30 = Ambulancia(
                        velocidad = 103,
                        patente = 'AB012JK',
                        centro = "Hospital Norte"
                    )
                    vehiculo31 = Avion(
                        velocidad = 635,
                        patente = 'AV345LM',
                        centro = "Hospital Este"
                    )
                    vehiculo32 = Helicoptero(
                        velocidad = 215,
                        patente = 'HE456NO',
                        centro = "Hospital Oeste"
                    )
                    vehiculo33 = Ambulancia(
                        velocidad = 94,
                        patente = 'AM789PQ',
                        centro = "Hospital Central"
                    )
                    vehiculo34 = Avion(
                        velocidad = 760,
                        patente = 'AV234RS',
                        centro = "Hospital Norte"
                    )
                    vehiculo35 = Helicoptero(
                        velocidad = 200,
                        patente = 'HE567TU',
                        centro = "Hospital Este"
                    )
                    vehiculo36 = Ambulancia(
                        velocidad = 108,
                        patente = 'AB890VW',
                        centro = "Hospital Oeste"
                    )
                    vehiculo37 = Avion(
                        velocidad = 590,
                        patente = 'AV123XY',
                        centro = "Hospital Central"
                    )
                    vehiculo38 = Helicoptero(
                        velocidad = 170,
                        patente = 'HE678ZA',
                        centro = "Hospital Norte"
                    )
                    vehiculo39 = Ambulancia(
                        velocidad = 112,
                        patente = 'AM901BC',
                        centro = "Hospital Este"
                    )
                    vehiculo40 = Avion(
                        velocidad = 705,
                        patente = 'AV012DE',
                        centro = "Hospital Oeste"
                    )
                    Vehiculos = [vehiculo1, vehiculo2, vehiculo3, vehiculo4, vehiculo5, vehiculo6, vehiculo7, vehiculo8, vehiculo9, vehiculo9, vehiculo10
                                , vehiculo11, vehiculo12, vehiculo13, vehiculo14, vehiculo15, vehiculo16, vehiculo17, vehiculo18, vehiculo19, vehiculo20, 
                                vehiculo21, vehiculo22, vehiculo23, vehiculo24, vehiculo25, vehiculo26, vehiculo27, vehiculo28, vehiculo29, vehiculo30, 
                                vehiculo31, vehiculo32, vehiculo33, vehiculo34, vehiculo35, vehiculo36, vehiculo37, vehiculo38, vehiculo39, vehiculo40]
                    for v in range(len(Vehiculos)):
                        pos = self.incucai.buscar_centro(Vehiculos[v].centro)
                        self.incucai.lista_c[pos].registrar_vehiculo(Vehiculos[v])

                    receptor1 = Receptor(
                        nombre="Carlos Martinez",
                        DNI=12345678,
                        nacimiento=15031985,
                        sexo="M",
                        telefono=1123456789,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Central",
                        organo="Corazon",
                        espera=20250120,
                        prioridad=1)
                    receptor2 = Receptor(
                        nombre="Maria Lopez",
                        DNI=35738921,
                        nacimiento=21042006,
                        sexo="F",
                        telefono=1133344455,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Central",
                        organo="Piel",
                        espera=20250325,
                        prioridad=1)
                    receptor3 = Receptor(
                        nombre="Pedro Gonzalez",
                        DNI=23456789,
                        nacimiento=8121978,
                        sexo="M",
                        telefono=1134567890,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Norte",
                        organo="Riñon",
                        espera=20250215,
                        prioridad=2)
                    receptor4 = Receptor(
                        nombre="Ana Rodriguez",
                        DNI=34567890,
                        nacimiento=12071992,
                        sexo="F",
                        telefono=1145678901,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Sur",
                        organo="Higado",
                        espera=20250110,
                        prioridad=1)
                    receptor5 = Receptor(
                        nombre="Luis Fernandez",
                        DNI=45678901,
                        nacimiento=3091988,
                        sexo="M",
                        telefono=1156789012,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Oeste",
                        organo="Pulmon",
                        espera=20250405,
                        prioridad=3)
                    receptor6 = Receptor(
                        nombre="Elena Sanchez",
                        DNI=56789012,
                        nacimiento=25111995,
                        sexo="F",
                        telefono=1167890123,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Este",
                        organo="Cornea",
                        espera=20250518,
                        prioridad=2)
                    receptor7 = Receptor(
                        nombre="Diego Torres",
                        DNI=67890123,
                        nacimiento=17061982,
                        sexo="M",
                        telefono=1178901234,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Central",
                        organo="Pancreas",
                        espera=20250228,
                        prioridad=1)
                    receptor8 = Receptor(
                        nombre="Carmen Ruiz",
                        DNI=78901234,
                        nacimiento=30051990,
                        sexo="F",
                        telefono=1189012345,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Norte",
                        organo="Intestino",
                        espera=20250620,
                        prioridad=3)
                    receptor9 = Receptor(
                        nombre="Roberto Silva",
                        DNI=89012345,
                        nacimiento=14021987,
                        sexo="M",
                        telefono=1190123456,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Sur",
                        organo="Hueso",
                        espera=20250315,
                        prioridad=2)
                    receptor10 = Receptor(
                        nombre="Patricia Morales",
                        DNI=90123456,
                        nacimiento=7101993,
                        sexo="F",
                        telefono=1101234567,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Oeste",
                        organo="Corazon",
                        espera=20250125,
                        prioridad=1)
                    receptor11 = Receptor(
                        nombre="Javier Castro",
                        DNI=11234567,
                        nacimiento=22081984,
                        sexo="M",
                        telefono=1112345678,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Este",
                        organo="Riñon",
                        espera=20250435,
                        prioridad=2)
                    receptor12 = Receptor(
                        nombre="Lucia Vargas",
                        DNI=22345678,
                        nacimiento=5041991,
                        sexo="F",
                        telefono=1123456781,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Central",
                        organo="Piel",
                        espera=20250710,
                        prioridad=3)
                    receptor13 = Receptor(
                        nombre="Gabriel Herrera",
                        DNI=33456789,
                        nacimiento=18121986,
                        sexo="M",
                        telefono=1134567892,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Norte",
                        organo="Higado",
                        espera=20250205,
                        prioridad=1)
                    receptor14 = Receptor(
                        nombre="Valentina Jimenez",
                        DNI=44567890,
                        nacimiento=11071989,
                        sexo="F",
                        telefono=1145678903,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Sur",
                        organo="Pulmon",
                        espera=20250820,
                        prioridad=2)
                    receptor15 = Receptor(
                        nombre="Francisco Mendez",
                        DNI=55678901,
                        nacimiento=28091994,
                        sexo="M",
                        telefono=1156789014,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Oeste",
                        organo="Cornea",
                        espera=20250530,
                        prioridad=3)
                    receptor16 = Receptor(
                        nombre="Sofia Romero",
                        DNI=66789012,
                        nacimiento=2011983,
                        sexo="F",
                        telefono=1167890125,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Este",
                        organo="Pancreas",
                        espera=20250140,
                        prioridad=1)
                    receptor17 = Receptor(
                        nombre="Mateo Delgado",
                        DNI=77890123,
                        nacimiento=16051992,
                        sexo="M",
                        telefono=1178901236,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Central",
                        organo="Intestino",
                        espera=20250925,
                        prioridad=2)
                    receptor18 = Receptor(
                        nombre="Isabella Ortega",
                        DNI=88901234,
                        nacimiento=9031988,
                        sexo="F",
                        telefono=1189012347,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Norte",
                        organo="Hueso",
                        espera=20250415,
                        prioridad=3)
                    receptor19 = Receptor(
                        nombre="Santiago Vega",
                        DNI=99012345,
                        nacimiento=23061985,
                        sexo="M",
                        telefono=1190123458,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Sur",
                        organo="Corazon",
                        espera=20250312,
                        prioridad=1)
                    receptor20 = Receptor(
                        nombre="Camila Flores",
                        DNI=10123456,
                        nacimiento=6101990,
                        sexo="F",
                        telefono=1101234569,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Oeste",
                        organo="Riñon",
                        espera=20250628,
                        prioridad=2)
                    receptor21 = Receptor(
                        nombre="Nicolas Aguilar",
                        DNI=21234567,
                        nacimiento=19021987,
                        sexo="M",
                        telefono=1112345679,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Este",
                        organo="Piel",
                        espera=20250745,
                        prioridad=3)
                    receptor22 = Receptor(
                        nombre="Martina Guerrero",
                        DNI=32345678,
                        nacimiento=13111993,
                        sexo="F",
                        telefono=1123456782,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Central",
                        organo="Higado",
                        espera=20250220,
                        prioridad=1)
                    receptor23 = Receptor(
                        nombre="Emilio Navarro",
                        DNI=43456789,
                        nacimiento=4081984,
                        sexo="M",
                        telefono=1134567893,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Norte",
                        organo="Pulmon",
                        espera=20250835,
                        prioridad=2)
                    receptor24 = Receptor(
                        nombre="Victoria Medina",
                        DNI=54567890,
                        nacimiento=27041991,
                        sexo="F",
                        telefono=1145678904,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Sur",
                        organo="Cornea",
                        espera=20250515,
                        prioridad=3)
                    receptor25 = Receptor(
                        nombre="Alejandro Peña",
                        DNI=65678901,
                        nacimiento=10121986,
                        sexo="M",
                        telefono=1156789015,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Oeste",
                        organo="Pancreas",
                        espera=20250125,
                        prioridad=1)
                    receptor26 = Receptor(
                        nombre="Renata Cruz",
                        DNI=76789012,
                        nacimiento=1071989,
                        sexo="F",
                        telefono=1167890126,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Este",
                        organo="Intestino",
                        espera=20250940,
                        prioridad=2)
                    receptor27 = Receptor(
                        nombre="Rodrigo Cabrera",
                        DNI=87890123,
                        nacimiento=24091994,
                        sexo="M",
                        telefono=1178901237,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Central",
                        organo="Hueso",
                        espera=20250610,
                        prioridad=3)
                    receptor28 = Receptor(
                        nombre="Julieta Rojas",
                        DNI=98901234,
                        nacimiento=15011983,
                        sexo="F",
                        telefono=1189012348,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Norte",
                        organo="Corazon",
                        espera=20250225,
                        prioridad=1)
                    receptor29 = Receptor(
                        nombre="Joaquin Ramos",
                        DNI=19012345,
                        nacimiento=8051992,
                        sexo="M",
                        telefono=1190123459,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Sur",
                        organo="Riñon",
                        espera=20250720,
                        prioridad=2)
                    receptor30 = Receptor(
                        nombre="Agustina Moreno",
                        DNI=20123456,
                        nacimiento=31031988,
                        sexo="F",
                        telefono=1101234570,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Oeste",
                        organo="Piel",
                        espera=20250445,
                        prioridad=3)
                    receptor31 = Receptor(
                        nombre="Thiago Blanco",
                        DNI=31234567,
                        nacimiento=12061985,
                        sexo="M",
                        telefono=1112345680,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Este",
                        organo="Higado",
                        espera=20250318,
                        prioridad=1)
                    receptor32 = Receptor(
                        nombre="Florencia Gil",
                        DNI=42345678,
                        nacimiento=26101990,
                        sexo="F",
                        telefono=1123456783,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Central",
                        organo="Pulmon",
                        espera=20250850,
                        prioridad=2)
                    receptor33 = Receptor(
                        nombre="Benjamin Luna",
                        DNI=53456789,
                        nacimiento=20021987,
                        sexo="M",
                        telefono=1134567894,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Norte",
                        organo="Cornea",
                        espera=20250530,
                        prioridad=3)
                    receptor34 = Receptor(
                        nombre="Micaela Torres",
                        DNI=64567890,
                        nacimiento=7111993,
                        sexo="F",
                        telefono=1145678905,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Sur",
                        organo="Pancreas",
                        espera=20250125,
                        prioridad=1)
                    receptor35 = Receptor(
                        nombre="Lautaro Sosa",
                        DNI=75678901,
                        nacimiento=29081984,
                        sexo="M",
                        telefono=1156789016,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Oeste",
                        organo="Intestino",
                        espera=20250635,
                        prioridad=2)
                    receptor36 = Receptor(
                        nombre="Guadalupe Paz",
                        DNI=86789012,
                        nacimiento=14041991,
                        sexo="F",
                        telefono=1167890127,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Este",
                        organo="Hueso",
                        espera=20250740,
                        prioridad=3)
                    receptor37 = Receptor(
                        nombre="Maximiliano Rey",
                        DNI=97890123,
                        nacimiento=3121986,
                        sexo="M",
                        telefono=1178901238,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Central",
                        organo="Corazon",
                        espera=20250415,
                        prioridad=1)
                    receptor38 = Receptor(
                        nombre="Antonella Diaz",
                        DNI=18901234,
                        nacimiento=18071989,
                        sexo="F",
                        telefono=1189012349,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Norte",
                        organo="Riñon",
                        espera=20250828,
                        prioridad=2)
                    receptor39 = Receptor(
                        nombre="Ignacio Castro",
                        DNI=29012345,
                        nacimiento=11091994,
                        sexo="M",
                        telefono=1190123460,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Sur",
                        organo="Piel",
                        espera=20250510,
                        prioridad=3)
                    receptor40 = Receptor(
                        nombre="Delfina Herrera",
                        DNI=30123456,
                        nacimiento=5011983,
                        sexo="F",
                        telefono=1101234571,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Oeste",
                        organo="Higado",
                        espera=20250220,
                        prioridad=1)
                    Receptores = [receptor1, receptor2, receptor3, receptor4, receptor5, receptor6, receptor7, receptor8, receptor9, receptor10, 
                                receptor11, receptor12, receptor13, receptor14, receptor15, receptor16, receptor17, receptor18, receptor19, receptor20,
                                receptor21, receptor22, receptor23, receptor24, receptor25, receptor26, receptor27, receptor28, receptor29, receptor30,
                                receptor31, receptor32, receptor33, receptor34, receptor35, receptor36, receptor37, receptor38, receptor39, receptor40]
                    for r in range(len(Receptores)):
                        self.incucai.registrar_paciente(Receptores[r])
                    
                    donante1 = Donante(
                        nombre="Camila Rodriguez",
                        DNI=39847251,
                        nacimiento=15081996,
                        sexo="F",
                        telefono=1134567890,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Norte",
                        organos=["Corazon", "Higado", "Cornea", "Pulmon"])
                    donante2 = Donante(
                        nombre="Sebastian Morales",
                        DNI=28456739,
                        nacimiento=22031988,
                        sexo="M",
                        telefono=1145678901,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Central",
                        organos=["Riñon", "Pancreas", "Piel"])
                    donante3 = Donante(
                        nombre="Valentina Castro",
                        DNI=41592837,
                        nacimiento=7121992,
                        sexo="F",
                        telefono=1156789012,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Sur",
                        organos=["Higado", "Cornea", "Hueso", "Intestino"])
                    donante4 = Donante(
                        nombre="Matias Lopez",
                        DNI=37284659,
                        nacimiento=19051985,
                        sexo="M",
                        telefono=1167890123,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Oeste",
                        organos=["Corazon", "Pulmon", "Riñon"])
                    donante5 = Donante(
                        nombre="Agustina Silva",
                        DNI=52847361,
                        nacimiento=3091994,
                        sexo="F",
                        telefono=1178901234,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Este",
                        organos=["Pancreas", "Piel", "Cornea", "Hueso", "Intestino"])
                    donante6 = Donante(
                        nombre="Nicolas Fernandez",
                        DNI=46183729,
                        nacimiento=14021990,
                        sexo="M",
                        telefono=1189012345,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Central",
                        organos=["Higado", "Pulmon"]
                    )
                    donante7 = Donante(
                        nombre="Sofia Martinez",
                        DNI=63748291,
                        nacimiento=28111987,
                        sexo="F",
                        telefono=1190123456,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Norte",
                        organos=["Corazon", "Riñon", "Cornea", "Piel", "Hueso"]
                    )
                    donante8 = Donante(
                        nombre="Diego Romero",
                        DNI=18374629,
                        nacimiento=11061993,
                        sexo="M",
                        telefono=1101234567,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Sur",
                        organos=["Pancreas", "Intestino", "Pulmon"]
                    )
                    donante9 = Donante(
                        nombre="Micaela Torres",
                        DNI=74829163,
                        nacimiento=26071989,
                        sexo="F",
                        telefono=1112345678,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Oeste",
                        organos=["Higado", "Cornea", "Hueso"]
                    )
                    donante10 = Donante(
                        nombre="Facundo Gonzalez",
                        DNI=59384726,
                        nacimiento=4101991,
                        sexo="M",
                        telefono=1123456789,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Este",
                        organos=["Corazon", "Pulmon", "Riñon", "Piel", "Intestino"]
                    )
                    donante11 = Donante(
                        nombre="Julieta Herrera",
                        DNI=38472951,
                        nacimiento=17041986,
                        sexo="F",
                        telefono=1134567890,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Central",
                        organos=["Pancreas", "Cornea"]
                    )
                    donante12 = Donante(
                        nombre="Tomas Sanchez",
                        DNI=62948371,
                        nacimiento=1121984,
                        sexo="M",
                        telefono=1145678901,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Norte",
                        organos=["Higado", "Hueso", "Intestino", "Piel"]
                    )
                    donante13 = Donante(
                        nombre="Florencia Ruiz",
                        DNI=47392856,
                        nacimiento=23081995,
                        sexo="F",
                        telefono=1156789012,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Sur",
                        organos=["Corazon", "Riñon", "Pulmon"]
                    )
                    donante14 = Donante(
                        nombre="Ignacio Vargas",
                        DNI=85739246,
                        nacimiento=9031988,
                        sexo="M",
                        telefono=1167890123,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Oeste",
                        organos=["Pancreas", "Cornea", "Hueso", "Intestino"]
                    )
                    donante15 = Donante(
                        nombre="Lucia Medina",
                        DNI=73946281,
                        nacimiento=15071992,
                        sexo="F",
                        telefono=1178901234,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Este",
                        organos=["Higado", "Piel"]
                    )
                    donante16 = Donante(
                        nombre="Lautaro Diaz",
                        DNI=29573864,
                        nacimiento=2051990,
                        sexo="M",
                        telefono=1189012345,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Central",
                        organos=["Corazon", "Pulmon", "Riñon", "Cornea", "Hueso"]
                    )
                    donante17 = Donante(
                        nombre="Martina Peña",
                        DNI=64827391,
                        nacimiento=20091987,
                        sexo="F",
                        telefono=1190123456,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Norte",
                        organos=["Pancreas", "Intestino", "Piel"]
                    )
                    donante18 = Donante(
                        nombre="Joaquin Gil",
                        DNI=51748329,
                        nacimiento=8111994,
                        sexo="M",
                        telefono=1101234567,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Sur",
                        organos=["Higado", "Cornea"]
                    )
                    donante19 = Donante(
                        nombre="Antonella Blanco",
                        DNI=73829461,
                        nacimiento=13021989,
                        sexo="F",
                        telefono=1112345678,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Oeste",
                        organos=["Corazon", "Hueso", "Intestino", "Pulmon"]
                    )
                    donante20 = Donante(
                        nombre="Emiliano Cruz",
                        DNI=46293851,
                        nacimiento=25061991,
                        sexo="M",
                        telefono=1123456789,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Este",
                        organos=["Riñon", "Piel", "Cornea"]
                    )
                    donante21 = Donante(
                        nombre="Catalina Vega",
                        DNI=82749163,
                        nacimiento=7041986,
                        sexo="F",
                        telefono=1134567890,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Central",
                        organos=["Pancreas", "Higado", "Hueso", "Intestino"]
                    )
                    donante22 = Donante(
                        nombre="Alejandro Moreno",
                        DNI=39572846,
                        nacimiento=18101993,
                        sexo="M",
                        telefono=1145678901,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Norte",
                        organos=["Corazon", "Pulmon"]
                    )
                    donante23 = Donante(
                        nombre="Renata Delgado",
                        DNI=74638291,
                        nacimiento=30071988,
                        sexo="F",
                        telefono=1156789012,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Sur",
                        organos=["Riñon", "Cornea", "Piel"]
                    )
                    donante24 = Donante(
                        nombre="Rodrigo Castro",
                        DNI=58394726,
                        nacimiento=12121990,
                        sexo="M",
                        telefono=1167890123,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Oeste",
                        organos=["Higado", "Pancreas", "Hueso", "Intestino"]
                    )
                    donante25 = Donante(
                        nombre="Delfina Lopez",
                        DNI=67249381,
                        nacimiento=5081985,
                        sexo="F",
                        telefono=1178901234,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Este",
                        organos=["Corazon", "Cornea"]
                    )
                    donante26 = Donante(
                        nombre="Thiago Ramos",
                        DNI=42857396,
                        nacimiento=21031992,
                        sexo="M",
                        telefono=1189012345,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Central",
                        organos=["Pulmon", "Riñon", "Piel", "Hueso"]
                    )
                    donante27 = Donante(
                        nombre="Guadalupe Silva",
                        DNI=85697342,
                        nacimiento=16051987,
                        sexo="F",
                        telefono=1190123456,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Norte",
                        organos=["Higado", "Pancreas", "Intestino"]
                    )
                    donante28 = Donante(
                        nombre="Benjamin Torres",
                        DNI=73428659,
                        nacimiento=3091994,
                        sexo="M",
                        telefono=1101234567,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Sur",
                        organos=["Corazon", "Cornea", "Hueso"]
                    )
                    donante29 = Donante(
                        nombre="Isabella Fernandez",
                        DNI=59473826,
                        nacimiento=27111989,
                        sexo="F",
                        telefono=1112345678,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Oeste",
                        organos=["Pulmon", "Riñon", "Piel"]
                    )
                    donante30 = Donante(
                        nombre="Maximiliano Rojas",
                        DNI=48362957,
                        nacimiento=10021991,
                        sexo="M",
                        telefono=1123456789,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Este",
                        organos=["Higado", "Pancreas", "Cornea", "Intestino"]
                    )
                    donante31 = Donante(
                        nombre="Constanza Herrera",
                        DNI=76584329,
                        nacimiento=24061988,
                        sexo="F",
                        telefono=1134567890,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Central",
                        organos=["Corazon", "Hueso"]
                    )
                    donante32 = Donante(
                        nombre="Franco Mendez",
                        DNI=63972485,
                        nacimiento=6121986,
                        sexo="M",
                        telefono=1145678901,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Norte",
                        organos=["Pulmon", "Riñon", "Piel", "Cornea", "Intestino"]
                    )
                    donante33 = Donante(
                        nombre="Milagros Ortega",
                        DNI=52847639,
                        nacimiento=19081993,
                        sexo="F",
                        telefono=1156789012,
                        tipo_de_sangre="A-",
                        centro_de_salud="Hospital Sur",
                        organos=["Higado", "Pancreas"]
                    )
                    donante34 = Donante(
                        nombre="Gael Navarro",
                        DNI=47639258,
                        nacimiento=11041990,
                        sexo="M",
                        telefono=1167890123,
                        tipo_de_sangre="O+",
                        centro_de_salud="Hospital Oeste",
                        organos=["Corazon", "Cornea", "Hueso", "Intestino"]
                    )
                    donante35 = Donante(
                        nombre="Pilar Guerrero",
                        DNI=84729356,
                        nacimiento=2101987,
                        sexo="F",
                        telefono=1178901234,
                        tipo_de_sangre="B-",
                        centro_de_salud="Hospital Este",
                        organos=["Pulmon", "Piel"]
                    )
                    donante36 = Donante(
                        nombre="Santiago Aguilar",
                        DNI=69372845,
                        nacimiento=28071995,
                        sexo="M",
                        telefono=1189012345,
                        tipo_de_sangre="AB+",
                        centro_de_salud="Hospital Central",
                        organos=["Riñon", "Higado", "Cornea"]
                    )
                    donante37 = Donante(
                        nombre="Esperanza Cabrera",
                        DNI=53968472,
                        nacimiento=14031988,
                        sexo="F",
                        telefono=1190123456,
                        tipo_de_sangre="A+",
                        centro_de_salud="Hospital Norte",
                        organos=["Pancreas", "Hueso", "Intestino", "Piel"]
                    )
                    donante38 = Donante(
                        nombre="Octavio Paz",
                        DNI=72856394,
                        nacimiento=8091992,
                        sexo="M",
                        telefono=1101234567,
                        tipo_de_sangre="O-",
                        centro_de_salud="Hospital Sur",
                        organos=["Corazon", "Pulmon"]
                    )
                    donante39 = Donante(
                        nombre="Alma Rey",
                        DNI=46285739,
                        nacimiento=22051989,
                        sexo="F",
                        telefono=1112345678,
                        tipo_de_sangre="B+",
                        centro_de_salud="Hospital Oeste",
                        organos=["Higado", "Cornea", "Hueso"]
                    )
                    donante40 = Donante(
                        nombre="Emilio Jimenez",
                        DNI=85639472,
                        nacimiento=17121984,
                        sexo="M",
                        telefono=1123456789,
                        tipo_de_sangre="AB-",
                        centro_de_salud="Hospital Este",
                        organos=["Riñon", "Pancreas", "Piel", "Intestino"]
                    )
                    Donantes = [donante1, donante2, donante3, donante4, donante5, donante6, donante7, donante8, donante9, donante10,
                                donante11, donante12, donante13, donante14, donante15, donante16, donante17, donante18, donante19, donante20,
                                donante21, donante22, donante23, donante24, donante25, donante26, donante27, donante28, donante29, donante30,
                                donante31, donante32, donante33, donante34, donante35, donante36, donante37, donante38, donante39, donante40]
                    for d in range(len(Donantes)):
                        self.incucai.registrar_paciente(Donantes[d])

                elif(eleccion == "6"):
                    self.incucai.match_por_llamado_del_menu()

                elif(eleccion == "7"):
                    self.incucai.print_pantalla()

                elif(eleccion == "8"):
                    centro = input('Ingrese nombre del centro al que pertenece el vehiculo: ') 
                    aux = self.incucai.buscar_centro(centro)

                    if aux == -1:
                        print("El centro no se encuentra registrado aun.")
                        continue

                    while True:
                        patente = input('Ingrese la patente del vehiculo: ').upper()
                        if not patente.isalnum():
                            print('Ingrese una respuesta válida.')
                        else:
                            break

                    encontrado = False
                    for vehiculo in self.incucai.lista_c[aux].vehiculos:
                        if patente == vehiculo.patente:
                            encontrado = True
                            try:
                                vehiculo.print_registro()
                            except Exception as e:
                                print("Error al imprimir el registro:", e)
                            break

                    if not encontrado:
                        print("El vehículo no se encuentra registrado.")

                elif (eleccion == "0"):
                    return

                else:
                    print("No se registro su respuesta, porfavor reingrese nuevamente una opcion.")
