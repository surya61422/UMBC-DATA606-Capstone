# Predicting Customer Subscription to Personal Loan Offers

## Title and Author
- **Project Title:** Predicting Customer Subscription to Personal Loan Offers
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Surya Prakash Reddy Gouni
- **GitHub Profile:** https://github.com/surya61422
- **LinkedIn Profile:** https://www.linkedin.com/in/surya-prakash-reddy-gouni-148011213/
- **Youtube link:** https://youtu.be/XnEZytazAwQ
  
## Background
### What is it about?
This project aims to predict whether customers will subscribe to personal loan offers provided by a bank based on various demographic and banking-related attributes.

### Why does it matter?
Understanding the factors influencing customers' decisions to subscribe to personal loan offers can help banks optimize their marketing strategies and increase their loan business while retaining existing customers.

### Research Questions
1. What demographic and banking-related factors influence customers' decisions to subscribe to personal loan offers?
2. Can we accurately predict whether a customer will accept a personal loan offer?
3. Which features have the most significant impact on predicting customer subscription to personal loan offers?

## Data
### Data Sources
The dataset provided by the bank contains information on 5000 customers.

### Data Details
- **Data Size:** 212 kb
- **Data Shape:** 5000 rows, [Number of columns]
- **Time Period:** Not specified
- **Each Row Represents:** A customer's demographic and banking information, along with their response to the previous personal loan campaign.

### Data Dictionary
| Column Name        | Data Type | Definition                                                 | Potential Values                        |
|--------------------|-----------|------------------------------------------------------------|-----------------------------------------|
| ID                 | -         | Customer ID                                                | -                                       |
| Age                | Numeric   | Customer's age in completed years                          | -                                       |
| Experience         | Numeric   | Years of professional experience                           | -                                       |
| Income             | Numeric   | Annual income of the customer (in thousand dollars)        | -                                       |
| ZIP Code           | Numeric   | Home Address ZIP code                                      | -                                       |
| Family             | Numeric   | Family size of the customer                                | -                                       |
| CCAvg              | Numeric   | Average spending on credit cards per month (in thousand dollars) | -                                   |
| Education          | Categorical | Education Level                                           | 1: Undergrad<br>2: Graduate<br>3: Advanced/Professional |
| Mortgage           | Numeric   | Value of house mortgage if any (in thousand dollars)       | -                                       |
| Personal Loan      | Binary    | Did this customer accept the personal loan offered in the last campaign? | Yes, No                          |
| Securities Account | Binary    | Does the customer have a securities account with the bank?  | Yes, No                                |
| CD Account         | Binary    | Does the customer have a certificate of deposit account with the bank? | Yes, No                            |
| Online             | Binary    | Do customers use internet banking facilities?              | Yes, No                                |
| Credit Card        | Binary    | Does the customer use a credit card issued by any other bank (excluding All life Bank)? | Yes, No |


## Methodology

To achieve the project goals, the following steps will be undertaken:

### Data Exploration and Preprocessing

1. **Understand the data distribution and handle missing values:**
   - Analyze the dataset to understand its structure and summary statistics.
   - Handle any missing values appropriately to ensure data quality.

2. **Encode categorical variables and normalize numerical variables:**
   - Convert categorical variables into numerical formats using encoding techniques.
   - Standardize numerical variables to bring them to a comparable scale.

### Feature Selection

1. **Identify the most significant features influencing personal loan subscription:**
   - Perform correlation analysis to find relationships between features and the target variable.
   - Utilize feature importance scores from machine learning models to select key features.

### Model Building

1. **Train multiple machine learning models to predict personal loan subscription:**
   - Logistic Regression
   - Decision Trees
   - Random Forest
   - Gradient Boosting

2. **Evaluate models using appropriate metrics:**
   - Accuracy
   - Precision
   - Recall
   - F1-score

### Model Evaluation and Selection

1. **Compare the performance of different models:**
   - Assess the models based on evaluation metrics to identify the best-performing model.

2. **Select the best-performing model for final deployment:**
   - Choose the model with the highest performance for deployment.

