# Run in terminal
# pip install ucimlrepo

from ucimlrepo import fetch_ucirepo 

######## Power Consumption ##########
# Multivariate, Time Series; Regression, Clustering
  
# fetch dataset 
individual_household_electric_power_consumption = fetch_ucirepo(id=235) 
  
# data (as pandas dataframes) 
x = individual_household_electric_power_consumption.data.features 
y = individual_household_electric_power_consumption.data.targets 
  
# metadata 
# print(individual_household_electric_power_consumption.metadata) 

# Algorithms: k-means clustering, Principal component analysis

print(x)