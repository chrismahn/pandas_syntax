import pandas as pd
#import datetime
#from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2015, 1, 1)
#
# df = web.DataReader('XOM', 'yahoo', start, end)
#
# print(df.head())
#
# df['Adj Close'].plot()
#
# plt.show()


##converting dict with pd dataframe
web_stat = {
    'Day':[1,2,3,4,5,6],
    'Visitors':[43,53,34,45,64,34],
    'Bounce Rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stat)

# print(df)
# print(df.head(4))

##set index to df
df.set_index('Day', inplace=True)
print(df.head())

##print specific column
print(df['Visitors'])
print(df.Visitors)

##referance multi column
#print(df[['Visitors','Day']])


##convert DataFrame to list
print(df.Visitors.tolist())

## convert multi list to numpy array
convert = np.array(df[['Visitors','Bounce Rate']])
print(convert)