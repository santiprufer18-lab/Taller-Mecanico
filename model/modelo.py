from model.marca import Marca  # Import corregido hacia el paquete model

class Modelo:
    def __init__(self, nombre: str, marca: Marca):
        self.__id = None
        self.__nombre = nombre
        self.__marca = marca

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:
        self.__id = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def marca(self) -> Marca:
        return self.__marca
