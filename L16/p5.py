import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("performance.csv")
sub=data["subjects"]
mrks=data["marks"]
plt.bar(sub,mrks,color="purple",width=0.4)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Performance")
plt.show()
