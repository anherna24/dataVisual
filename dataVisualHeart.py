# Run in terminal
# pip install ucirepo

from ucimlrepo import fetch_ucirepo 

######### Heart Disease ##############
# Multivariate; Classification
  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
x = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
# print(heart_disease.metadata) 