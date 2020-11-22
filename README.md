# group_26
Group repository for DSCI 552, Group 26
# Movie Review Rating Predictor

## Authors: Yuanzhe Marco Ma, Arash Shamseddini, Kaicheng Tan, Zhenrui Yu
## Nov.-Dec. 2020

# Objectives
In this project we tend to build a Regression model that uses the [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html) (SVMs) with RBF kernel algorithm to predict the rating of movies based on the review made. For this aim, we will be using a dataset called “Dataset_IMDB” from [SentimentDictionaries](hhttps://github.com/nproellochs/SentimentDictionaries) library compiled by Nicolas Pröllochs and Stefan Feuerriegel Copyright © under the MIT License. [Here](hhttps://github.com/nproellochs/SentimentDictionaries/blob/master/Dataset_IMDB.csv) is a direct link to the dataset which is sourced open in github.com.
The main objective of this study is to answer the following predictive question using our model:


“Given a review of a specific movie from one of the critics of the list below, what is the critic’s rating of the movie based on a number between 0 and 1?”

| Critics   |       
|----------|
| Dennis Schwartz |  
| James Berardinelli |   
| Scott Renshaw | 
| Steve Rhodes | 

# Dataset
The “Dataset_IMDB” is a mid-sized dataset of 5006 movie reviews from the four critics. It has four columns as shown in below table.

|  Column Name	 | Column Type	 |  Description |  
|---|---|---|
|  Id |  Numeric | Unique ID assigned to each observation|
|   Text|  Free Text	 | Body of the review content|
|  Author | Categorical  | Author's name of the review|
|  Rating | Numeric  | Ratings given along with the review|


# Analysis
For the purpose of this project, we will use SVM with RBF kernel algorithm for our model. We have split the dataset into 80-20 % proportion for the training and test splits respectively. We have built our model using the training portion to come up with the best predictor. Next, we have examined the model using the test split to evaluate its performance. The results of the analysis is in the Report folder [here](https://github.com/UBC-MDS/group_26). These include, but are not limited to, tabeles that summarize the prediction scores as well as figures that show the relation between explanatory variables and the response, interactively.

We will go further with our analysis and use other regression models to predict the ratings and make comparison with the SVM in terms of accuracy and other metrics.

# Exploratory Data Analysis
The Exploratory Data Analysis (EDA) for this project can be found in EDA folder [here](https://github.com/UBC-MDS/group_26/tree/main/EDA) which contains statistical information of the dataset presented in both tables and plots. As an example we have included:

1- A histogram to illustrate the distribution of the ratings.

2- A table that lists the 20 "most frequent" words appeared in all reviews.

3- A chart to depict the relation between the lenght of the reviews and the scored rating.

# Dependencies
Python 3.7.4 and Python packages:

	docopt=0.6.2

	requests=2.22.0

	pandas=0.25.1R

	feather-format=0.4.0

    altair=4.1.0

    scikit-learn=0.23.2

# References
1- Varada Kolhatkar. 2020, “MDS Machine Learning Repository.” University of British Columbia, Vancouver, (https://github.ubc.ca/MDS-2020-21/DSCI_571_sup-learn-1_students)

2- Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences. (http://archive.ics.uci.edu/ml)

3- Gareth James, Daniela Witten, Trevor Hastie and Rob Tibshirani, 2009, “An Introduction to Statistical Learning with Application in R”, Springer Publishing

