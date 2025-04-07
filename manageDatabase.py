import psycopg2


def read_database(db_host, db_port, db_name, db_user, db_password, table):

    try:
        #Establecer la conexión a la base de datos
        conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table};")
        registros = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]
        lista_de_diccionarios = []
        for fila in registros:
            diccionario_fila = dict(zip(column_names, fila))
            lista_de_diccionarios.append(diccionario_fila)

        cur.close()
        return lista_de_diccionarios
    
    except psycopg2.Error as e:
        print(f"Error al conectar o consultar la base de datos: {e}")

    finally:
        # Cerrar la conexión si está abierta
        if conn:
            conn.close()
            print("Conexión a PostgreSQL cerrada.")


def update_database(db_host, db_port, db_name, db_user, db_password, table, data):
    try:
        conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port)
        cur = conn.cursor()
        sql = f"UPDATE {table} SET fase = %s WHERE id = %s;"
        cur.execute(sql, (data['Fase'], data['id']))
        conn.commit()
        cur.close()
        
    except psycopg2.Error as e:
        print(f"Error al conectar o consultar la base de datos: {e}")

    finally:
        # Cerrar la conexión si está abierta
        if conn:
            conn.close()
            print("Conexión a PostgreSQL cerrada.")