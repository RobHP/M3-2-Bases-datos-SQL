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
    query = "SELECT * FROM curso"
    df = pd.read_sql(query, con=conexion)

    # Mostrar los primeros registros del DataFrame (opcional)
    print(df.head())

    # Me! get only a column row datum.
    print("----->",df["nombreDescriptivo"][0])

    # Exportar el DataFrame a un archivo Excel
    nombre_archivo = "registros_curso.xlsx"
    df.to_excel(nombre_archivo, index=False)
    print(f"Datos exportados exitosamente a '{nombre_archivo}'")

    # Cerrar la conexión
    conexion.close()
    print("Conexión cerrada")
else:
    print("Error al conectar a la base de datos")
