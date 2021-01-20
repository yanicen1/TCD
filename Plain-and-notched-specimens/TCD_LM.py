# Sigma_0 is the ultimate stress for the plain specimen (without a notch). Change it according to your data.
Sigma_0 = 295375266.405298 #(Pa)

import pandas as pd
import numpy as np

# SR is a stress-distance curve for the notched specimen. This curve can be obtained by
# Finite Element Analysis (Ansys, Abaqus, and so on). Store your data in file "stress_riser.csv".
SR = np.array(pd.read_csv('stress_riser.csv'))

Sigma = np.array([[0]])
i = 1
while (Sigma[i-1]*SR[i-1,0] + (SR[i-1,1] + SR[i,1])/2*(SR[i,0] - SR[i-1,0]))/SR[i,0] > Sigma_0:
    Sigma = np.append(Sigma, [(Sigma[i-1]*SR[i-1,0] +
        (SR[i-1,1] + SR[i,1])/2*(SR[i,0] - SR[i-1,0]))/SR[i,0]], axis=0)
    i+=1

# Critical distance value (in mm) according to the line method.
L = (-(SR[i-1,1]/2 - 0.5*(SR[i,0]*(SR[i-1,1] - SR[i,1])/(SR[i-1,0] - SR[i,0]) - SR[i,1]) -
      SR[i-1,0]/2*((SR[i-1,1] - SR[i,1])/(SR[i-1,0] - SR[i,0])) - Sigma_0) -
    ((SR[i-1,1]/2 - 0.5*(SR[i,0]*(SR[i-1,1] - SR[i,1])/(SR[i-1,0] - SR[i,0]) - SR[i,1]) -
  SR[i-1,0]/2*((SR[i-1,1] - SR[i,1])/(SR[i-1,0] - SR[i,0])) - Sigma_0)**2 -
 4*(0.5*(SR[i-1,1] - SR[i,1])/(SR[i-1,0] - SR[i,0]))*(Sigma[i-1]*SR[i-1,0] -
    0.5*SR[i-1,1]*SR[i-1,0] + 0.5*SR[i-1,0]*(SR[i,0]*(SR[i-1,1] - SR[i,1])/(SR[i-1,0] -
        SR[i,0]) - SR[i,1])))**0.5)/2/(0.5*(SR[i-1,1] - SR[i,1])/(SR[i-1,0] - SR[i,0]))/2*1000

print('The critical distance according to the Line Method: L =', float(L.round(4)), "mm")

# Data visualization
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sb

SR_pd = pd.read_csv('stress_riser.csv')
Sigma_0_tab = [Sigma_0 for n in range(len(SR_pd))]
SR_pd['Sigma_0_Pa'] = Sigma_0_tab

plt.figure(figsize=(8,4))
sb.lineplot(x=SR_pd['Length_m'][:2*i+1]*1000, y=SR_pd['MaxPrSt_Pa']/1000000, label="Notched specimen")
sb.lineplot(x=SR_pd['Length_m'][:2*i+1]*1000, y=SR_pd['Sigma_0_Pa']/1000000, label="Plain specimen")
plt.xlim((SR_pd['Length_m'][0]*1000, SR_pd['Length_m'][2*i]*1000))
plt.xlabel("Distance from the notch root (mm)")
plt.ylabel("Stress (MPa)")
plt.show()
