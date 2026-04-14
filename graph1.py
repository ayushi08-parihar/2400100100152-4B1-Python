import matplotlib.pyplot as plt
import numpy as np
prizes=[]
for i in range(100, 500, 10):
    prizes.append(i+2)
print(prizes)
plt.plot(prizes)
plt.show()
#parabolic curve
#x^2
#y=x^2
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y)
plt.show()
