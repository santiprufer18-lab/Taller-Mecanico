import conectar  # Importa el módulo conectar para inicializar la base de datos
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
# from dao.modelo_dao import ModeloDao  # Importa el DAO de modelos
# from dao.auto_dao import AutoDao  # Importa el DAO de autos (que también gestiona vehículos)
from model.marca import Marca  # Importa el modelo Marca para instanciar objetos

def main():  # Función principal de ejecución
    print("--- Inicializando Base de Datos ---")  # Mensaje de inicio
    
    # 1. Crear conexión
    conn = conectar.crear_conexion()  # Llama a crear_conexion para obtener el objeto de conexión
    
    # 2. Instanciar el DAO pasándole la conexión
    marca_dao = MarcaDao(conn)  # Instancia MarcaDao entregando la conexión
    # modelo_dao = ModeloDao(conn)  # Instancia ModeloDao entregando la conexión
    # auto_dao = AutoDao(conn)  # Instancia AutoDao entregando la conexión
    
    # 3. Asegurar que la tabla exista antes de insertar
    marca_dao.crear_tabla()  
    
    # --- INSERCIÓN DE MARCAS MÁS POPULARES EN CHILE ---
    print("\n--- Insertando marcas populares en Chile ---")
    nombres_marcas = [
        "Lexus",
        "Toyota",
        "Chevrolet",
        "Hyundai",
        "Kia",
        "Nissan",
        "Suzuki",
        "Mazda",
        "Ford",
        "Volkswagen",
        "Peugeot",
        "Renault",
        "Honda",
        "Mitsubishi",
        "Jeep",
        "Tesla",
    ]

    # for nombre in nombres_marcas:
    #     marca = Marca(nombre)  # Instanciamos cada marca
    #     marca_dao.insertar(marca)  # Insertamos en la base de datos
    #     conn.commit()  # Guardamos los cambios
    #     print(f"Marca '{marca.nombre}' insertada con ID: {marca.id}")

    # --- PRUEBA DEL MÉTODO LISTAR ---
    print("\n--- Probando método listar() ---")
    todas_las_marcas = marca_dao.listar()
    for m in todas_las_marcas:
        print(f"ID: {m.id} | Marca: {m.nombre}")

    # --- PRUEBA DEL MÉTODO BUSCAR ---
    print("\n--- Probando método buscar() ---")
    id_a_buscar = 2  # Probamos buscando el ID 2 (debería ser Toyota)
    marca_encontrada = marca_dao.buscar(id_a_buscar)
    
    if marca_encontrada:
        print(f"¡Marca encontrada! ID: {marca_encontrada.id} corresponde a {marca_encontrada.nombre}")
    else:
        print(f"No existe ninguna marca con el ID {id_a_buscar}")

    # --- PRUEBA DEL MÉTODO ACTUALIZAR ---
    print("\n--- Probando método actualizar() ---")
    marca_a_actualizar = marca_dao.buscar(1)  # Buscamos Lexus (ID 1)
    if marca_a_actualizar:
        print(f"Antes de actualizar: {marca_a_actualizar.nombre}")
        # Para actualizar, modificamos el atributo 'nombre' (rompiendo temporalmente el encapsulamiento para la demo, o creando una nueva)
        # Como __nombre es privado, lo ideal es crear un objeto nuevo con el mismo ID, o tener un setter. 
        # Como no hay setter de nombre, creamos una nueva instancia con el mismo ID.
        marca_modificada = Marca("Lexus Premium")
        marca_modificada.id = 1
        
        marca_dao.actualizar(marca_modificada)
        conn.commit()
        
        verificacion = marca_dao.buscar(1)
        print(f"Después de actualizar: {verificacion.nombre}")

    # --- PRUEBA DEL MÉTODO ELIMINAR ---
    print("\n--- Probando método eliminar() ---")
    id_a_eliminar = 16  # Asumiendo que Tesla es la 16
    print(f"Eliminando marca con ID {id_a_eliminar}...")
    marca_dao.eliminar(id_a_eliminar)
    conn.commit()
    
    verificacion_eliminado = marca_dao.buscar(id_a_eliminar)
    if not verificacion_eliminado:
        print(f"¡Eliminación exitosa! La marca con ID {id_a_eliminar} ya no existe.")
    
    # --- RESTO DEL CÓDIGO COMENTADO PARA REFERENCIA ---
    # print("\nCreando resto de las tablas...")
    # modelo_dao.crear_tabla()  # Ejecuta la creación de la tabla modelos
    # auto_dao.crear_tabla()  # Ejecuta la creación de las tablas vehiculos y autos (por herencia)
    
    # 4. Validar que las tablas existan en la BD
    # cursor = conn.cursor()  # Obtiene un cursor directamente desde la conexión para una consulta general
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")  # Consulta al maestro de SQLite por los nombres de las tablas
    # tablas_creadas = [fila[0] for fila in cursor.fetchall()]  # Extrae los nombres de las tablas en una lista
    
    # print("\n--- Tablas encontradas en la Base de Datos ---")  # Mensaje informativo
    # for tabla in tablas_creadas:  # Itera sobre la lista de tablas encontradas
    #     # Excluimos la tabla interna de SQLite
    #     if tabla != "sqlite_sequence":  # Ignora 'sqlite_sequence' que es una tabla del sistema
    #         print(f"- {tabla}")  # Imprime el nombre de cada tabla de nuestro negocio
    
    print("\nProceso finalizado exitosamente.")  # Mensaje final de éxito

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal
