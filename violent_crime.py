import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

vcrimedata = pd.read_csv("fbi.csv", header = 0)

import numpy as np


plt.plot(vcrimedata['Year'], vcrimedata['Violent crime rate'], color='blue')
plt.xticks(np.arange(2000,2020,2))
plt.ylabel("Crime")
plt.xlabel("Years")
plt.title("Crime Data")

plt.show()