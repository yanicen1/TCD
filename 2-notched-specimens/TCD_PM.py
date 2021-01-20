import pandas as pd
import numpy as np

# SR contains stress-distance data for 2 notched specimens. This data can be obtained by
# Finite Element Analysis (Ansys, Abaqus, and so on). Store your data in file "stress_riser.csv".
SR = np.array(pd.read_csv('stress_riser.csv'))
SR_new = SR

if SR[0,1] < SR[0,2]:
    SR_new = np.hstack((SR[:,0:1], SR[:,2:], SR[:,1:2]))

i = 0
while SR_new[i,1] > SR_new[i,2]:
    i+=1

# Critical distance value (in mm) according to the point method.
L = 2000*(((SR_new[i,1]-SR_new[i-1,1])/(SR_new[i,0]-SR_new[i-1,0])*SR_new[i-1,0] - SR_new[i-1,1] -
       (SR_new[i,2]-SR_new[i-1,2])/(SR_new[i,0]-SR_new[i-1,0])*SR_new[i-1,0] + SR_new[i-1,2]) /
       ((SR_new[i,1]-SR_new[i-1,1])/(SR_new[i,0]-SR_new[i-1,0]) -
       (SR_new[i,2]-SR_new[i-1,2])/(SR_new[i,0]-SR_new[i-1,0]))) #(mm)

print('The critical distance according to the Point Method: L =', float(L.round(4)), 'mm')

# Data visualization
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sb

SR_pd = pd.read_csv('stress_riser.csv')

plt.figure(figsize=(8,4))
sb.lineplot(x=SR_pd['Length_m'][:3*i+1]*1000, y=SR_pd['MaxPrSt1_Pa']/1000000, label="Notched specimen 1")
sb.lineplot(x=SR_pd['Length_m'][:3*i+1]*1000, y=SR_pd['MaxPrSt2_Pa']/1000000, label="Notched specimen 2")
plt.xlim((SR_pd['Length_m'][0]*1000, SR_pd['Length_m'][3*i]*1000))
plt.xlabel("Distance from the notch root (mm)")
plt.ylabel("Stress (MPa)")
plt.show()
