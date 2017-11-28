import numpy as np

from dg_calibration import radiance

from . import data


def test_dn_to_reflectance():
    dn = np.random.randint(0, 6000, (3, 20, 30))
    imdfile = data.IMDFILES['WV02']
    out = radiance.dn_to_radiance(dn, imdfile, band_ids=[4, 3, 2])
    assert isinstance(out, np.ndarray)
    assert np.issubdtype(out.dtype, np.float)
