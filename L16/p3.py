import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("performance.csv")
sub=data["subjects"]
mrks=data["marks"]
plt.plot(sub,mrks,color="purple",linewidth=5,marker="o",markersize=15,markerfacecolor="red")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Performance")
plt.savefig("performance.pdf")
plt.savefig("performance.png")
plt.grid()
plt.show()
