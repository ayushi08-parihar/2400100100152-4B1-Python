import matplotlib.pyplot as plt
Pprize=[100,120,90,49,500]
year=[200,400,600,700,800]
Pquantity=[100,80,40,500,10]
plt.ylabel("Year")
plt.xlabel("Prizer")
plt.title("This is my First Graph")
plt.plot(Pprize,year,label="line1",color="red",linestyle="dashed",linewidth="6",marker="o",
         markersize="10",markerfacecolor="blue",markeredgecolor="black")
plt.plot(year,Pquantity,label="line2",color="blue",linestyle="solid")
plt.legend()
plt.show()  
