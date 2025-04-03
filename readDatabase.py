import psycopg2


def read_database(db_host, db_port, db_name, db_user, db_password, table):
    # Conexión a la base de datos
    # db_host = "localhost"
    # db_port = 5433
    # db_name = "latienditaqro"
    # db_user = "postgres"
    # db_password = "5715"
    # Inicializar la conexión
    try:
        #Establecer la conexión a la base de datos
        conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port)

        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        # Ejecutar una consulta SELECT para obtener todos los datos de la tabla
        cur.execute(f"SELECT * FROM {table};")

        # Obtener todos los resultados de la consulta
        registros = cur.fetchall()

        # Obtener los encabezados de las columnas (opcional)
        column_names = [desc[0] for desc in cur.description]

        lista_de_diccionarios = []
        # Iterar sobre los registros y añadirlos a un diccionario.
        for fila in registros:
            diccionario_fila = dict(zip(column_names, fila))
            lista_de_diccionarios.append(diccionario_fila)
        # Cerrar el cursor
        cur.close()
        return lista_de_diccionarios
    
        
    except psycopg2.Error as e:
        print(f"Error al conectar o consultar la base de datos: {e}")

    finally:
        # Cerrar la conexión si está abierta
        if conn:
            conn.close()
            print("Conexión a PostgreSQL cerrada.")

# inventario = read_database("localhost", 5433, "latienditaqro", "postgres", "5715", "weed")
# print(inventario)