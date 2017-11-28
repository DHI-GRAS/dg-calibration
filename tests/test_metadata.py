from . import data

from dg_calibration import metadata


def test_metadata():
    for sat_id, imdfile in data.IMDFILES.items():
        mtd = metadata.parse_metadata(imdfile)
        assert 'sensing_time' in mtd
        assert sat_id == mtd['satId']
