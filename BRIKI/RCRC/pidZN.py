# Modules

from scipy.optimize import leastsq
from matplotlib.pyplot import *
import numpy as np
from control import *
from supsictrl.ctrl_utils import *
from supsictrl.ctrl_repl import *

def respFun(t, K, tau, a):
    N = len(t)
    u = []
    for n in range(0,N):
        if t[n] < tau:
            u.append(0.0)
        else:
            u.append(1.0)

    u = np.array(u)

    y = u*K*(1-np.exp(-a*(t-tau)))
    return y
            
# Motor response for least square identification
def residuals(p, y, t):
    [K,tau, a] = p
    Y = respFun(t, K,tau, a)
    err=y-Y
    return err

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

sysRCRC = ss(a, b, c, d)   # Continous timer system
gRCRC = tf(sysRCRC)

t = np.linspace(0,10, 1001)
t1, y1 = step_response(gRCRC,t)

p0=[1, 0.1, 0.1]
plsq = leastsq(residuals, p0, args=(y1, t1))

[K, tau, a] = plsq[0]
y =  respFun(t, K, tau, a)
plt.plot(t1, y1, t,y)
plt.grid()
plt.show()

# PID after Ziegler-Nichols
ts = 5e-3

L = tau
T = 1/a

Kp = 1.2*K*T/L
Ti = 2*L
Td = 0.5*L
N = 20

Ki = Kp/Ti
Kd = Kp*Td

Gi = tf([ts,0],[1, -1], ts)
Gd = tf([N, -N], [1+N*ts, -1], ts)

