import numpy as np

from dg_calibration import reflectance

from . import data


def test_radiance_to_reflectance():
    radiance = np.random.random((3, 20, 30))
    imdfile = data.IMDFILES['GE01']
    out = reflectance.radiance_to_reflectance(radiance, imdfile, band_ids=[3, 2, 1])
    assert isinstance(out, np.ndarray)
    assert np.issubdtype(out.dtype, np.float)


def test_dn_to_reflectance():
    dn = np.random.randint(0, 6000, (3, 20, 30))
    imdfile = data.IMDFILES['WV02']
    out = reflectance.dn_to_reflectance(dn, imdfile, band_ids=[4, 3, 2])
    assert isinstance(out, np.ndarray)
    assert np.issubdtype(out.dtype, np.float)
