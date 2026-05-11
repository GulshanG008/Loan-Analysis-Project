# 🏦 Loan Analysis Model using Machine Learning

A Machine Learning based Loan Analysis Model developed using Python, Scikit-learn, and Streamlit.  
The system analyzes applicant financial and personal details to predict loan approval status and assess applicant risk.

This project also includes:
- Interactive dashboard
- Risk analysis
- Model comparison
- Dataset upload and retraining
- Database integration
- Real-time prediction system

---

# 📌 Project Objective

The main objective of this project is to analyze loan applicant data using machine learning techniques and assist in automated loan-related decision-making.  
The system helps reduce manual effort, improve prediction accuracy, and minimize financial risk for banking and financial institutions.

---

# 🚀 Features

## ✅ Loan Analysis & Prediction
Analyzes applicant information and predicts loan approval status.

## 📊 Dashboard & Visualization
Provides graphical insights into:
- Loan approval distribution
- Credit score analysis
- Income distribution
- Correlation heatmap
- Feature importance

## 🧠 Machine Learning Models
Implements and compares:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

## 🔄 Dynamic Retraining
Allows uploading new datasets and retraining the model dynamically.

## 🗄️ Database Integration
Stores prediction history and user data using SQLite.

## ⚠️ Risk Analysis
Classifies applicants into:
- Low Risk
- Medium Risk
- High Risk

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Framework
- Streamlit

## Machine Learning Libraries
- scikit-learn
- pandas
- numpy

## Visualization Libraries
- matplotlib
- seaborn
- plotly

## Database
- SQLite

## Model Serialization
- joblib

---

# 📂 Project Structure

```text
loan-analysis-project/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── loan_data.csv
│   │
│   └── processed/
│       └── processed_loan_data.csv
│
├── model/
│   ├── loan_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── Loan_Analysis.ipynb
│
├── database/
│   └── loan_app.db
│
├── diagrams/
│   ├── dfd_level_0.png
│   ├── dfd_level_1.png
│   └── er_diagram.png
│
├── requirements.txt
│
├── LICENSE
│
└── README.md
```

---

# 📊 Dataset Information

The dataset contains applicant details used for training and prediction.

| Column Name | Description |
|---|---|
| age | Age of applicant |
| income | Applicant income |
| credit_score | Creditworthiness score |
| dependents | Number of dependents |
| home_owner | House ownership status |
| loan_approved | Loan approval result |

---

# 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Prediction Generation
8. Dashboard Visualization
9. Dataset Retraining

---

# 📈 Exploratory Data Analysis

The project performs:
- Distribution analysis
- Correlation analysis
- Feature importance analysis
- Loan approval trend analysis

Visualization techniques used:
- Count plots
- Histograms
- Box plots
- Heatmaps

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/GulshanG008/Loan-Analysis-Project.git
cd loan-analysis-project
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit plotly joblib
```

---

# ▶️ Run the Application

```bash
streamlit run app/app.py
```

The application will automatically open in your browser.

---

# 🧪 Model Evaluation Metrics

The project evaluates model performance using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 📉 Sample Model Performance

| Model | Accuracy |
|---|---|
| Logistic Regression | 86% |
| Decision Tree | Improved Recall |
| Random Forest | Best Overall Balance |

---

# 🗄️ Database Features

SQLite database stores:
- Applicant details
- Prediction results
- Confidence scores
- Risk levels
- Prediction history

---

# 📊 Dashboard Features

## Prediction Dashboard
- Applicant form
- Real-time prediction
- Confidence score display
- Risk classification

## Analytics Dashboard
- Approval distribution
- Income analysis
- Credit score analysis
- Correlation heatmap
- Feature importance graph

---

# 🔄 Dynamic Features

- Upload new datasets
- Retrain models dynamically
- Save trained models automatically
- Real-time prediction updates

---

# 📁 DFD and ER Diagrams

The project includes:
- DFD Level 0
- DFD Level 1
- ER Diagram

Located in:
```text
diagrams/
```

---

# 🔐 Future Improvements

- User authentication system
- Cloud deployment
- Explainable AI integration
- Real-time banking APIs
- Advanced deep learning models
- Multi-user support

---

# 📷 Screenshots

Add screenshots here:

## Dashboard
```text
screenshots/dashboard.png
```

## Prediction Page
```text
screenshots/prediction.png
```

## DFD & ER Diagrams
```text
screenshots/dfd_er.png
```

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more details.

---

# 👨‍💻 Author

## Gulshan Godsora
MCA Student

---

# ⭐ Conclusion

This project demonstrates how machine learning can be applied to analyze loan applicant data and automate financial decision-making systems.  
The application combines prediction, visualization, database management, and dynamic retraining into a complete end-to-end loan analysis solution suitable for academic and practical learning purposes.
