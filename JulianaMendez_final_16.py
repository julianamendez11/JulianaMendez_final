import numpy as np

tiempo=[73,28,59,52,39,137]
coordenada_x=[4,10,12,80,50,40]
coordenada_y=[100,5,80,50,50,200]

def metropolis_hastings(arreglo):
    
    for i in range(1,10000):
        prop  = arreglo[i-1] + np.random.normal(loc=0.0, scale=1)
        r = min(1,prop/arreglo[i-1])
        alpha = np.random.random()
        if(alpha<r):
            arreglo.append(prop)
        if(alpha>r):
            arreglo.append(arreglo[i-1])
    return np.array(arreglo)



probable=np.mean(metropolis_hastings(tiempo))

print("tiempo de lanzamiento:", " ", probable, "segundos +/- 1 segundo")


probable_x=np.mean(metropolis_hastings(coordenada_x))

print("coordenada x:", " ", probable_x, "Km +/-  1 Km")


probable_y=np.mean(metropolis_hastings(coordenada_y))

print("coordenada y:", " ", probable_y, "Km +/-  1 Km")

velocidad_del_sonido=np.sqrt(probable_x**2 + probable_y**2)/probable
print("Velocidad del sonido:", " ", velocidad_del_sonido, "m/s +/- 1m/s")
