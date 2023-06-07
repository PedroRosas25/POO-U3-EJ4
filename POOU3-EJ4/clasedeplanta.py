from claseempleado import Empleado
class DePlanta(Empleado):
    __sueldo=float
    __antiguedad=int

    def __init__(self,dni,nombre,direccion,telefono,sueldo,antiguedad):
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldo=sueldo
        self.__antiguedad=antiguedad

    def getSueldo(self):
        return self.__sueldo
    def getAntiguedad(self):
        return self.__antiguedad   

    def getSueldo(self):
        sueldo=float(self.__sueldo+float(((self.__sueldo/100)*self.__antiguedad)))
        return sueldo 
    
    def __str__(self):
        return 'DNI:{} Nomre:{} Direccion:{} Tlelefono:{} Sueldo:{} Antiguedad:{}'.format(self.getDni(),self.getNombre(),self.getDireccion(),self.getTelefono(),self.__sueldo,self.__antiguedad)