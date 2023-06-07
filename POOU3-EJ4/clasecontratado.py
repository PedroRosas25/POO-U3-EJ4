from claseempleado import Empleado

class Contratado(Empleado):
    __fechainicio=str
    __fechafin=str
    __horas=int
    __valorxhora=500

    def __init__(self,dni,nombre,direccion,telefono,fechainicio,fechafin,horas,valorxhora):
        super().__init__(dni,nombre,direccion,telefono)
        self.__fechainicio=fechainicio
        self.__fechafin=fechafin
        self.__horas=horas
        self.__valorxhora=valorxhora

    def getFechainicio(self):
        return self.__fechainicio
    def getFechafin(self):
        return self.__fechafin
    def getHoras(self):
        return self.__horas
    def getValorxhora(self):
        return self.__valorxhora
    def cambiarhoras(self,horax):
        self.__horas=horax
    
    def getSueldo(self):
        sueldo=float(self.__horas*self.__valorxhora)
        return sueldo

    def __str__(self):
        return 'DNI:{} Nombre:{} Direccion:{} Telefono:{} Fechainicio:{} Fechafin:{} Horas:{} Valorxhora:{}'.format(self.getDni(),self.getNombre(),self.getDireccion(),self.getTelefono(),self.__fechainicio,self.__fechafin,self.__horas,self.__valorxhora) 
        