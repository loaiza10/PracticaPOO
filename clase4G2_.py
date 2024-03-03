#se crea la clase paciente
class Paciente:
    # se inicializa la clase con el init o el constructor
    def __init__(self):
      self.__nombre = "" #se crea variable de nombre privada
      self.__cedula = 0  #se crea variable de cedula privada
      self.__genero = "" #se crea variable de genero privada
      self.__servicio = "" #se crea variable de servicio privada
      
    #metodos get
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    #metodos set
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

#se crea la clase sistema que es donde se almacenan los pacientes
class Sistema:
    # se inicializa la clase con el metodo init o constructor
    def __init__(self):
      self.__lista_pacientes = [] #se crea lista para pacientes privada
    #   self.__lista_pacientes = {}
      self.__numero_pacientes = len(self.__lista_pacientes) #numero de pacientes privada
      
    #se crean funciones propias del sistema
    def verificarPaciente(self,cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False
    
    def ingresarPaciente(self):
        # 1- solicito los datos por teclado
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))    
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")
        # 2- creo el objeto Paciente y le asigno los datos
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)        
        # 3- guardo el Paciente en  la lista        
        self.__lista_pacientes.append(p)
        # self.__lista_pacientes[p.verCedula()] = p
        # 4- actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self, cedula):
        cedula = int(input("Ingrese la cedula a buscar: "))
        
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
                

def main():
    sis = Sistema() 
    while True:
        opcion = int(input("""Seleccione una opción 
              1. Ingresar paciente
              2. Buscar paciente
              3. Ver numero de pacientes
              4. Salir\n"""))
        
        if opcion == 1:
            # Ingreso pacientes
            print("A continuación se solicitarán los datos...") 
            # 1. Solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            
            else:    
                # 2. Se crea un objeto Paciente
                p = Paciente() 
                # Como el paciente está vacío, se le ingresan los datos
                p.asignarNombre(input("Ingrese el nombre: ")) 
                p.asignarCedula(cedula) 
                p.asignarGenero(input("Ingrese el genero: ")) 
                p.asignarServicio(input("Ingrese servicio: ")) 
                # 3. Se almacena en la lista que está dentro de la clase Sistema
                r = sis.ingresarPaciente(cedula)             
                if r:
                    print("------------------")
                    print("Paciente ingresado") 
                    print("------------------")
                    
                else:
                    print("------------")
                    print("No ingresado") 
                    print("------------")
                    
        elif opcion == 2:
            # 1. Solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: ")) 
            # Le pido al sistema que me devuelva en la variable p al paciente que tenga
            # la cedula c en la lista
            p = sis.verDatosPaciente(c) 
            # 2. Si encuentro al paciente, imprimo los datos
            if p is not None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            
            else:
                print("------------------------------------")
                print("No existe un paciente con esa cedula") 
                print("------------------------------------")
                
        elif opcion == 3:
            print("----------------------------------------------------------------")
            print(f'El número de pacientes ingresados es {sis.verNumeroPacientes()}')
            print("----------------------------------------------------------------")
            
        elif opcion == 4:
            print("--------------")
            print("Saliendo......")
            print("--------------")
            continue 
        
        else:
            break 

# Aca el python descubre cual es la función principal
if __name__ == "__main__":
    main() 
