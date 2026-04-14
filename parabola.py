#parabolic graph using loop
import matplotlib.pyplot as plt
x = []
y = []
for i in range(-10,11):

    x.append(i)
    y.append(i**2)
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Parabolic graph")

plt.show()
plt.savefig("parabola.png")
plt.show()

