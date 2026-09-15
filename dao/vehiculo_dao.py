from dao.dao import Dao

class VehiculoDao(Dao):
    """
    Data Access Object para la entidad Vehiculo.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):
        """
        Crea la tabla 'vehiculos' en la base de datos si no existe.
        La tabla contiene:
        - patente: TEXT PRIMARY KEY
        - anio: INTEGER NOT NULL
        - en_taller: INTEGER
        - modelo_id: INTEGER NOT NULL (Clave Foránea hacia modelos.id)
        """
        sql = """
        CREATE TABLE IF NOT EXISTS vehiculos(
            patente TEXT PRIMARY KEY,
            anio INTEGER NOT NULL,
            en_taller INTEGER,
            modelo_id INTEGER NOT NULL,
            FOREIGN KEY (modelo_id) REFERENCES modelos (id)
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()
