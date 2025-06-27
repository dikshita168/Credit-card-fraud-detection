# 💳 Credit Card Fraud Detection

This project is a machine learning-based approach designed to automatically detect fraudulent credit card transactions. As identity theft and online fraud become increasingly common, effective fraud detection mechanisms are crucial to protect individuals and financial institutions from significant losses.

## 🧠 Project Objective

The goal of this project is to build a robust classification model that can distinguish between legitimate and fraudulent credit card transactions using supervised machine learning techniques.

## 📌 Problem Statement

Credit card fraud occurs when someone uses another person's credit card information without authorization. This leads to financial loss and emotional distress for victims. Detecting such frauds in real-time is challenging due to the imbalance of datasets and the subtlety of fraudulent behavior.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Google Colab** – Cloud-based Jupyter notebook environment for running ML models
- **Pandas & NumPy** – Data manipulation and analysis
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Machine learning models and preprocessing
- **Classification Algorithms:**
  - Random Forest
  - AdaBoost
  - Support Vector Machine (SVM)

## 🗃️ Dataset

The dataset used is a publicly available anonymized credit card transaction dataset, which includes:
- Time and Amount of transaction
- PCA-transformed features (V1, V2, ..., V28)
- Class label (0: Legitimate, 1: Fraudulent)

> 📍 Note: The dataset is highly imbalanced with very few fraud cases compared to legitimate transactions.

## 🔍 Key Steps in the Project

1. **Data Exploration and Preprocessing**
   - Handling class imbalance
   - Feature scaling
   - Data visualization

2. **Model Building**
   - Training classifiers like Random Forest, AdaBoost, and SVM
   - Applying cross-validation and performance tuning

3. **Model Evaluation**
   - Precision, Recall, F1-score
   - Confusion Matrix
   - ROC-AUC Curve

4. **Conclusion**
   - Insights and effectiveness of different models


