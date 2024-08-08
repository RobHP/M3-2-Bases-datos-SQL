
import pandas as pd
import mysql.connector

# Establecer la conexión a MySQL
conexion = mysql.connector.connect(
    host="195.179.238.58",
    user="u927419088_admin",
    password="#Admin12345#",
    database="u927419088_testing_sql"
)

if conexion.is_connected():
    print("Conexión establecida correctamente")

    # Consultar datos desde MySQL y cargarlos en un DataFrame
    query = "SELECT * FROM curso where idCurso=1"
    df = pd.read_sql(query, con=conexion)

    # Mostrar los primeros registros del DataFrame (opcional)
    print(df.head())

    # Cerrar la conexión
    conexion.close()
    print("Conexión cerrada")
else:
    print("Error al conectar a la base de datos")
