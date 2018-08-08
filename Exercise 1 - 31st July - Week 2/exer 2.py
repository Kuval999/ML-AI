import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series([150,400,225,175,50])
#series.columns=['Beast animals','Other land animals','Birds','Water animals','Reptiles']
series.rename(index={0:'Beast animals',1:'Other land animals',
                     2:'Birds',3:'Water animals',4:'Reptiles'},inplace=True)
series.plot(kind='pie' )
plt.axis("equal")
plt.show()