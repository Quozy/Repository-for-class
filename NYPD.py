import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

nypd = pd.read_csv("NYPD_Arrest_Data__Year_to_Date_.csv", header = 0)

count0 = nypd['AGE_GROUP'].value_counts().get('<18',0)
print("times of '<18': ", count0)
count18 = nypd['AGE_GROUP'].value_counts().get('18-24',0)
print("times of '18-24': ", count18)
count25 = nypd['AGE_GROUP'].value_counts().get('25-44',0)
print("times of '25-44': ", count25)
count45 = nypd['AGE_GROUP'].value_counts().get('45-64',0)
print("times of '45-64': ", count45)
count65 = nypd['AGE_GROUP'].value_counts().get('65+',0)
print("times of '65+': ", count65)

plt.style.use('_mpl-gallery')

# make data:
x = .5 + np.arange(5)
y = [count0, count18, count25, count45, count65]
ageGroups = ('<18', '18-24', '25-44', '45-64', '65+')
# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 5), xticks=np.arange(1, 5),
       ylim=(0, 200000), yticks=np.arange(1, 200000))
p = ax.bar(ageGroups)
ax.bar_label(p, label_type='center')

plt.show()
mjfovvdo