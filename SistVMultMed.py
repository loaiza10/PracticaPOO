from datetime import datetime,date
#funciones de validación
def validar_enteros(msj):
    try:
        data = int(input(msj))
        return data
    except:
        print("--------------------------------------------------")
        print("Ingrese solo números enteros. Inténtelo nuevamente")
        print("--------------------------------------------------")
        return validar_enteros(msj)
    
def validar_flotantes(msj):
    try:
        data = float(input(msj))
        return data
    except:
        print("----------------------------------------------------")
        print("Ingrese solo números decimales. Inténtelo nuevamente")
        print("----------------------------------------------------")
        return validar_flotantes(msj)
    
import re
r2 = r'^[A-Za-z-ñÑ-áÁéÉíÍóÓúÚ  ]+$'
patron = re.compile(r2)

def validar_letras(msj):
    
    data = input(msj)
    if patron.match(data):
        return data
    else:
        print("----------------------------------------------")
        print("Debe ingresar solo letras y espacios en blanco")
        print("----------------------------------------------")
        return validar_letras(msj)

def validar_date(msj):
    while True:
        print("---------------------------------------------------------------")
        print("A continuación ingrese la fecha en la que se realizó el estudio")
        print("Ingrese el día: ")
        dia = validar_enteros(msj)

        print("Ingrese el mes: ")
        mes = validar_enteros(msj)

        print("Ingresar el año: ")
        año = validar_enteros(msj)

        try:
            fecha = datetime(año, mes, dia)
            break
        except ValueError:
            print("-------------------------------------------")
            print("Fecha incorrecta, ingrese la fecha de nuevo")
            print("-------------------------------------------")

    print("Fecha: ", fecha.strftime("%d/%m/%Y"))
    return str(fecha)

