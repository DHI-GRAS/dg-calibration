import os
import glob

here = os.path.abspath(os.path.dirname(__file__))

IMDFILES = {
    os.path.splitext(os.path.basename(p))[0]: p
    for p in glob.glob(os.path.join(here, '*.imd'))}
