import sqlite3

#Conexion a base de datos
def query_conexion(consulta, parametros=()):
     with sqlite3.connect('bd.db') as conexion:

            try: #Captura la excepcion en caso de que algo falle
                cursor = conexion.cursor()
                resultado = cursor.execute(consulta, parametros) #  Establece la consulta sql a realizar y sus parametros
                conexion.commit()
                conexion.close()
                return resultado

            except Exception as e:

                print(e)
                conexion.close()
                return False