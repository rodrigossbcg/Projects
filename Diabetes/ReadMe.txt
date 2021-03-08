In this notebook I will implement an K-Nearest Neighbors algorithm. KNN algorithm was created by Evelyn Fix and Joseph Hodges in 1951, it can be used for both 
regression and classification problems. In this example I will be using KNN for classification, since the problem consists on determining whether a person has 
diabetes or not. The data set in use is "diabetes.csv". This csv file contains medical information related with the diabetes desiese, the variables that compose 
it are the following: 

Pregnancies - Number of pregnancies;
Glucose - Glucose levels on blood;
BloodPressure -  Diastolic blood pressure (mm Hg);
SkinThickness - Skin Thickness (mm);
Insulin - Insulin level on blood;
BMI - Body Mass Index (weight in kg/(height in m)2);
DiabetesPedigreeFunction - 
Age - Age of the individual in years;
Outcome - Boolean variable reflecting the existance of diabetes in each individual;


_________________________________________________________________________________________
|                                                                                       |
|   Link to dataset: https://www.kaggle.com/uciml/pima-indians-diabetes-database        |
|                                                                                       |
|   Programming language: R                                                             |
|                                                                                       |
|   Packages used:                                                                      |
|                                                                                       |
|     library(class)       # KNN model                                                  |
|     library(caTools)     # divide yesy and train sets                                 |
|     library(psych)       # Graph                                                      |
|     library(ggplot2)     # Visualization                                              |
|                                                                                       |
|   Model accuracy: 82,5%                                                               |
|_______________________________________________________________________________________|

By: Rodrigo Sarroeira
On: 3/8/2021
