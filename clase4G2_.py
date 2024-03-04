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
    def verificarCedulaUnica(self, cedula):
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                return False  
        return True 
    
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self,cedula):
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                bandera = True
            else:
                bandera = False
        
        if bandera == True:
            print("-------------------------------")
            print("Nombre: " + paciente.verNombre())
            print("Cedula: " + str(paciente.verCedula()))
            print("Genero: " + paciente.verGenero())
            print("Servicio: " + paciente.verServicio())
                
        else:
            print("------------------------------------------")
            print("El paciente no se encuentra en el sistema.")
            print("------------------------------------------")
            
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
            
            if sis.verificarCedulaUnica(cedula):
            
                
                # 2. Se crea un objeto Paciente
                p = Paciente() 
                # Como el paciente está vacío, se le ingresan los datos
                p.asignarNombre(input("Ingrese el nombre: ")) 
                p.asignarCedula(cedula) 
                p.asignarGenero(input("Ingrese el genero: ")) 
                p.asignarServicio(input("Ingrese servicio: ")) 
                # 3. Se almacena en la lista que está dentro de la clase Sistema
                r = sis.ingresarPaciente(p)             
                if r:
                    print("------------------")
                    print("Paciente ingresado") 
                    print("------------------")
                    
                else:
                    print("------------")
                    print("No ingresado") 
                    print("------------")
                    
            else:    
                print("--------------------------------------------")
                print("Ya existe un paciente con esa cedula".upper())
                print("--------------------------------------------")
                    
        elif opcion == 2:
            cedula = int(input("Ingrese la cedula a buscar: "))
            datos_pac = sis.verDatosPaciente(cedula)
            print(datos_pac)
                    
        elif opcion == 3:
            sis.verNumeroPacientes()
            
        elif opcion == 4:
            print("--------------")
            print("Saliendo......")
            print("--------------")
            break
        
        else:
            print("---------------------------")
            print("Ingresó una opción inválida")
            print("---------------------------")
            break 

# Aca el python descubre cual es la función principal
if __name__ == "__main__":
    main() 
