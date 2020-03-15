# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/13Dataset.csv",encoding="utf-8")

print("\n------- output data :-----------\n")
print("COVID-19 data analysis:")
print("\n-----------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")



#Question - C : print country/region name (using GROUP BY method) and no. of states :

country_names = df.groupby(['Country_Region'])[['Province/State']].count()
print("---------------------------------")
print("\t Country/Region  names : ")
print("-------------------------------")
print(country_names)
print("-------------------------------")
count = 0
for row in range(len(country_names)): 
        count = count+1
print("total no. of available  country/Region = ",count)        
print("-----------------------------\n")

#Question – D : Available last update dates with time(using GROUP BY method)  :

date = df.groupby(['Last Update'])[['Confirmed']].count()
print("---------------------------------")
print("\t Last update Date with time : ")
print("-------------------------------")
print(date)
print("-------------------------------")
count = 0
for row in range(len(date)): 
        count = count+1
print("total no. of available last update dates with time = ",count)        
print("-----------------------------\n")


#Question - E : Data print for UK

print("\n---: convert to Total operation :-------")
df_uk = df[df.Country_Region== 'UK']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_uk.shape)
print('---------------------------------------------')

print('\t Available Dates With times\n--------------------------------')       
dates=df_uk['Last Update']
print(date)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_uk.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

print('\tConfirmed Reporting')
df_1 = df_uk['Confirmed']

print('\t Deaths')
df_2 = df_uk['Deaths']

print('\tRecovered')
df_3 = df_uk['Recovered']

plt.title('plot for UK ')
plt.xlabel("Dates with time serial no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> Confirmed Reporting")

plt.plot(df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> Deaths")

plt.plot(df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> Recovered")
            

            
plt.legend()
plt.show()



#Question - F : Data print for US

print("\n---: convert to Total operation :-------")
df_US = df[df.Country_Region== 'US']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_US.shape)
print('---------------------------------------------')

print('\t Available Dates With times\n--------------------------------')       
dates=df_US['Last Update']
print(date)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_US.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

print('\tConfirmed Reporting')
df_1 = df_US['Confirmed']

print('\t Deaths')
df_2 = df_US['Deaths']

print('\tRecovered')
df_3 = df_US['Recovered']

plt.title('plot for US ')
plt.xlabel("Dates with time serial no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> Confirmed Reporting")

plt.plot(df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> Deaths")

plt.plot(df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> Recovered")
            

            
plt.legend()
plt.show()

#Question - G : Data print for United Arab Emirates(UAE)


print("\n---: convert to Total operation :-------")
df_UAE = df[df.Country_Region== 'United Arab Emirates']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_UAE.shape)
print('---------------------------------------------')

print('\t Available Dates With times\n--------------------------------')       
dates=df_UAE['Last Update']
print(date)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_UAE.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

print('\tConfirmed Reporting')
df_1 = df_UAE['Confirmed']

print('\t Deaths')
df_2 = df_UAE['Deaths']

print('\tRecovered')
df_3 = df_UAE['Recovered']

plt.title('plot for UAE ')
plt.xlabel("Dates with time serial no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> Confirmed Reporting")

plt.plot(df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> Deaths")

plt.plot(df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> Recovered")
            

            
plt.legend()
plt.show()

#Question - H: for Minland China

print("\n---: convert to Total operation :-------")
df_MC = df[df.Country_Region== 'Mainland China']
print('---------------------------------------------')
print("Dimension of the data frame = ",df_MC.shape)
print('---------------------------------------------')

print('\t Available Dates With times\n--------------------------------')       
dates=df_MC['Last Update']
print(date)
print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df_MC.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n") 

print('\tConfirmed Reporting')
df_1 = df_MC['Confirmed']

print('\t Deaths')
df_2 = df_MC['Deaths']

print('\tRecovered')
df_3 = df_MC['Recovered']

plt.title('plot for MC ')
plt.xlabel("Dates with time serial no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df_1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="1 --> Confirmed Reporting")

plt.plot(df_2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="2 --> Deaths")

plt.plot(df_3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="3 --> Recovered")
            

            
plt.legend()
plt.show()
