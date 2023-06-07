from claseempleado import Empleado
from clasecontratado import Contratado
from clasedeplanta import DePlanta
from claseexternos import Externo
import numpy as np
import csv

class ManejadorEmpleado:
    __listaempleados=[]

    def __init__(self,dimension):
        self.__len=dimension
        self.__incremento=1
        self.__cant=0
        self.__listaempleados=np.empty(self.__len,dtype=Empleado)

    def cargararreglo(self,empleado):
        if self.__len==self.__cant:
            self.__len+=self.__incremento
            self.__listaempleados.resize(self.__len)
        self.__listaempleados[self.__cant]=empleado
        self.__cant+=1        

    def cargarempleados(self):
        archivo=open('contratados.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            dni=int(input('Ingrese dni de la persona '))
            nombre=str(input('Ingrese nombre de la persona '))
            direccion=str(input('Ingrese direccion de la persona '))
            telefono=str(input('Ingrese telefono de la persona '))
            fechainicio=fila[0]
            fechafin=fila[1]
            horas=int(fila[2])
            valorxhora=int(fila[3])
            uncontratado=Contratado(dni,nombre,direccion,telefono,fechainicio,fechafin,horas,valorxhora)
            self.cargararreglo(uncontratado)
        archivo=open('externos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            dni=int(input('Ingrese dni de la persona '))
            nombre=str(input('Ingrese nombre de la persona '))
            direccion=str(input('Ingrese direccion de la persona '))
            telefono=str(input('Ingrese telefono de la persona '))
            tarea=str(fila[0])
            fechainicio=str(fila[1])
            fechafin=str(fila[2])
            montoviatico=float(fila[3])
            costoobra=float(fila[4])
            montoseguro=float(fila[5])
            unexterno=Externo(dni,nombre,direccion,telefono,tarea,fechainicio,fechafin,montoviatico,costoobra,montoseguro)
            self.cargararreglo(unexterno)
        archivo=open('planta.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            dni=int(input('Ingrese dni de la persona '))
            nombre=str(input('Ingrese nombre de la persona '))
            direccion=str(input('Ingrese direccion de la persona '))
            telefono=str(input('Ingrese telefono de la persona '))
            sueldo=float(fila[0])
            antiguedad=int(fila[1])
            unplanta=DePlanta(dni,nombre,direccion,telefono,sueldo,antiguedad)
            self.cargararreglo(unplanta)
            
                
    def registrarhoras(self):
        dnix=str(input('Ingrese DNI del empleado a buscar (de tipo Contratado) '))
        horax=int(input('Ingrese nueva cantidad de horas del Contratado ingresado '))
        i=0
        while i<len(self.__listaempleados) and dnix!=str(self.__listaempleados[i].getDni()):
            i+=1
        if i==len(self.__listaempleados):
            print('No se encontro el contratado ingresado ')
        else:
            self.__listaempleados[i].cambiarhoras(horax)
            print('Horas cambiadas: {}'.format(self.__listaempleados[i]))    

    def totaltarea(self):
        total=0
        tareax=str(input('Ingrese una tarea a calcular el monto a pagar por ella '))
        for i in range(len(self.__listaempleados)):
            if type(self.__listaempleados[i])==Externo:
                if self.__listaempleados[i].getTarea()==tareax:
                    total+=int(int(self.__listaempleados[i].getMontoviatico())+int(self.__listaempleados[i].getCostoobra())+int(self.__listaempleados[i].getMontoseguro()))
        print('Total que se pagara en la tarea ingresada: {}'.format(total))

    def ayudaeconomica(self):
        print('Listado de los empleados que necesitan ayuda economica ')
        for i in range(len(self.__listaempleados)):
            if self.__listaempleados[i].getSueldo()<15000:
                print('{}'.format(self.__listaempleados[i]))    

    def calcularsueldo(self):
        print('Listado de empleados con sueldo ')
        for i in range(len(self.__listaempleados)):
            print('{} {} {}'.format(self.__listaempleados[i].getNombre(),self.__listaempleados[i].getTelefono(),self.__listaempleados[i].getSueldo()))


    def mostrarempleados(self):
        for i in range(len(self.__listaempleados)):
            print('{}'.format(self.__listaempleados[i]))          

    