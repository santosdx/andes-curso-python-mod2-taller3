from models.perro import Perro
from models.boaConstrictor import BoaConstrictor
from models.huron import Huron
from guarderia import Guarderia

"""
print("#### Inicio del Taller 4")

el_perro = Perro("Chocolate", 1, 4)
print('EL perro "{0}" hace {1}'.format(el_perro.get_nombre(), el_perro.hacer_sonido()))

la_boa = BoaConstrictor("Resbalosa", 2, 8, "Brasil", 10)
print('La boa "{0}" hace {1}'.format(la_boa.get_nombre(), la_boa.hacer_sonido()))
la_boa.comer(2)
print("La boa comio {0} ratones.".format(la_boa.get_kilos_comidos()))
la_boa.comer(3)
print("La boa comio {0} ratones.".format(la_boa.get_kilos_comidos()))
print("La boa tiene costo de importación de: $ {0}".format(la_boa.calcular_flete()))

el_huron = Huron("Tomas", 1.5, 4, "Australia", 2.5)
print('El huron "{0}" hace {1}'.format(el_huron.get_nombre(), el_huron.hacer_sonido()))
print("El huron tiene costo de importación de: $ {0}".format(el_huron.calcular_flete()))
"""

print("#### Inicio del Pruebas")
la_boa = BoaConstrictor("Resbalosa", 2, 8, "Brasil", 10)
print('La boa "{0}" hace {1}'.format(la_boa.get_nombre(), la_boa.hacer_sonido()))
el_huron = Huron("Tomas", 1.5, 4, "Australia", 2.5)
print('El huron "{0}" hace {1}'.format(el_huron.get_nombre(), el_huron.hacer_sonido()))

lista_animales = [la_boa, el_huron]
la_guarderia = Guarderia(lista_animales)
la_guarderia.alimentar_boa(la_boa, 2)
la_guarderia.alimentar_boa(la_boa, 20)

otra_boa = BoaConstrictor("Filomena", 2, 8, "Brasil", 10)
la_guarderia.alimentar_boa(otra_boa, 2)
