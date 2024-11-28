import pytest
import numpy as np
from nordanastruct import LoadCase, LoadCombination, SystemElements
from nordanastruct.fem.examples.ex_8_non_linear_portal import ss as SS_ex8
from nordanastruct.fem.examples.ex_7_rotational_spring import ss as SS_ex7
from nordanastruct.fem.examples.ex_11 import ss as SS_ex11
from nordanastruct.fem.examples.ex_12 import ss as SS_ex12
from nordanastruct.fem.examples.ex_13 import ss as SS_ex13
from nordanastruct.fem.examples.ex_14 import ss as SS_ex14
from nordanastruct.fem.examples.ex_15 import ss as SS_ex15
from nordanastruct.fem.examples.ex_16 import ss as SS_ex16
from nordanastruct.fem.examples.ex_17_gnl import ss as SS_ex17
from nordanastruct.fem.examples.ex_18_discretize import ss as SS_ex18
from nordanastruct.fem.examples.ex_19_num_displacements import ss as SS_ex19
from nordanastruct.fem.examples.ex_20_insert_node import ss as SS_ex20
from nordanastruct.fem.examples.ex_26_deflection import ss as SS_ex26


@pytest.fixture
def SS_7():
    return SS_ex7


@pytest.fixture
def SS_8():
    return SS_ex8


@pytest.fixture
def SS_11():
    return SS_ex11


@pytest.fixture
def SS_12():
    return SS_ex12


@pytest.fixture
def SS_13():
    return SS_ex13


@pytest.fixture
def SS_14():
    return SS_ex14


@pytest.fixture
def SS_15():
    return SS_ex15


@pytest.fixture
def SS_16():
    return SS_ex16


@pytest.fixture
def SS_17():
    return SS_ex17


@pytest.fixture
def SS_18():
    return SS_ex18


@pytest.fixture
def SS_19():
    return SS_ex19


@pytest.fixture
def SS_20():
    return SS_ex20


@pytest.fixture
def SS_26():
    return SS_ex26
