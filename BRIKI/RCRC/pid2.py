# Modules

from matplotlib.pyplot import *
import numpy as np
from control import *
from supsictrl.ctrl_utils import *
from supsictrl.ctrl_repl import *

set_mydefaults()

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
gRCRC = tf(sysRCRC)

mag, phase, omega=bode_plot(gRCRC);
plt.legend(['G(s)'],prop={'size':10})
plt.show()

wgc = 10         # Desired Bandwidth
desiredPM = 70   # Desired Phase margin

# PI part
Ti=0.15
Gpi=tf([Ti,1],[Ti,0])
print("PI part is: ")
Gpi
m,p,w = bode_plot(Gpi);
plt.show()

m,p,w = bode_plot(gRCRC);
m,p,w = bode_plot(Gpi*gRCRC);
plt.legend((['G(s)','Gpi(s)*G(s)']),prop={'size':10})
plt.show()

mag,phase,omega = bode_plot(Gpi*gRCRC,[wgc],plot=False,Hz=False);
mag

ph = phase[0]/np.pi*180
if ph>=0:
    ph = ph-360;

Phase = -180+desiredPM
dPM = Phase-ph

print("\nAdditional phase from Lead part: ", dPM)
# Lead part
dPMrad = dPM/180*np.pi

alfa = (1+np.sin(dPMrad))/(1-np.sin(dPMrad));
print("Alpha is: ", alfa)

TD = 1/(np.sqrt(alfa)*wgc);
Glead = tf([alfa*TD,1],[TD,1])
print("Lead part is: ")
Glead

m,p,w = bode(Glead);

plt.figure()
m,p,w = bode_plot(gRCRC);
m,p,w = bode_plot(Gpi*gRCRC);
m,p,w = bode_plot( Gpi*Glead*gRCRC);
plt.legend((['G(s)','Gpi(s)*G(s)','Gpi(s)*GLead(s)*G(s)']),prop={'size':10})
plt.show()

mag,phase,omega = bode_plot(Gpi*Glead*gRCRC,[wgc],plot=False)
print("Phase at wgc is: ", phase[0])
K=1/mag[0]
print("Gain to have MAG at gwc 0dB: ", K)
plt.figure()
m,p,w = bode_plot(gRCRC);
m,p,w = bode_plot(Gpi*gRCRC);
m,p,w = bode_plot(Gpi*Glead*gRCRC);
m,p,w = bode_plot(K*Gpi*Glead*gRCRC);
plt.legend((['G(s)','Gpi(s)*G(s)','Gpi(s)*GLead(s)*G(s)','K*Gpi(s)*GLead(s)*G(s)']),prop={'size':10})
plt.show()

Contr = K*Gpi*Glead
print("Full controller: ", Contr)

mag,phase,omega = bode_plot(K*Gpi*Glead*gRCRC,[wgc],plot=False)
print("Data at wgc : ", omega[0], "Magnitude: ",mag[0], "Phase: ",phase[0]/np.pi*180)

gt=feedback(K*Gpi*Glead*gRCRC,1)
gt
t=np.linspace(0,2.5,300)
t,y = step_response(gt,t)
f = plt.figure();
p = plt.plot(t,y)
t=plt.xlabel('t');
t=plt.ylabel('y');
t=plt.title('Step response of the controlled plant');
plt.grid()
plt.show()

ts = 5e-3
contrZ = c2d(Contr,ts)

# Anti windup
[gss_in,gss_out]=set_aw(contrZ,[0, 0])
