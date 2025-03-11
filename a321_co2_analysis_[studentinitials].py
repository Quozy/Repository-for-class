import matplotlib.pyplot as plt
import pandas as pd
import math

co2_data = pd.read_csv("co2_data.csv", header=0) 
print(co2_data)


co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)

plt.plot(co2_data['Year'], co2_data['Average'], color='gray')
plt.ylabel('Average Co2')
plt.xlabel('Years')
plt.title('Change in Co2')
plt.show()

