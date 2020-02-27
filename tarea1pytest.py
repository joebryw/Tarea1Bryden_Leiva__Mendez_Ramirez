import tarea1funciones


def test_capital():
    assert tarea1funciones.capital("joseph")== "JOSEPH"
    assert tarea1funciones.capital(3)== "error"
    assert tarea1funciones.capital("3")== "3"
    assert tarea1funciones.capital("Joseph")== "error"


def test_finder():
    assert tarea1funciones.finder("wendy")== True
    assert tarea1funciones.finder("jose")== False
    assert tarea1funciones.finder("Wanda")== False
    assert tarea1funciones.finder(3)== False


def test_natural():
    assert tarea1funciones.natural(2,3)== "error"
    assert tarea1funciones.natural(3,2)== 1
    assert tarea1funciones.natural(3,-2)== 5
    assert tarea1funciones.natural(-2,3)== "error"
