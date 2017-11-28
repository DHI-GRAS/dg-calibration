BAND_ORDER = [
    'PAN', 'COASTAL', 'BLUE', 'GREEN', 'YELLOW', 'RED', 'REDEDGE',
    'NIR1', 'NIR2', 'SIWR1', 'SIWR2', 'SIWR3', 'SIWR4', 'SIWR5',
    'SIWR6', 'SIWR7', 'SIWR8']


def get_values_sorted(bandsdict):
    """Get values of bandsdict in BAND_ORDER"""
    return [bandsdict[band] for band in BAND_ORDER if band in bandsdict]
