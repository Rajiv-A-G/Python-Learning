import pytest

def cap(x):
    if not isinstance(x,str):
        raise TypeError('Not a String')
    return x.capitalize()

def test_cap():
    return cap('r')

def test_capwithnum():
    with pytest.raises(TypeError):
        cap(9)