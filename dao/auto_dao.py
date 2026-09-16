from dao.vehiculo_dao import VehiculoDao

class AutoDao(VehiculoDao):
    """
    Data Access Object para la entidad Auto.
    Hereda de VehiculoDao.
    """
    
    def crear_tabla(self):
        """
        Crea la tabla 'autos' en la base de datos si no existe.
        Invoca primero a super().crear_tabla() para asegurar que 'vehiculos' exista.
        La tabla contiene:
        - patente: TEXT PRIMARY KEY (y Foreign Key hacia vehiculos.patente)
        """
        super().crear_tabla()
        
        sql = """
        CREATE TABLE IF NOT EXISTS autos(
            patente TEXT PRIMARY KEY,
            FOREIGN KEY (patente) REFERENCES vehiculos (patente)
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()
