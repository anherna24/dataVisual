# Run in terminal
# pip install ucirepo

from ucimlrepo import fetch_ucirepo 

######### Air Quality #########
# Multivariate, Time Series; Regression

# fetch dataset 
air_quality = fetch_ucirepo(id=360) 
  
# data (as pandas dataframes) 
x = air_quality.data.features 
y = air_quality.data.targets 
  
# metadata 
# print(air_quality.metadata) 