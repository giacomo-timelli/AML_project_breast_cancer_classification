# Machine Learning Pipeline for Malignant Breast Cancer Cell Prediction

## Index

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Tools Used](#tools-used)

---

## Project Overview

This project implements a supervised machine learning pipeline to classify breast cancer tumors as **benign** or **malignant**, based on diagnostic features extracted from cell nuclei images.

The main goal is to identify the most effective classification model for accurate and rapid tumor detection, ultimately supporting clinical decision-making in medical diagnostics.

---

## Dataset

The analysis is based on the **Breast Cancer Wisconsin (Diagnostic)** dataset, available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(diagnostic)).

> *Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). Breast Cancer Wisconsin (Diagnostic) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.*

Each observation corresponds to a tumor sample, described by 30 numerical features derived from digitized images of a fine needle aspirate (FNA) of a breast mass.

- **Target variable**:
  - `M` → Malignant  
  - `B` → Benign  

- **Main features include**:
  - Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Concave Points, Symmetry, Fractal Dimension

---

## Workflow

### 1. Data Acquisition & Preparation
- Dataset loading
- Data cleaning and formatting

> Initial dataset: [breast_df.csv](train_test_data/breast_df.csv)

---

### 2. Exploratory Data Analysis (EDA)
- Class distribution analysis
- Feature density visualization
- Boxplots grouped by diagnosis
- Correlation heatmap

> Plots available in the [Plots folder](eda)

---

### 3. Feature Engineering
- Train/Test split (80% / 20%) using `train_test_split`
- Feature scaling with `StandardScaler`
- Feature selection using `SelectKBest` and `RFE`

> Generated datasets:
- Training set: [X_train](train_test_data/X_train.csv)  
- Test set: [X_test](train_test_data/X_test.csv)  
- Training labels: [Y_train](train_test_data/Y_train.csv)  
- Test labels: [Y_test](train_test_data/Y_test.csv)  
- Scaled datasets: [X_train_scaled](train_test_data/X_train_scaled.csv), [X_test_scaled](train_test_data/X_test_scaled.csv)  
- Selected features datasets: [X_train_sel](train_test_data/X_train_sel.csv), [X_test_sel](train_test_data/X_test_sel.csv)  
- Labels for selected datasets: [y_train_sel](train_test_data/y_train_sel.csv), [y_test_sel](train_test_data/y_test_sel.csv)  

---

### 4. Model Training & Evaluation

**Models used:**
- Logistic Regression  
- Linear Discriminant Analysis (LDA)  
- k-Nearest Neighbors (KNN)  
- Decision Tree  
- Naive Bayes  
- Support Vector Machine (SVM)  

> Trained models are stored in the [Models folder](trained_models)

**Evaluation metrics:**
- Accuracy  
- Precision & Recall  
- F1 Score  
- Confusion Matrix  
- Matthews Correlation Coefficient (MCC)  
- ROC Curve and AUC  

> ROC curves, AUC values, and confusion matrices are available in the [Plots folder](eda)

---

### 5. Model Comparison

- Comparative analysis of model performance using both visualizations and tabular results

> Final performance summary: [results_models](results.csv)

---

## Tools Used

| Category                  | Libraries              |
|--------------------------|------------------------|
| **Data Handling**        | `pandas`, `numpy`      |
| **Visualization**        | `matplotlib`, `seaborn`|
| **Modeling & Evaluation**| `scikit-learn`         |

---

## References

- [User Guide](https://scikit-learn.org/stable/user_guide.html) – Overview of preprocessing, pipelines, and machine learning models  
- [Getting Started](https://scikit-learn.org/stable/getting_started.html) – Introduction to model training, prediction, and pipelines  
- [API Reference](https://scikit-learn.org/stable/api/index.html) – Full documentation of available classes and functions  

### Key modules used
- [Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)  
- [Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)  
- [Model Selection](https://scikit-learn.org/stable/modules/model_selection.html)  
- [Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)  
- [SVM](https://scikit-learn.org/stable/modules/svm.html)  
- [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)  
- [Decision Trees](https://scikit-learn.org/stable/modules/tree.html)  
- [Neighbors](https://scikit-learn.org/stable/modules/neighbors.html)  
- [Discriminant Analysis](https://scikit-learn.org/stable/modules/lda_qda.html)  
- [Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html)  

---

## AML Basic Course Materials

- Course repository with slides and notebooks: [Repository](https://drive.google.com/drive/folders/1ZrQpF_F9E45yQTO9mG8Izr3LaECVH0aH)

---

## Script for Exporting Pipeline Results

A custom Python script was developed to automatically export key outputs generated during the pipeline execution, including datasets, trained models, and visualizations.

[saving.py](saving_script/saving_script.py)

---

## Author

Giacomo Timelli  

Project developed for the AML Basic Course of the Bioinformatics Master's Degree at the University of Bologna  

📧 giacomo.timelli@studio.unibo.it
