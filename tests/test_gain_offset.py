import pytest

from dg_calibration import gain_offset as go


def test_data_saninty():
    assert set(go.GAIN) == set(go.OFFSET)
    for k in go.GAIN:
        assert set(go.GAIN[k]) == set(go.OFFSET[k])


def test_get_gain_values():
    for sat_id in go.GAIN:
        vv = go.get_gain_values(sat_id)
        assert isinstance(vv, list)
        if sat_id == 'WV01':
            assert len(vv) == 0
        else:
            assert isinstance(vv[0], float)


def test_get_offset_values():
    for sat_id in go.OFFSET:
        vv = go.get_gain_values(sat_id)
        assert isinstance(vv, list)
        if sat_id == 'WV01':
            assert len(vv) == 0
        else:
            assert isinstance(vv[0], float)


def test_get_gain_values_invalid_satid():
    sat_id = 'nosatisevercalledthis'
    with pytest.raises(ValueError):
        go.get_gain_values(sat_id)


def test_get_offset_values_invalid_satid():
    sat_id = 'nosatisevercalledthis'
    with pytest.raises(ValueError):
        go.get_offset_values(sat_id)


def test_get_gain_values_known():
    sat_id = 'GE01'
    vv = go.get_gain_values(sat_id)
    assert vv[0] == 1.053
    assert vv[3] == 0.994
