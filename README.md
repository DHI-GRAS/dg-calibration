# dg-calibration
Coefficients and functions for calibrating DigitalGlobe imagery in Python

[![Build Status](https://travis-ci.org/DHI-GRAS/dg-calibration.svg?branch=master)](https://travis-ci.org/DHI-GRAS/dg-calibration)
[![codecov](https://codecov.io/gh/DHI-GRAS/dg-calibration/branch/master/graph/badge.svg)](https://codecov.io/gh/DHI-GRAS/dg-calibration)

Bascially a Python-implementation of https://dg-cms-uploads-production.s3.amazonaws.com/uploads/document/file/209/ABSRADCAL_FLEET_2016v0_Rel20170606.pdf with metadata parsing.

## Installation

Requires `numpy` as single non-trivial dependency. All other dependencies are easily `pip`-installable.

```
pip install -r requirements.txt
pip install .
```

## Usage

### Compute radiance from digital numbers

```python
from dg_calibration import radiance

imdfile = r'/path/to/some/metadata.IMD'

dn = np.random.randint(0, 6000, size=(3, 20, 30))

rad = radiance.dn_to_radiance(dn, imdfile, band_ids=[3, 2, 1])  # band 4, 3, 2
```

### Compute reflectance from digital numbers or radiance

```python
from dg_calibration import reflectance

refl = reflectance.dn_to_reflectance(dn, imdfile, band_ids=None)  # full band stack

refl = reflectance.radiance_to_reflectance(rad, imdfile, band_ids=[3, 2, 1])
```

### Retrieve gain and offset

```python
from dg_calibration import gain_offset

gain = gain_offset.get_gain_values('WV02')
offset = gain_offset.get_offset_values('GE01')
```

## Testing

```
python -m pytest -v
```
