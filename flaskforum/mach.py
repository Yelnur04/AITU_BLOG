import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cancer_filepath = 'C:/Users/ASUS/Downloads/cancer.csv'
cancer_data = pd.read_csv(cancer_filepath, parse_dates=True)




y = cancer_data['Radius (mean)']
x = cancer_data.index = np.arange(1, len(cancer_data) + 1)
plt.plot(x,y)