### Insights and Recommendations

1. **Interpret the model results to identify key factors influencing loan subscription:**
   - Analyze the selected model to understand which features significantly impact the prediction.

2. **Provide actionable insights and recommendations for the bank’s marketing strategy:**
   - Use the insights gained from the model to suggest improvements in marketing strategies, targeting high-potential customers more effectively.

## Data Visualisations
### 1.Value of count of age
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-1.png)
### 2.Value of count of income distribution
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-2.png)
### 3.Value of count of education level
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-3.png)
### 4.Value of count of personal loan acceptance by education level
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-4.png)
### 5.Relationship between age and income
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-5.png)
### 6.Value of count of family sizes
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-6.png)
### 7.correlation matrix
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-7.png)

## Model building
### Report on Logistic Regression for Predicting Customer Subscription to Personal Loan Offers

#### Introduction

The aim of this report is to detail the implementation and performance evaluation of Logistic Regression in predicting customer subscription to personal loan offers. Logistic Regression is a binary classification algorithm, and in this project, it helps determine whether a customer will accept a personal loan offer based on various demographic and banking-related attributes.

#### Methodology Overview

1. **Data Exploration and Preprocessing:**
   - Explored the dataset to understand its distribution and handle missing values appropriately.
   - Encoded categorical variables and normalized numerical variables to prepare the data for modeling.

2. **Feature Selection:**
   - Identified significant features using correlation analysis and feature importance from machine learning models.

3. **Model Building:**
   - Trained multiple machine learning models, including Logistic Regression, to predict personal loan subscription.

4. **Model Evaluation and Selection:**
   - Compared the performance of different models using metrics such as accuracy, precision, recall, and F1-score.
   - Selected the best-performing model based on evaluation metrics for final deployment.

#### Logistic Regression Implementation

1. **Data Preparation:**
   - **Feature Selection:** Dropped irrelevant features like 'ID' and 'ZIP Code'. The target variable is 'Personal Loan'.
   - **Data Splitting:** Split the dataset into training (80%) and testing (20%) sets.
   - **Feature Scaling:** Standardized numerical features using StandardScaler.

2. **Model Training:**
   - Utilized Logistic Regression to train the model on the preprocessed training data.

3. **Model Prediction and Evaluation:**
   - Predicted the target variable on the test data using the trained model.
   - Evaluated the model's performance using accuracy, confusion matrix, and classification report.

#### Results and Analysis

- **Accuracy:** Achieved an accuracy of 95%, indicating that the model correctly predicts personal loan subscriptions for 95% of the customers in the test dataset.
- **Confusion Matrix:** The confusion matrix provides insight into the model's performance in terms of true positive, true negative, false positive, and false negative predictions.
- **Classification Report:** The classification report presents precision, recall, F1-score, and support for each class, providing a comprehensive evaluation of the model's performance across different metrics.

## Deployment using streamlit
With Streamlit, an open-source Python toolkit, you can quickly and easily develop interactive web apps for data science, machine learning, and other applications. It makes writing Python scripts that automatically convert into interactive web applications easier when creating data-driven web applications.
![image](https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/Streamlit.png)
## Conclusion


In conclusion, this study demonstrates the effective use of a dataset containing demographic and banking-related characteristics to predict client subscription to personal loan offers using logistic regression. We made certain that the model had pertinent and useful data for producing precise predictions by applying rigorous data exploration, preprocessing methods, and feature selection. The final model's remarkable 95% accuracy rate shows how reliable it is in predicting consumer actions linked to the approval of personal loans. Moreover, thorough assessment metrics that confirmed the model's efficacy and dependability included the confusion matrix and classification report, which offered deeper insights into the model's performance.
The significance of machine learning algorithms, such logistic regression, in providing financial institutions with useful information to improve client interaction and marketing tactics is highlighted by this study. Banks may increase customer satisfaction and loyalty by customizing their loan offerings to each individual's tastes and requirements by utilizing the predictive powers of these models. In the end, this research demonstrates how data-driven methods may revolutionize strategic decision-making and maximize financial sector business outcomes.








