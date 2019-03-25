"""Generate core-collapse supernovae waveforms
"""

import numpy
import h5py
from pycbc.types import TimeSeries, FrequencySeries, float64, complex128, zeros
from pycbc.waveform.waveform import get_obj_attrs

def get_td_corecollapse_bounce_signal():
    pass

# Approximant names ###########################################################
supernovae_td_approximants = {'CoreCollapseBounce' : get_td_corecollapse_bounce_signal}
