from calculadora import soma, subtracao, multiplicacao


def test_soma():

    assert soma(2, 3) == 4


def test_subtracao():
    assert subtracao(5, 3) == 5


def test_multiplicacao():
    assert multiplicacao(4, 3) == 12