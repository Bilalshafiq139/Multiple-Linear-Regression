# Multiple-Linear-Regression
This repository contains a Python script that implements Multiple Linear Regression to predict outcomes based on multiple independent variables.

# Multiple Linear Regression Model

## Overview
This repository contains a Python script that implements **Multiple Linear Regression** to predict outcomes based on multiple independent variables. The model is trained using a dataset containing various features related to automobiles.

---

## **Problem Statement**
This project aims to predict a target variable (e.g., car price or fuel efficiency) based on multiple factors such as **horsepower, engine size, and weight** using a **Multiple Linear Regression** model.

### **Why Scaling is Required?**
The features **horsepower, engine size, and weight** have different value ranges. Scaling ensures that no single feature dominates the prediction, improving the model's accuracy and stability.

### **Dataset Description**
The dataset contains multiple columns, including:
- **Horsepower**: Power output of the engine.
- **Engine Size**: Volume capacity of the engine.
- **Weight**: The weight of the vehicle.
- **Target Variable**: The value to be predicted (e.g., car price or fuel efficiency).

---

## **How the Script Works**
1. **Data Loading**: The script reads the dataset from a CSV file.
2. **Data Preprocessing**:
   - Observes the dataset using Pandas `.head()`.
   - Splits the dataset into **training (80%)** and **testing (20%)** sets.
   - Applies **feature scaling** to standardize input variables.
3. **Model Training**:
   - Implements **Multiple Linear Regression** using `sklearn.linear_model.LinearRegression()`.
   - Fits the model on the training dataset.
4. **Prediction**:
   - Makes predictions on the test dataset.
   - Compares predicted vs. actual values using NumPy.
5. **Custom Prediction**:
   - Allows manual input of features to predict an outcome.

---

## **Dependencies**
Ensure you have the following Python libraries installed:
```sh
pip install numpy pandas matplotlib scikit-learn
```

---

## **How to Run the Script**
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project folder:
   ```sh
   cd <project_folder>
   ```
3. Run the Python script:
   ```sh
   python multiple_linear_regression.py
   ```
4. Follow the output to view predictions and comparisons.

---

## **Contributing**
Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or additional features.


