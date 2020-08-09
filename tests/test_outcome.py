from io import StringIO
from unittest.mock import Mock
import pytest
import roulette as rt

def test_outcome():
    o1 = rt.Outcome('Red', 1)
    o2 = rt.Outcome('Red', 1)
    o3 = rt.Outcome('Black', 2)
    assert  str(o1) == 'Red (1:1)'
    assert repr(o2) == "Outcome(name='Red', odds=1)"
    assert o1 == o2
    assert o1.odds == 1
    assert o1.name == 'Red'
    assert o1 != o3
    assert o2 != o3
