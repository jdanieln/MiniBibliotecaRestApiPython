from flask import Flask, jsonify, request
from database.db_connection import get_db_connection

app = Flask(__name__)

#Enpoint para obtener todos los libros con detalles
@app.route("/libros", methods=['GET'])
def get_libros():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'No connection to database!'}), 500

    cursor = conn.cursor()

    # Consulta de SQL que une las tres tablas
    query = """
    SELECT 
        L.Titulo,
        l.AnioPublicacion,
        A.Nombre as AutorNombre,
        A.Apellido as AutorApellido,
        E.Nombre as EditorialNombre
    FROM LIBROS AS L
    JOIN Autores AS A
    ON L.AutorID = A.AutorID
    JOIN Editoriales AS E
    on e.EditorialID = l.EditorialID
    """

    cursor.execute(query)

    libros = []

    for row in cursor.fetchall():
        libros.append({
        "titulo": row.Titulo,
        "anio_publicacion": row.AnioPublicacion,
        "autor": f"{row.AutorNombre} {row.AutorApellido}",
        "editorial": row.EditorialNombre,
        })

    conn.close()
    return jsonify(libros)

# Endpoint para crear un nuevo libro
@app.route("/libros", methods=['POST'])
def add_libro():
    nuevo_libro = request.get_json()

    # Simple validación

    if not nuevo_libro or 'titulo' not in nuevo_libro or 'autor_id' not in nuevo_libro:
        return jsonify({'error': 'Autor and Editorial fields are required!'}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'No connection to database!'}), 500

    cursor = conn.cursor()

    query = "INSERT INTO Libros (Titulo, AnioPublicacion, AutorID, EditorialID ) VALUES (?, ?, ?, ?)"

    try:
        cursor.execute(
            query,
            nuevo_libro['titulo'],
             nuevo_libro['anio_publicacion'],
             nuevo_libro['autor_id'],
             nuevo_libro['editorial_id']
        )
        conn.commit()
        conn.close()
        return jsonify({'success': True}), 201
    except Exception as ex:
        conn.close()
        return jsonify({'error': str(ex)}), 500


if __name__ == "__main__":
    app.run(debug=True)