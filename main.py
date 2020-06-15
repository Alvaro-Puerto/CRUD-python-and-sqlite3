
from os import system

from conexion import query_conexion

import sqlite3


class Persona():
    """
    Clase persona con los metodos utilizados para el CRUD
    
    """

    def __init__(self, *args, **kwargs):
        self.id = 0
        self.nombre = ''
        self.edad = 0

    def guardar(self): 

        consulta = 'INSERT INTO persona VALUES(NULL, ?, ?)'
        parametros = [self.nombre, self.edad]

        return query_conexion(consulta, parametros) # Funcion que sirve para conectar la bd con su consulta 
        
    def actualizar(self):
       
        consulta = 'SELECT * FROM persona WHERE id=?'
        parametros = [self.id]

        resultado = query_conexion(consulta, parametros)

        if resultado:
            for datos in resultado:

                print("""
                ID      NOMBRE                     EDAD
                {}        {}                       {}
                ____________________________________________
                
                """.format(datos[0], datos[1], datos[2]))

                try:
                    nuevo_nombre = input('Ingrese el nuevo nombre -> : ')
                    nueva_edad =  input('Ingrese la nueva edad -> :')
                    
                    if nuevo_nombre == '':
                        nuevo_nombre = datos[1]

                    if nueva_edad == '':
                        nueva_edad = datos[2]
                    
                    consulta = 'UPDATE FROM persona set nombre=?, set edad=? WHERE id=?' #---PENDIENTE
                    parametros=[nuevo_nombre, int(nueva_edad), datos[0]]

                    query_conexion(consulta, parametros)

                except Exception as e:
                    print('Operacion erronea ')

        else:
            print('error')

        input()

    def eliminar(self):
        
        consulta = 'DELETE FROM  persona WHERE id=?'
        parametros = [self.id]
        resultado = query_conexion(consulta, parametros)

        if resultado:
            print('Borrado del registro exitoso')
        else:
            print('Error en la operacion ')

        input()
        system("clear")
        




if __name__ == "__main__": #    main del script

    centinela = True

    while(centinela):
        system('clear')
        print(""" 
        ***************** CRUD con sqlite3 *******************
        
                    1- Agregar registro 
                    2- Editar registro
                    3- Eliminar registro
                    4- Listar registros
                    5- Salir
        """)
        print()

        try:

            op = int(input("Seleccione una opcion 1-4 -> : "))
            system('clear')

        except Exception as e:

            op = False

        if op == 1: # Guardar

            persona = Persona()

            try:
                persona.nombre = input('Ingrese el nombre ->  : ')
                persona.edad = int(input('Ingrese la edad -> : '))

                if persona.guardar():

                    print('Insercion exitosa')
                   
                else:

                    print('Error en la insercion')
                    
            except Exception as e:

                print('Error en los datos ingresados ')

            input()

        elif op == 2: #Editar

            try:

                persona = Persona()
                persona.id = int(input('Ingrese el Id de la persona -> : '))
                persona.actualizar()
               
            except Exception as e:
                op = False


        elif op == 3: # Eliminar 
            persona = Persona()

            try:
                persona.id = int(input("Ingrese el Id de la persona a eliminar -> :"))
                persona.eliminar()
            
            except Exception as e:
                op = False

            
        elif op == 4: # Listar

            consulta = 'SELECT * FROM persona '
            parametros = []
            resultado = query_conexion(consulta)

            print("""
            ________________________________________________________
            |           |                              |            |
            |   ID      |    Nombre                    |   Edad     |
            |___________|______________________________|____________|""")
            

            if resultado:
                for datos in resultado:
                  print(
            """
               {}         {}                           {}          
            _______________________________________________________
            """.format(datos[0], datos[1], datos[2])
            )

            input()
            

        elif op == 5: # Salir 

            centinela = False
            print('Cerrando script')
            input()

        else: # Opciones invalidas 

            print('Opcion invalida')
            input()
        











    