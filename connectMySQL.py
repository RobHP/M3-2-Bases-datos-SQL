import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    host="195.179.238.58",
    user="u927419088_admin",
    password="#Admin12345#",
    database="u927419088_testing_sql"
)

if conexion.is_connected():
    print("Conexión establecida correctamente")

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta (ejemplo)
    cursor.execute("SELECT * FROM asignatura")

    # Obtener resultados
    resultados = cursor.fetchall()

    # Mostrar los resultados
    for fila in resultados:
        print(fila)

    # Me! Get data type for resultados.
    print("Data type for results",type(resultados))
    print("value for results[0]",resultados[0])

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    print("Conexión cerrada")
else:
    print("Error al conectar a la base de datos")
