#Enter 5 student name and marks and if marks less than 30 use marker colour tred and if above 30 use marker coler blue
import matplotlib.pyplot as plt
name=[]
marks=[]
for i in range(5):
    n=input("Enter name:")
    m=int(input("Enter marks:"))
    name.append(n)
    marks.append(m)
    #use markercolor function red if marks less than 30 and blue if above 30
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Student Marks")
for i in range(5):
    if marks[i]<30:
        plt.plot(name[i],marks[i],marker="o",markersize=10,markerfacecolor="red",markeredgecolor="black")
    else:
        plt.plot(name[i],marks[i],marker="o",markersize=10,markerfacecolor="blue",markeredgecolor="black")

plt.show()
