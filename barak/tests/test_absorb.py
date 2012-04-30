from ..absorb import *
from ..pyvpfit import *
from ..utilities import get_data_path
import numpy as np

DATAPATH = get_data_path()
atom = readatom()

def test_calctau():
    
    wav0,osc,gam = 1215.6701,0.4164,6.265E8   # Ang, unitless, s^-1
    btemp,bturb = 20., 0.                     # km/s
    v = np.linspace(-100, 100, 500)           # km/s
    logN = 13.0                               # cm^-2
    tau = calctau(v, wav0, osc, gam, logN, btemp=btemp, bturb=bturb)
    tau13 = np.loadtxt(DATAPATH + 'tests/tau_n13.txt.gz')
    assert np.allclose(tau, tau13)
    
    v = np.linspace(-1000, 1000, 1000)        # km/s
    logN = 21.                                # cm^-2
    tau = calctau(v, wav0, osc, gam, logN, btemp=btemp, bturb=bturb)
    tau21 = np.loadtxt(DATAPATH + 'tests/tau_n21.txt.gz')
    assert np.allclose(tau, tau21)
    

def text_calc_iontau():
    wa = np.linspace(2500, 2700, 5000)

    tau = calc_iontau(wa, atom['CIV'], 1.7, 14, 50)

    assert abs(tau.max() - 0.8803955) < 1e-6
    assert abs(tau.min() - 0.0) < 1e-6
    