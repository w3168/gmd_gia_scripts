import numpy as np
from pathlib import Path
import pytest

base = Path(__file__).parent.resolve()


@pytest.fixture
def expected_displacement(benchmark):
    return np.loadtxt(base / f"expected-displacement-{benchmark}.dat")[:, 1]


cases = [("weerdesteijn-2d"),
         ("spada-cylindrical-2d-dx500km-nz80-dt50years")
         ]


@pytest.mark.parametrize("benchmark", cases)
def test_viscoelasticity(benchmark, expected_displacement):

    displacement = np.loadtxt(base / f"displacement-{benchmark}.dat")[:, 1]

    # check that greatest (-ve) displacement under ice load is the same as old run
    assert np.allclose(displacement, expected_displacement, rtol=1e-6, atol=1e-16)
