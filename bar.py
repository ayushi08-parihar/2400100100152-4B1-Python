import matplotlib.pyplot as plt
x=[10,2,3,4]
y=["mohan","sohan","rohan","lohan"]
colour=["red","blue","green","yellow"]
plt.bar(x,y,color=["red","blue","green","yellow"],width=0.5)
plt.show()
plt.bar(y,x,color=colour)
plt.show()