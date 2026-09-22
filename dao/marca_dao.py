from dao.dao import Dao  # Importa la clase base Dao desde el módulo dao.dao
from model.marca import Marca  # Importa el modelo Marca para construir objetos desde la BD

class MarcaDao(Dao):  # Define la clase MarcaDao que hereda de Dao
    """
    Data Access Object para la entidad Marca.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):  # Define el método para crear la tabla correspondiente
        """
        Crea la tabla 'marcas' en la base de datos si no existe.
        La tabla contiene:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        """
        sql = """
        CREATE TABLE IF NOT EXISTS marcas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)  # Ejecuta la consulta SQL utilizando el cursor heredado
        self.conexion.commit()  # Confirma (guarda) los cambios en la base de datos utilizando la conexión heredada

    def insertar(self, marca):
        self.cursor.execute("INSERT INTO marcas (nombre) values (?)", (marca.nombre,))
        marca.id=self.cursor.lastrowid

    def buscar(self, id):
        self.cursor.execute("SELECT id, nombre FROM marcas WHERE id = ?", (id,))
        fila = self.cursor.fetchone()
        if fila is None:
            return None
        marca = Marca(fila[1])
        marca.id = fila[0]
        return marca

    def listar(self):
        self.cursor.execute("SELECT id, nombre FROM marcas")
        marcas = []
        for fila in self.cursor.fetchall():
            marca = Marca(fila[1])
            marca.id = fila[0]
            marcas.append(marca)
        return marcas

    def actualizar(self, marca):
        self.cursor.execute("UPDATE marcas SET nombre = ? WHERE id = ?", (marca.nombre, marca.id))

    def eliminar(self, id):
        self.cursor.execute("DELETE FROM marcas WHERE id = ?", (id,))

