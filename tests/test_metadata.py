from . import data

from dg_calibration import metadata


def test_metadata():
    for key, imdfile in data.IMDFILES.items():
        sat_id = key.split('_')[0]
        mtd = metadata.parse_metadata(imdfile)
        assert 'sensing_time' in mtd
        assert sat_id == mtd['satId']
