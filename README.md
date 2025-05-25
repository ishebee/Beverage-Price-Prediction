
# Predicting Survey-Based Price Preferences – ML Project (Atliq Technologies Internship)

This project was developed during a **virtual internship at Atliq Technologies**, and aims to predict a survey respondent's preferred **price range** for a beverage product (CodeX) using machine learning techniques. The project includes everything from **data cleaning**, **EDA**, **feature engineering**, **ML modeling**, **experiment tracking using MLflow & DagsHub**, and a **Streamlit web app deployment**.

---

## Project Files

- `survey_results.csv`: Raw dataset with 30,000+ responses. => (Not providing publicly in github)
- `data_cleaning_instructions.pdf`: PDF with strict cleaning guidelines used during the internship.
- `Survey.ipynb`: Main notebook for EDA, cleaning, feature engineering, and model training.
- `main.py`: Streamlit app for interactive prediction.
- `prediction_helper.py`: Utility functions for input transformation and prediction logic.

---

## Project Summary

### Data Exploration
- Over 30,000 survey responses with age, income, occupation, consumption frequency, brand preferences, etc.
- Initial findings revealed strong influence of **age** and **income levels** on price preference.
- Younger age groups preferred lower price ranges; older groups leaned toward premium options.

### Data Cleaning
- Handled typos and label inconsistencies (e.g., `"Metor"` → `"Metro"`).
- Removed outliers like unrealistic ages (e.g., 604).
- Followed internship-specific cleaning standards from the PDF.

### Feature Engineering
- Derived features:
  - `zac_score`: Combines zone and income for affluence scoring.
  - `cf_ab_score`: Ratio of consumption frequency to brand awareness.
  - `bsi`: Price/quality-sensitive brand switcher flag.
- Encoded ordinal and nominal features using label encoding and one-hot encoding.
- Checked multicollinearity and dropped redundant features.

### Model Building
- Compared several models: Logistic Regression, Random Forest, SVM, Naive Bayes.
- **Final choice**: Logistic Regression – simple and accurate (~80% test accuracy).
- Separate models trained for **young (≤25)** and **older (>25)** customers.
- Evaluation: Stratified train/test split, macro F1 ~0.79, few major misclassifications.

---

## Experiment Tracking

- All experiments tracked using **MLflow**.
- **Remote logging enabled with [DagsHub]([https://dagshub.com/](https://dagshub.com/ishebee/survey-ml-flow-dagshub.mlflow/#/experiments/1?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D&compareRunsMode=ARTIFACT))**.
- Tracked hyperparameters, evaluation metrics, and model artifacts.
- Visual comparison of models helped identify the optimal pipeline.

---

## Streamlit App

A web app was built with **Streamlit** to allow interactive use of the model:

- User inputs demographic and preference data.
- App preprocesses inputs, selects age-appropriate model.
- Returns predicted price range instantly.
- Deployed locally for demo; ready for cloud deployment.

Launch it with:

```bash
streamlit run main.py
```

---

## Requirements

- Python 3.8+
- Key Libraries:
  - pandas, numpy, scikit-learn
  - streamlit, joblib
  - mlflow

Install via:

```bash
pip install -r requirements.txt
```

---

## Highlights

- Complete ML pipeline from raw data to deployed prediction tool.
- 80%+ model accuracy on multiclass classification.
- Advanced feature engineering with real-world logic.
- MLflow + DagsHub used for transparent experiment tracking.
- Interactive Streamlit app with segmentation logic.

---

## Internship

This project was independently developed during a **virtual internship at Atliq Technologies** over **2–3 weeks**, with regular mentor review checkpoints.

---
