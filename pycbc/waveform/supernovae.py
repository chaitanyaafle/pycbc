"""Generate core-collapse supernovae waveforms
"""

import numpy
import h5py
from pycbc.types import TimeSeries, FrequencySeries, float64, complex128, zeros
from pycbc.waveform.waveform import get_obj_attrs

def get_td_corecollapse_bounce_signal(coefficients_array, pc_hdf_file, 
                                      template=None, **kwargs):
    """generates CCSNe waveform
    """
    pc_file = h5py.File(pc_hdf_file, 'r')
    principal_components = numpy.array(pc_file.get('principal_components'))

    strain = numpy.dot(coeffs, pc_test)
    return strain

# Approximant names ###########################################################
supernovae_td_approximants = {'CoreCollapseBounce' : get_td_corecollapse_bounce_signal}
