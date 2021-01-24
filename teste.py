import pytest

from calculadora import soma

def teste_soma():
    """Testa a fun soma do modulo 'Calculadora' """
    assert soma(2, 4) == 6
