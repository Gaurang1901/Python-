import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("result.csv")
sub=data["subjects"]
amit=data["amit"]
sumit=data["sumit"]
x=np.arange(len(sub))
plt.bar(x-0.10,amit,width=0.2,label="amit")
plt.bar(x+0.10,sumit,width=0.2,label="sumit")
plt.xticks(x,sub)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Performance")
plt.legend()
plt.show()
 