import pytest
import numpy as np

from dg_calibration import radiance

from . import data


def test_dn_to_radiance():
    dn = np.random.randint(0, 6000, (3, 20, 30))
    for sat_id in ['WV02', 'WV04', 'GE01']:
        imdfile = data.IMDFILES[sat_id]
        out = radiance.dn_to_radiance(dn, imdfile, band_ids=[3, 2, 1])
        assert isinstance(out, np.ndarray)
        assert np.issubdtype(out.dtype, np.float)
        assert np.sum(out > 0) > (out.size * 0.5)


def test_dn_to_radiance_fail_PAN():
    dn = np.zeros(3, dtype=int)
    imdfile = data.IMDFILES['WV04_PAN']
    with pytest.raises(NotImplementedError):
        radiance.dn_to_radiance(dn, imdfile, band_ids=[4, 3, 2])
