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
            assert isinstance(vv[0], float)
    vv = si.get_solar_irradiance_values(sat_id='WV01', source='Thuillier2003')
    assert len(vv) == 1
