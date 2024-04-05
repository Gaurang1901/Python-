import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("result.csv")
sub=data["subjects"]
amit=data["amit"]
sumit = data["sumit"]
plt.plot(sub,amit,label="amit",marker="o")
plt.plot(sub,sumit,label="sumit",marker="o")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Performance")
plt.savefig("performance.pdf")
plt.savefig("performance.png")
plt.legend()
plt.grid()
plt.show()
