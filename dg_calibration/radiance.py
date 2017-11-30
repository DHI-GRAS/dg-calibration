import numpy as np

from dg_calibration import metadata
from dg_calibration import gain_offset
from dg_calibration import bands


def calculate_radiance(dn, gain, offset, absCalFactor, effectiveBandwidth):
    """Compute radiance from digital numbers

    Parameters
    ----------
    dn : ndarray (nbands, ny, nx) or (ny, nx, nbands)
        digital numbers data
    gain, offset : ndarray (nbands)
        gain and offset for all bands in dn data
    absCalFactor, effectiveBandwidth : ndarray (nbands)
        coefficients for all bands in dn data

    Returns
    -------
    ndarray
        radiance
    """
    rolled = False
    if dn.shape[-1] != len(gain):
        dn = np.rollaxis(dn, 0, 3)
        rolled = True

    if not np.issubdtype(dn.dtype, np.float):
        dn = dn.astype('float32')

    # now for the actual calculation
    radiance = gain * dn * absCalFactor / effectiveBandwidth + offset

    if rolled:
        radiance = np.rollaxis(radiance, 2, 0)
    return radiance


def get_parameters(mtd, band_ids=None):
    if mtd['bandId'] != 'Multi':
        raise NotImplementedError(
            'Currently only supporting \'Multi\' (multispectral) metadata. Got \'{}\'.'
            .format(mtd['bandId']))
    if band_ids is None:
        band_ids = slice(None, None)
    sat_id = mtd['satId']
    calvals = {k: bands.get_values_sorted(d, sat_id=sat_id) for k, d in mtd['calibration'].items()}
    calkw = {k: np.array(calvals[k])[band_ids] for k in calvals}
    gain = np.array(gain_offset.get_gain_values(sat_id))[band_ids]
    offset = np.array(gain_offset.get_offset_values(sat_id))[band_ids]
    return dict(calkw, gain=gain, offset=offset)


def dn_to_radiance(dn, imdfile_or_str, band_ids=None):
    """Get radiance from digital numbers and meta data

    Parameters
    ----------
    dn : ndarray (nbands, ny, nx) or (ny, nx, nbands)
        digital numbers data
    imdfile_or_str : str
        path to IMD file or full contents of one
    band_ids : sequence of int, optional
        0-based index of bands in dn data

    Returns
    -------
    ndarray
        radiance
    """
    mtd = metadata.parse_metadata(imdfile_or_str)
    kw = get_parameters(mtd, band_ids)
    return calculate_radiance(dn, **kw)
