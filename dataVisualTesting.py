# Run in terminal
# pip install ucirepo

from ucimlrepo import fetch_ucirepo 

######### Air Quality #########
# Multivariate, Time Series; Regression

# fetch dataset 
air_quality = fetch_ucirepo(id=360) 
  
# data (as pandas dataframes) 
X = air_quality.data.features 
y = air_quality.data.targets 
  
# metadata 
# print(air_quality.metadata) 
  

######## Power Consumption ##########
# Multivariate, Time Series; Regression, Clustering
  
# fetch dataset 
individual_household_electric_power_consumption = fetch_ucirepo(id=235) 
  
# data (as pandas dataframes) 
X = individual_household_electric_power_consumption.data.features 
y = individual_household_electric_power_consumption.data.targets 
  
# metadata 
# print(individual_household_electric_power_consumption.metadata) 
  

######### Heart Disease ##############
# Multivariate; Classification
  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
# print(heart_disease.metadata) 
