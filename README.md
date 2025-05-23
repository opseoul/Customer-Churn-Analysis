# 📊 Customer Churn Analysis

This project analyzes customer churn behavior using a fictional bank dataset. The goal is to understand which features influence churn, apply feature engineering, and build a predictive model to identify customers at risk of leaving.

---

## 📁 Dataset

The dataset used is `Customer-Churn-Records.csv`, which includes 10,000 customer records with features such as:

- Demographics: `Geography`, `Gender`, `Age`
- Banking activity: `Balance`, `EstimatedSalary`, `Tenure`, `NumOfProducts`
- Behavioral: `IsActiveMember`, `HasCrCard`, `Complain`, `Satisfaction Score`
- Churn label: `Exited` (1 = churned, 0 = retained)

---

## 🧹 Data Cleaning & Preprocessing

- Cleaned malformed columns and ensured proper data types
- Checked for null values (none found)
- Converted currency fields to a consistent format (USD)
- One-hot encoded categorical variables (`Geography`, `Gender`, `Card Type`)
- Removed uninformative identifiers (`RowNumber`, `CustomerId`, `Surname`)

---

## 📊 Exploratory Data Analysis

- **Churn by Gender**: Females had a slightly higher churn rate than males
- **Churn by Geography**: Germany showed the highest churn rate
- **Churn by Age**: Older customers were more likely to churn
- **Churn by Number of Products**: Customers with 3+ products had increased churn
- **Churn by Card Type**: Card type showed no major churn impact
- **Correlation Heatmap**: `Age`, `IsActiveMember`, and `Complain` were most correlated with churn

Plots were created using Seaborn for intuitive visual insights.

---

## 🛠 Feature Engineering

- Encoded categorical variables
- Selected top correlated features using a Random Forest model
- Key features: `Complain`, `Age`, `NumOfProducts`, `IsActiveMember`, `Balance`

---

## 🤖 Model Training

Used a **Random Forest Classifier**:

- Train/test split: 80/20
- Accuracy: **99.9%**
- Confusion Matrix:
[[1606    1]
 [   1  392]]


- - Precision, Recall, F1-score: All near perfect (due to synthetic or cleaned data)

---

## 📌 Key Takeaways

- Customers who lodged complaints were highly likely to churn
- Age and number of products are also strong churn indicators
- The model performs exceptionally well, but should be validated on real-world noisy data

---

## 📂 Repository Structure
Customer-Churn-Analysis/
├── Customer-Churn-Records.csv # Dataset
├── Customer Churn Records.ipynb # Main notebook
├── LICENSE # License info
└── README.md # Project overview


