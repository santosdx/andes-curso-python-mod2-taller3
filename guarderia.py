from models.boaConstrictor import BoaConstrictor


class Guarderia:

    # Constructor de la clase Guarderia
    def __init__(self, lista_animales: list):
        self.lista_animales = lista_animales

    def alimentar_boa(self, boa: BoaConstrictor, ratones: int):
        boa_existe = False
        for animal in self.lista_animales:
            if boa is not None and boa.get_nombre() == animal.get_nombre():
                boa_existe = True
                break

        if not boa_existe:
            print("Esta Boa no existe!")
        else:
            try:
                boa.comer(ratones)
            except ValueError as e:
                print(f"La boa está llena, {e}")
            else:
                print("Éxito")
