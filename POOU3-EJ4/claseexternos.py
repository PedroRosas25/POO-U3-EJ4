from claseempleado import Empleado
class Externo(Empleado):
    __tarea=str
    __fechainicio=str
    __fechafin=str
    __montoviatico=float
    __costoobra=float
    __montoseguro=float

    def __init__(self,dni,nombre,direccion,telefono,tarea,fechainicio,fechafin,montoviatico,costoobra,montoseguro):
        super().__init__(dni,nombre,direccion,telefono)
        self.__tarea=tarea
        self.__fechainicio=fechainicio
        self.__fechafin=fechafin
        self.__montoviatico=montoviatico
        self.__costoobra=costoobra
        self.__montoseguro=montoseguro

    def getTarea(self):
        return self.__tarea
    def getFechainicio(self):
        return self.__fechainicio
    def getFechafin(self):
        return self.__fechafin
    def getMontoviatico(self):
        return self.__montoviatico
    def getCostoobra(self):
        return self.__costoobra  
    def getMontoseguro(self):
        return self.__montoseguro  
    
    def getSueldo(self):
        sueldo=float(self.__costoobra-self.__montoviatico-self.__montoseguro)
        return sueldo
    
    def __str__(self):
        return 'DNI:{} Nombre:{} Direccion:{} Telefono:{} Tarea:{} Fechainicio:{} Fechafin:{} Montoviatico:{} Costoobra:{} Montoseguro:{}'.format(self.getDni(),self.getNombre(),self.getDireccion(),self.getTelefono(),self.__tarea,self.__fechainicio,self.__fechafin,self.__montoviatico,self.__costoobra,self.__montoseguro)