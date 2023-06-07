from manejadorempleados import ManejadorEmpleado as ME


if __name__=='__main__':
    dimension=int(input('Inmgrese cantidad de empleados '))
    me=ME(dimension)
    me.cargarempleados()
    print('\n')
    me.mostrarempleados()
    print('\n')
    me.registrarhoras()
    print('\n')
    me.totaltarea()
    print('\n')
    me.ayudaeconomica()
    print('\n')
    me.calcularsueldo()


    