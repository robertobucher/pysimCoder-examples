import numpy as np
import scipy as sp
from control import *
from supsictrl.ctrl_repl import *
from supsictrl.ctrl_utils import *
import matplotlib.pyplot as plt

# Values
R1 = 3.6e3
R2 = 5.6e3
C1 = 100e-6
C2 = 100e-6

# System
a = [[-1/(R1*C1)-1/(R2*C1), 1/(R2*C1)],[1/(R2*C2), -1/(R2*C2)]]
b = [[1/(R1*C1)],[0]]
c = [0, 1]
d = [0]

sysRCRC = ss(a, b, c, d)   # Continous timr system

Ts = 5e-3    # Sampling time

sysRCRCd = c2d(sysRCRC, Ts)

# Control system design
# State feedback with integral part

wn = 5
xi=np.sqrt(2)/2

cl_p1=[1,2*xi*wn,wn**2]
cl_p2=[1,wn]
cl_poly=np.polymul(cl_p1,cl_p2)
cl_poles=np.roots(cl_poly);  # Desired continous poles
cl_polesd=np.exp(cl_poles*Ts)  # Desired discrete poles

Phi_f, G_f = matext(sysRCRCd)

k = place(Phi_f,G_f,cl_polesd)

# Reduced order observer
p_oc=-10*max(abs(cl_poles))
p_od=np.exp(p_oc*Ts);

T=[1, 0]
r_obs=red_obs(sysRCRCd, T, [p_od])

# Full order observer
p_oc=10*np.roots(cl_p1)
p_od=np.exp(p_oc*Ts);
f_obs = full_obs(sysRCRCd, p_od)

contr_I=comp_form_i(sysRCRCd, f_obs, k)

# Anti windup
[gss_in,gss_out]=set_aw(contr_I,[0.1, 0.1, 0.1])

w0 = 25

gf = tf(w0,[1,w0])
gfz = c2d(gf, Ts)
