import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt


'''plt.pie([140,70,55,5], labels=['Cars','Motorbikes','Vans','Buses'])
plt.axis('equal')'''
series = pd.Series([140,70,55,5])
series.columns=['Type of vehicle','Number of vehicles']
series.rename(index={0:'Cars',1:'Motorbikes',2:'Vans',3:'Buses'},inplace=True)
series.plot(kind='pie', legend=True)
plt.axis("equal")
plt.show()