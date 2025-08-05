import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Crea y retorna un objeto de conexión a la base de datos."""
    try:
        connection_string = os.getenv('DB_CONNECTION_STRING')
        conn = pyodbc.connect(connection_string)
        print("Conexión a la base de datos exitosa.")
        return conn
    except Exception as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        return None

