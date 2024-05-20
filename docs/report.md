# Predicting Customer Subscription to Personal Loan Offers

## Title and Author
- **Project Title:** Predicting Customer Subscription to Personal Loan Offers
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Surya Prakash Reddy Gouni
- **GitHub Profile:** https://github.com/surya61422
- **LinkedIn Profile:** https://www.linkedin.com/in/surya-prakash-reddy-gouni-148011213/

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
https://github.com/surya61422/UMBC-DATA606-Capstone/blob/main/app/DV-1.png
