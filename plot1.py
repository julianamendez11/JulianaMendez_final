import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos1.dat")

plt.figure()
plt.plot(data[:,1], data[:,2], , c='aquamarine')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

plt.savefig("MendezJuliana_final_15.pdf")
