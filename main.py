from conectar import crear_conexion
from dao.marca_dao import MarcaDao
from dao.modelo_dao import ModeloDao
from dao.vehiculo_dao import VehiculoDao
from dao.auto_dao import AutoDao
from dao.moto_dao import MotoDao
from dao.camion_dao import CamionDao


def main():
    # 1. Crear conexión con soporte de Foreign Keys
    conexion = crear_conexion()

    # 2. Creación de tablas en orden de dependencias
    marca_dao = MarcaDao(conexion)
    marca_dao.crear_tabla()

    modelo_dao = ModeloDao(conexion)
    modelo_dao.crear_tabla()

    vehiculo_dao = VehiculoDao(conexion)
    vehiculo_dao.crear_tabla()

    auto_dao = AutoDao(conexion)
    auto_dao.crear_tabla()

    moto_dao = MotoDao(conexion)
    moto_dao.crear_tabla()

    camion_dao = CamionDao(conexion)
    camion_dao.crear_tabla()

    print("Tablas creadas exitosamente: marcas, modelos, vehiculos, autos, motos, camiones.")

    # 3. Cerrar conexión
    conexion.close()


if __name__ == "__main__":
    main()
