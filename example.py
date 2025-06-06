"""
import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
file_path = 'C:\web dev\Intern-DSR\range vs weight.xlsx'

data = pd.read_excel(file_path)

# Assume the Excel file has columns 'X' and 'Y' for plotting
x = data['Weight']
y = data['Range']

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o')

# Customize the plot
plt.title('Sample Plot from Excel Data')
plt.xlabel('Weight')
plt.ylabel('Range')
plt.grid(True)

# Show the plot
plt.show()
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import os
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'rangevsbatterycap.xlsx')
df=pd.read_excel(file_path)
print(df)

#%matplotlib inline
plt.scatter(df.Range,df.BatteryCapacity,color='red',marker='.')
plt.xlabel('Range')
plt.ylabel('BatteryCapacity')
plt.title('Range vs Battery Capacity')
plt.grid(True)
plt.show()
