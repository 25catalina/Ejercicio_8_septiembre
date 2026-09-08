from mysqlconnection import connectToMySQL


# Creamos la clase basada en la tabla
class Registro:
   def __init__( self , data ):
       self.id = data['id']
       self.nombre = data['nombre']
       self.apellido = data['apellido']
       self.edad = data['edad']
       self.created_at = data['created_at']
       self.updated_at = data['updated_at']

   # Creamos un método de clase para consultar nuestra base de datos
   @classmethod
   def get_all(cls):
       query = "SELECT * FROM registros;"

       # Llamamos a función connectToMySQL con el esquema al que te diriges
       resultados = connectToMySQL('lista_registro').query_db(query)

       # Creamos una lista vacía para agregar nuestras instancias de la tabla
       registros = []

       # Iteramos sobre los resultados de la base de datos y creamos instancias de la clase
       for  usuario in resultados: # usuario es un elemento de la lista de resultados
           registros.append( cls(usuario) )
       return registros

   @classmethod #metodos que se va encargar de crear nuevos registros
   def save(cls, datos):
    query = "INSERT INTO registros (nombre, apellido, edad, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW());"
    return connectToMySQL('lista_registro').query_db(query, datos)