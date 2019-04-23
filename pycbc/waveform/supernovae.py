"""Generate core-collapse supernovae waveforms
"""

import numpy
import h5py
from pycbc.types import TimeSeries, FrequencySeries, float64, complex128, zeros
from pycbc.waveform.waveform import get_obj_attrs


def get_td_corecollapse_bounce_signal(template=None, **kwargs):
    """generates CCSNe waveform
    """
    
    # check if a hdf file with principal components is provided as an arg:
    if 'pc_hdf_file' in kwargs:
        pc_file = h5py.File(kwargs['pc_hdf_file'], 'r')
        principal_components = numpy.array(pc_file.get('principal_components'))

    if 'principal_components' in kwargs:
        principal_components = kwargs['principal_components']

    pc_len = len(principal_components)
    
    if 'coefficients_array' in kwargs:
        coefficients_array = kwargs['coefficients_array']
    else:
        coeffs_keys = [x for x in kwargs if x.startswith('coeff_')]
        coeffs_keys = numpy.sort(numpy.array(coeffs_keys))
        coefficients_array = numpy.array([kwargs[x] for x in coeffs_keys])

    assert len(coefficients_array) == pc_len

    distance = kwargs['distance']
    mpc_conversion = 3.086e+22
    distance *=  mpc_conversion

    wf = numpy.dot(coefficients_array, principal_components) / distance
    
    delta_t = kwargs['delta_t']
    outhp = TimeSeries(wf, delta_t=delta_t)
    outhc = TimeSeries(numpy.zeros(len(wf)), delta_t=delta_t)

    # returning the same output for hp, hc as 2D waveforms don't have 
    # polarization info
    
    return outhp, outhp


# Approximant names ###########################################################
supernovae_td_approximants = {'CoreCollapseBounce' : get_td_corecollapse_bounce_signal}
