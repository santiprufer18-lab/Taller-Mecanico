from dao.vehiculo_dao import VehiculoDao

class CamionDao(VehiculoDao):
    """
    Data Access Object para la entidad Camion.
    Hereda de VehiculoDao.
    """
    
    def crear_tabla(self):
        """
        Crea la tabla 'camiones' en la base de datos si no existe.
        Invoca primero a super().crear_tabla() para asegurar que 'vehiculos' exista.
        La tabla contiene:
        - patente: TEXT PRIMARY KEY (y Foreign Key hacia vehiculos.patente)
        - capacidad_carga: INTEGER NOT NULL
        """
        super().crear_tabla()
        
        sql = """
        CREATE TABLE IF NOT EXISTS camiones(
            patente TEXT PRIMARY KEY,
            capacidad_carga INTEGER NOT NULL,
            FOREIGN KEY (patente) REFERENCES vehiculos (patente)
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()
