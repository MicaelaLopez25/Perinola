# cada test es un def y cada uno empieza con test si o si! cada uno va aprobar una parte de la apuesta
# solo una parte chiquita 

import pytest

from Clases.apuesta import Apuesta

def test_prueba():
    assert(True)

def test_constructor():
    a = Apuesta ()
    assert(a.fichas == 0 )

def test_repr():
    a = Apuesta()
    msj = a.__repr__()
    assert ("Apuesta: " in msj)
    assert("fichas" in msj)
    assert ("0" in msj)

def test_ponerFicha():
    a = Apuesta()
    a.ponerFicha(8)
    assert(a.fichas == 8)

    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2)

    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2)
    a.ponerFicha(2)
    assert(a.fichas == 4)

def test_tomarFicha_sin_argumentos():
    a = Apuesta()
    a.fichas = 5 
    a.tomarFicha()
    assert(a.fichas == 4)

    a = Apuesta()
    a.fichas = 10 
    a.tomarFicha()
    assert(a.fichas == 9)

def test_tomarFicha_error():
    with pytest.raises(ValueError):
     a = Apuesta()
     a.tomarFicha()