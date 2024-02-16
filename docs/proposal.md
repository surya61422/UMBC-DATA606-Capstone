# Predicting Customer Subscription to Personal Loan Offers

## Title and Author
- **Project Title:** Predicting Customer Subscription to Personal Loan Offers
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** [Your Name]
- **GitHub Profile:** [Your GitHub Profile](https://github.com/surya61422)
- **LinkedIn Profile:** [Your LinkedIn Profile](https://www.linkedin.com/in/surya-prakash-reddy-gouni-148011213/)

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
- **Data Size:** Not specified
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

### Target Variable
- **Personal Loan:** Did the customer accept the personal loan offered in the last campaign?

### Features/Predictors
- Age, Experience, Income, ZIP Code, Family, CCAvg, Education, Mortgage, Securities Account, CD Account, Online, Credit Card

