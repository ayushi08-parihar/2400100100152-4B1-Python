import matplotlib.pyplot as plt
prizes=[100, 200, 300, 400, 500]
year=[2010, 2011, 2012, 2013, 2014]
'''plt.plot(year, prizes)
#plt.xlabel('Year')
#plt.ylabel('Prize Amount')
plt.show()
plt.bar(year, prizes)
plt.show()
plt.hist(year, prizes)
plt.show()
plt.pie(prizes, labels=year)
plt.show()'''
plt.scatter(year, prizes)
plt.show()

#draw a parabolic graph
import numpy as np
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y)
plt.show()

#draw a sine wave
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

