import pandas as pd
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib 
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from scipy.signal import savgol_filter

def analys(df):
    print('Sensor1', 'Sensor2', 'Sensor3', 'Sensor4')
    trimmed_data = df.head(450000) #Keep a chunk of the data
    cols_to_keep = ['Sensor1', 'Sensor2', 'Sensor3', 'Sensor4', 'CO2 conc (ppm)','Ethylene conc (ppm)']
    timestamp = trimmed_data['Time (seconds)']
    trimmed_data = trimmed_data[cols_to_keep]

    plt.figure(figsize=(24,16))
    plt.subplot(2,1,1)
    plt.plot(timestamp, trimmed_data[['Sensor1', 'Sensor2', 'Sensor3', 'Sensor4',]])
    plt.legend(['Sensor1', 'Sensor2', 'Sensor3', 'Sensor4',], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Sensor Recordings', fontsize=16)

    plt.subplot(2,1,2)
    plt.plot(timestamp, trimmed_data[['CO2 conc (ppm)','Ethylene conc (ppm)']])
    plt.legend(['CO2 conc (ppm)','Ethylene conc (ppm)'], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Concentration (ppm)', fontsize=16)
    
    plt.show()
    
    print('Sensor5', 'Sensor6', 'Sensor7', 'Sensor8')
    trimmed_data = df.head(450000) #Keep a chunk of the data
    cols_to_keep = ['Sensor5', 'Sensor6', 'Sensor7', 'Sensor8', 'CO2 conc (ppm)','Ethylene conc (ppm)']
    timestamp = trimmed_data['Time (seconds)']
    trimmed_data = trimmed_data[cols_to_keep]

    plt.figure(figsize=(24,16))
    plt.subplot(2,1,1)
    plt.plot(timestamp, trimmed_data[['Sensor5', 'Sensor6', 'Sensor7', 'Sensor8',]])
    plt.legend(['Sensor5', 'Sensor6', 'Sensor7', 'Sensor8',], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Sensor Recordings', fontsize=16)

    plt.subplot(2,1,2)
    plt.plot(timestamp, trimmed_data[['CO2 conc (ppm)','Ethylene conc (ppm)']])
    plt.legend(['CO2 conc (ppm)','Ethylene conc (ppm)'], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Concentration (ppm)', fontsize=16)
    
    plt.show()
    
    print('Sensor9', 'Sensor10', 'Sensor11', 'Sensor12')
    trimmed_data = df.head(450000) #Keep a chunk of the data
    cols_to_keep = ['Sensor9', 'Sensor10', 'Sensor11', 'Sensor12', 'CO2 conc (ppm)','Ethylene conc (ppm)']
    timestamp = trimmed_data['Time (seconds)']
    trimmed_data = trimmed_data[cols_to_keep]

    plt.figure(figsize=(24,16))
    plt.subplot(2,1,1)
    plt.plot(timestamp, trimmed_data[['Sensor9', 'Sensor10', 'Sensor11', 'Sensor12',]])
    plt.legend(['Sensor9', 'Sensor10', 'Sensor11', 'Sensor12',], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Sensor Recordings', fontsize=16)

    plt.subplot(2,1,2)
    plt.plot(timestamp, trimmed_data[['CO2 conc (ppm)','Ethylene conc (ppm)']])
    plt.legend(['CO2 conc (ppm)','Ethylene conc (ppm)'], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Concentration (ppm)', fontsize=16)
    
    plt.show()
    
    print('Sensor13', 'Sensor14', 'Sensor15', 'Sensor16')
    trimmed_data = df.head(450000) #Keep a chunk of the data
    cols_to_keep = ['Sensor13', 'Sensor14', 'Sensor15', 'Sensor16', 'CO2 conc (ppm)','Ethylene conc (ppm)']
    timestamp = trimmed_data['Time (seconds)']
    trimmed_data = trimmed_data[cols_to_keep]

    plt.figure(figsize=(24,16))
    plt.subplot(2,1,1)
    plt.plot(timestamp, trimmed_data[['Sensor13', 'Sensor14', 'Sensor15', 'Sensor16',]])
    plt.legend(['Sensor13', 'Sensor14', 'Sensor15', 'Sensor16',], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Sensor Recordings', fontsize=16)

    plt.subplot(2,1,2)
    plt.plot(timestamp, trimmed_data[['CO2 conc (ppm)','Ethylene conc (ppm)']])
    plt.legend(['CO2 conc (ppm)','Ethylene conc (ppm)'], fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Concentration (ppm)', fontsize=16)
    
    plt.show()
    #sorting 
def sor(df):
    sorted_data=df.sort_values(by=["Time (seconds)"])
    sorted_data.head(10)
    return df
def chunk_denoise(sorted_data):
    x1=sorted_data.T.values[0]
    y1=sorted_data.T.values[3]
    x=x1[40000:50000]
    y=y1[40000:50000]

    yhat = savgol_filter(y, 121,2) # window size 121, polynomial order 2
    yhat2= savgol_filter(yhat,121,2)

    plt.figure(1, figsize=(24,16))
    plt.plot(x,y)
    #plt.plot(x,yhat,color="green")

    plt.plot(x,yhat2, color='red',linewidth=4)
    plt.show()
def whole_denoise(sorted_data):
    df_smooth=sorted_data[['Time (seconds)','CO2 conc (ppm)','Ethylene conc (ppm)']]

    # Add the smoothed out data for each sensor
    for i in range(3,19):
        y=sorted_data.T.values[i]
        yhat = savgol_filter(y, 121,2) # window size 121, polynomial order 2
        yhat2= savgol_filter(yhat,121,2)
        df_smooth.loc[:,'Sensor%d'%(i)]=yhat2

    # Rename the data           
    df_smooth=df_smooth.rename(columns = { 3:'Sensor1',4:'Sensor2',5:'Sensor3',6:'Sensor4',7:'Sensor5',8:'Sensor6',9:'Sensor7',10:'Sensor8',11:'Sensor9',12:'Sensor10',13:'Sensor11',14:'Sensor12',15:'Sensor13',16:'Sensor14',17:'Sensor15',18:'Sensor16'})
    df_smooth.head()
    return df_smooth
def dif(df_smooth):
    df_der=df_smooth[['Time (seconds)','CO2 conc (ppm)','Ethylene conc (ppm)']]
    for i in range(3,19):
        df_der.loc[:,'der%d'%(i)]=df_smooth.iloc[:,[i]].shift(-10)-df_smooth.iloc[:,[i]] #Approximate by differences of step 10
    df_der.head()
    return df_der
def plot_der(i,beg,fin,scale,df,der,k=1):

    x=df.T.values[0] #timestamp
    y=df.T.values[1] #CO concentration
    z=50*df.T.values[2] #etholene concentration
    deriv=scale*der.T.values[i] #derivatives scaled by some integer for easier viewing
    x=x[beg:fin]
    y=y[beg:fin]
    deriv=deriv[beg:fin]
    z=z[beg:fin]
    
    plt.figure(k,figsize=(24,16))    #Plot with the given range
    plt.plot(x,y,color="blue",label='CO')    
    plt.plot(x,z,color="orange",label='Ethylene')
    plt.plot(x,deriv,color="green",label='Derivative approximation')
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Concentration(ppm)',fontsize=16)
    plt.legend(fontsize=16)
    plt.show()