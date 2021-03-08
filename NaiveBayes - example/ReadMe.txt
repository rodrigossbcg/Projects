Project: NaiveBayes - Cross validation

Programming language: R

In this notebook I am going to implement a very simple example of the Naive Bayes algorithm. The dataset in use will be the famous Iris, used many times for classification 
demonstrations. This dataset has information about 3 Species of Iris (Setosa, Versicolour, Virginica). The main goal is for our model to read the data and identify
each observation correctly, as Setosa, Versicolour or Virginica. In addiction, I am going to test the model using the Cross Validation method (K=6). We can benefit from 
this method when our dataset has a reduced number of observations, so reduced that it would be imprudent to divide the dataset into training_set and test_set.

_________________________________________________________________________________________
|                                                                                       |
|   Programming language: R                                                             |
|                                                                                       |
|   Packages used:                                                                      |
|                                                                                       |
|     library(naivebayes)  # Naive Bayes                                                |
|     library(ggplot2)     # Visualization                                              |
|     library(dplyr)                                                                    |
|     library(psych)       # Graph                                                      |
|     library(caret)       # Cross Validation                                           |
|                                                                                       |
|   Model accuracy: 96%                                                                 |
|_______________________________________________________________________________________|

By: Rodrigo Sarroeira
Date: 19/02/2021
