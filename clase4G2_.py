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
    
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, cedula):
        pacientes_encontrados = []

        for paciente in self.__lista_pacientes:
            if str(cedula).isdigit():
            # If cedula is a number, search by cedula
                if int(cedula) == paciente.verCedula():
                    pacientes_encontrados.append(paciente)
            else:
            # If cedula is not a number, search by name
                if paciente.verNombre().lower().startswith(cedula.lower()):
                    pacientes_encontrados.append(paciente)

        return pacientes_encontrados

            
    def verNumeroPacientes(self):
        print("----------------------------")
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 
        print("----------------------------")

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
            ced_or_name = input("Ingrese la cedula o nombre a buscar: ")
    
            # Le pido al sistema que me devuelva en la variable pacientes_encontrados
            # a los pacientes que coinciden con la cedula o nombre proporcionados
            pacientes_encontrados = sis.verDatosPaciente(ced_or_name)

            # 2. Si encuentro pacientes, imprimo los datos
            if pacientes_encontrados:
                print("-----------------------------------")
                print("Datos de paciente(s) encontrado(s):")
        
            for paciente in pacientes_encontrados:
                print("Nombre:", paciente.verNombre())
                print("Cedula:", paciente.verCedula())
                print("Genero:", paciente.verGenero())
                print("Servicio:", paciente.verServicio())
                print("---------------------------------")
                
            else:
                print("---------------------------------------------")
                print("No existe un paciente con esa cedula o nombre")
                print("---------------------------------------------")

        elif opcion == 3:
            sis.verNumeroPacientes()
            
        elif opcion == 4:
            print("--------------")
            print("Saliendo......")
            print("--------------")
            break
        
        else:
            break 

# Aca el python descubre cual es la función principal
if __name__ == "__main__":
    main() 
