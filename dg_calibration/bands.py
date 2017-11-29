BAND_ORDER = ['COASTAL', 'BLUE', 'GREEN', 'YELLOW', 'RED', 'REDEDGE', 'NIR1', 'NIR2']


def get_values_sorted(bandsdict):
    """Get values of bandsdict in BAND_ORDER"""
    return [bandsdict[band] for band in BAND_ORDER if band in bandsdict]
