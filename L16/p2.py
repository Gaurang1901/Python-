import matplotlib.pyplot as plt
subjects = ["phy","chem","math"]
marks = [87,75,99]
plt.plot(subjects,marks,linewidth=5,marker="o",markersize=15,markerfacecolor="red")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Performance")
plt.savefig("performance.pdf")
plt.savefig("performance.png")
plt.grid()
plt.show()