class Medicamento:
    #metodo init o constructor de la clase
    def __init__(self):
        self.__nombre = "" #se crea variable de nombre y es privada
        self.__dosis = 0 #se crea variable de dosis y es privada
    
    #metodos get
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    #metodos set
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    #metodo init para inicializar la clase
    def __init__(self):
        self.__nombre= " " # se crea variable nombre y es privada
        self.__historia = 0 # se crea variable historia y es privada
        self.__tipo = " " # se crea variable tipo y es privada
        self.__peso = " " # se crea variable peso y es privada
        self.__fecha_ingreso = " " #se crea variable fecha de ingreso y es privada
        self.__lista_medicamentos = [] # se crea una lista de medicamentos que es el elemento contenedor donde van a estar los medicamentos y es privada
    
    #metodos get
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
    
    #metodos set
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarHistoria(self,nh):
        self.__historia = nh
    def asignarTipo(self,t):
        self.__tipo = t
    def asignarPeso(self,p):
        self.__peso = p
    def asignarFecha(self,f):
        self.__fecha_ingreso = f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    # se inicializa la clase con el metodo init
    def __init__(self):
        self.__lista_caninos = {} # se crea elemento contenedor de tipo diccionario para caninos y es privado
        self.__lista_felinos = {} # se crea elemento contenedor de tipo diccionario para felinos y es privado
    
    # se crean funciones propias del sistema
    def verificarExiste(self, historia):
        for m in self.__lista_felinos.values():
            if historia == m.verHistoria():
                return True

        for m in self.__lista_caninos.values():
            if historia == m.verHistoria():
                return True
            
        return False
    
    def verNumeroMascotas(self):
        cantidad_de_felinos = 0
        cantidad_de_caninos = 0
        
        cantidad_de_felinos = len(self.__lista_felinos)
        cantidad_de_caninos = len(self.__lista_caninos)
        
        a = cantidad_de_caninos + cantidad_de_felinos
        return a  
    
    def ingresarMascota(self,mascota, historia):
        if mascota.verTipo() == "felino":
            self.__lista_felinos[historia] = mascota
            
        elif mascota.verTipo() == "canino":
            self.__lista_caninos[historia] = mascota
            
        else: 
            print("---------------------------")
            print("Ingresó una opción inválida") 
            print("---------------------------")
   
    def verFechaIngreso(self,historia):
        for mascota_actual in self.__lista_felinos:
            if historia == mascota_actual:
                return self.__lista_felinos[mascota_actual].verFecha()
    
        for mascota_actual in self.__lista_caninos:
            if historia == mascota_actual:
                return self.__lista_caninos[mascota_actual].verFecha()
    
        return None

    def verMedicamento(self,historia):
        for mascota_actual in self.__lista_felinos:
            if historia == mascota_actual:
                return self.__lista_felinos[mascota_actual].verLista_Medicamentos()

        for mascota_actual in self.__lista_caninos:
            if historia == mascota_actual:
                return self.__lista_caninos[mascota_actual].verLista_Medicamentos()
    
    def eliminarMascota(self, historia):
        if historia in self.__lista_felinos:
            mascota_eliminada = self.__lista_felinos.pop(historia)
            return mascota_eliminada
        
        elif historia in self.__lista_caninos:
            mascota_eliminada = self.__lista_caninos.pop(historia)
            return mascota_eliminada
        
        else:
            return "No encontrado"
        
    def eliminarMedicamento(self, historia):
        for mascota in self.__lista_felinos.values():
            if historia == mascota.verHistoria():
                mascota.asignarLista_Medicamentos([])  
                return True  # Eliminado con éxito

        for mascota in self.__lista_caninos.values():
            if historia == mascota.verHistoria():
                mascota.asignarLista_Medicamentos([])  
                return True  # Eliminado con éxito
        

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu = validar_enteros('''Ingrese una opción: 
                       1. Ingresar una mascota
                       2. Ver fecha de ingreso
                       3. Ver número de mascotas en el servicio
                       4. Ver medicamentos
                       5. Eliminar mascota 
                       6. Eliminar medicamento
                       7. Salir
                       ''' )
        
        if menu == 1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("------------------")
                print("No hay espacio ...") 
                print("------------------")
                continue
            
            historia = validar_enteros("Ingrese la historia clínica de la mascota: ")
            
            #   verificacion = servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre = validar_letras("Ingrese el nombre de la mascota: ")
                tipo = validar_letras("Ingrese el tipo de mascota (felino o canino): ")
                peso = validar_flotantes("Ingrese el peso de la mascota: ")
                fecha = validar_date("Ingrese la fecha de ingreso: ")
                nm = validar_enteros("Ingrese cantidad de medicamentos: ")
                lista_med = []

                
                for i in range(0, nm):
                    nombre_medicamentos = validar_letras("Ingrese el nombre del medicamento: ")

                    med_repetido = False
                    for medicamento in lista_med: 
                        if nombre_medicamentos == medicamento.verNombre():
                            print("------------------------------------------------------------------")
                            print("No se puede recetar el medicamento ya que ya se encuentra recetado")
                            print("------------------------------------------------------------------")
                            med_repetido = True
                            break

                    if med_repetido:
                        continue

                    dosis = validar_enteros("Ingrese la dosis: ")
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas, historia)
                
                print("-----------------------------")
                print("Mascota guardada exitosamente")
                print("-----------------------------")
            
            else:
                print("------------------------------------------------------")
                print("Ya existe la mascota con el número de historia clínica")
                print("------------------------------------------------------")

        elif menu == 2: # Ver fecha de ingreso
            historia = validar_enteros("Ingrese la historia clínica de la mascota: ")
            fecha = servicio_hospitalario.verFechaIngreso(historia)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("----------------------------------------------")
                print("La fecha de ingreso de la mascota es: " + fecha)
                print("----------------------------------------------")
                
            else:
                print("-------------------------------------------------------------------------------")
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                print("-------------------------------------------------------------------------------")
        
        elif menu == 3: # Ver número de mascotas en el servicio 
            numero = servicio_hospitalario.verNumeroMascotas()
            print("-------------------------------------------------------")
            print("El número de pacientes en el sistema es: " + str(numero))
            print("-------------------------------------------------------")
            
        elif menu == 4: # Ver medicamentos que se están administrando
            historia = validar_enteros("Ingrese la historia clínica de la mascota: ")
            medicamento = servicio_hospitalario.verMedicamento(historia) 
            
            if medicamento != None: 
                print("------------------------------------")
                print("Los medicamentos suministrados son: ")
                print("------------------------------------")
                
                for m in medicamento:   
                    print("--------------------")
                    print(f"\n- {m.verNombre()}")
                    print("--------------------")
                    
            else:
                print("-------------------------------------------------------------------------------")
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                print("-------------------------------------------------------------------------------")
                
        elif menu == 5: # Eliminar mascota
            historia = validar_enteros("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMascota(historia) 

            if resultado_operacion != "No encontrado":
                print("---------------------------------------")
                print("Mascota eliminada del sistema con éxito")
                print("---------------------------------------")
            
            else:
                print("-----------------------------------")
                print("No se ha podido eliminar la mascota")
                print("-----------------------------------")
        
        elif menu == 6: #eliminar medicamento
            historia = validar_enteros("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMedicamento(historia) 
            
            if resultado_operacion == True:
                print("---------------------------------------")
                print("Medicamento eliminada del sistema con exito")
                print("---------------------------------------")
                
            else:
                print("-----------------------------------")
                print("No se ha podido eliminar el medicamento")
                print("-----------------------------------")
        
        elif menu == 7: #salir
            
            print("-------------------------------------------------------------")
            print("Usted ha salido del sistema de servicio de hospitalización...")
            print("-------------------------------------------------------------")
            break
        
        else:
            
            print("-----------------------------------------------------------")
            print("Usted ingresó una opción no válida, intentelo nuevamente...")
            print("-----------------------------------------------------------")
            
if __name__=='__main__':
    main()







            

                

