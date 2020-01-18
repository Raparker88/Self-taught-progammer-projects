import numpy as np
import matplotlib.pylab as plt
plt.show()
x=np.arange(-4*np.pi,4*np.pi,0.05)
y_sin=np.sin(x)
y_cos=np.cos(x)

plt.plot(x,y_sin,color='red',linwidth=1.5,label="Sin(x)")
plt.plot(x,y_cos,color='blue',label="Cos(x)")
plt.title("Sin vs Cos graph")
plt.xlabell('Angles in radian')
plt.ylabel('sin(x) and cos(x)')
plt.legend(['sin(x)','cos(x)'])
plt.show()
