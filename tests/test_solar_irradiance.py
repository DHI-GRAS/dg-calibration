import pytest

from dg_calibration import solar_irradiance as si


def test_get_solar_irradiance_dict():
    for sat_id in si.CSV:
        for source in si.SOURCES:
            dd = si.get_solar_irradiance_dict(sat_id, source=source)
            assert isinstance(dd, dict)
            assert 'PAN' in dd
            assert isinstance(dd['PAN'], float)


def test_get_solar_irradiance_values():
    for sat_id in si.CSV:
        for source in si.SOURCES:
            vv = si.get_solar_irradiance_values(sat_id, source=source)
            assert isinstance(vv, list)
            if sat_id == 'WV01':
                assert len(vv) == 0
            else:
                assert isinstance(vv[0], float)


def test_get_solar_irradiance_values_known():
    VERIFICATION = [
        dict(
            kw=dict(sat_id='GE01', source='Thuillier2003'),
            nvalues=4, idx_values=[(-1, 1022.58)]),
        dict(
            kw=dict(sat_id='WV03', source='ChKur'),
            nvalues=8, idx_values=[(-1, 858.632), (2, 1858.1)])]

    for ver in VERIFICATION:
        vv = si.get_solar_irradiance_values(**ver['kw'])
        assert len(vv) == ver['nvalues']
        for i, val in ver['idx_values']:
            assert vv[i] == val


def test_get_solar_irradiance_values_invalid_source():
    for sat_id in si.CSV:
        source = 'invalid_existing_source'
        with pytest.raises(ValueError):
            si.get_solar_irradiance_values(sat_id, source=source)
