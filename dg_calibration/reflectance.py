import numpy as np

from dg_calibration import metadata
from dg_calibration import solar_irradiance as si
from dg_calibration import earth_sun_distance
from dg_calibration import radiance as radiancemod


def calculate_reflectance(radiance, dsun, solar_irradiance, sun_zenith):
    """Calculate reflectance from radiance data

    Parameters
    ----------
    radiance : ndarray (nbands, ny, nx) or (ny, nx, nbands)
        radiance data
    dsun : float
        distance from Earth to Sun
    solar_irradiance : ndarray (nbands)
        solar irradiance for each band in radiance data
    sun_zenith : float
        Sun zenith angle

    Returns
    -------
    ndarray
        reflectance
    """
    rolled = False
    if radiance.shape[-1] != len(solar_irradiance):
        radiance = np.rollaxis(radiance, 0, 3)
        rolled = True

    # now for the actual calculation
    reflectance = radiance * dsun**2 * np.pi / (solar_irradiance * np.cos(np.radians(sun_zenith)))

    if rolled:
        reflectance = np.rollaxis(reflectance, 2, 0)
    return reflectance


def get_parameters(mtd, band_ids=None):
    if mtd['bandId'] != 'Multi':
        raise NotImplementedError(
            'Currently only supporting \'Multi\' (multispectral) metadata. Got \'{}\'.'
            .format(mtd['bandId']))
    if band_ids is None:
        band_ids = slice(None, None)
    sat_id = mtd['satId']
    sensing_time = mtd['sensing_time']
    sun_zenith = 90 - mtd['angles']['meanSunEl']
    solar_irradiance = np.array(si.get_solar_irradiance_values(sat_id))[band_ids]
    dsun = earth_sun_distance.get_earth_sun_distance(sensing_time)
    return dict(solar_irradiance=solar_irradiance, dsun=dsun, sun_zenith=sun_zenith)


def radiance_to_reflectance(radiance, imdfile_or_str, band_ids=None):
    """Calculate reflectance (via radiance) from digial numbers

    Parameters
    ----------
    radiance : ndarray (nbands, ny, nx) or (ny, nx, nbands)
        radiance data
    imdfile_or_str : str
        path to IMD file or full contents of one
    band_ids : sequence of int, optional
        0-based index of bands in dn data

    Returns
    -------
    ndarray
        reflectance
    """
    mtd = metadata.parse_metadata(imdfile_or_str)
    kw = get_parameters(mtd, band_ids)
    return calculate_reflectance(radiance, **kw)


def dn_to_reflectance(dn, imdfile_or_str, band_ids=None):
    """Calculate reflectance (via radiance) from digial numbers

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
        reflectance
    """
    mtd = metadata.parse_metadata(imdfile_or_str)
    radiance_kw = radiancemod.get_parameters(mtd, band_ids)
    radiance = radiancemod.calculate_radiance(dn, **radiance_kw)
    reflectance_kw = get_parameters(mtd, band_ids)
    return calculate_reflectance(radiance, **reflectance_kw)
