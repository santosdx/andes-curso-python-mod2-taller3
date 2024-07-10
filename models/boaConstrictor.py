from models.animalExotico import AnimalExotico
from models.iAnimal import IAnimal


class BoaConstrictor(AnimalExotico, IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__raton = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def comer(self, kilos: int):
        if self.__raton + kilos < 10:
            self.__raton = self.__raton + kilos
        else:
            raise ValueError("Demasiados Ratones!")


    def get_kilos_comidos(self):
        return self.__raton
