import pandas as pd;
import matplotlib.pyplot as plt;
#%matplotlib inline

data = {
    'day':["1/3/2019","2/3/2019","3/3/2019","4/3/2019","5/3/2019","6/3/2019","7/3/2019",],
    'temperature':[23, 24, 25, 34, 21, 28, 36],
    'windspeed':[6,2,8,9,4,5,2],
    'event' : ['Sunny','Rainy','Snow','Sunny','Rainy','Snow','Sunny']
}

df = pd.DataFrame(data);
print(df)
print(df.shape)
#print(df['event'].hist(bins=20))

print(df.head()[['day', 'windspeed']])


##plt.hist(df['temperature'],density=1, bins=20) 
##plt.axis([50, 110, 0, 0.06]) 
###axis([xmin,xmax,ymin,ymax])
##plt.xlabel('Weight')
##plt.ylabel('Probability')
##plt.show()
