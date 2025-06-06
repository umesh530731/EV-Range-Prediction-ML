# ⚡ EV Range & Performance Predictor

This project is a **Flask-based machine learning web application** that predicts key performance metrics of electric vehicles (EVs) like **range**, **torque**, **efficiency**, and more. It utilizes a **Linear Regression** model trained on real-world EV datasets.

---

## 🔍 Overview

Electric vehicles are becoming the future of transportation. Accurately estimating their performance is crucial for both manufacturers and consumers. This tool simplifies that process using a web-based interface that takes user input and gives predicted outcomes in seconds.

---

## 🚀 Features

- 🔢 **7-output prediction** from a trained regression model
- 📊 Graph-based analysis using `.xlsx` files
- 📁 Includes both Python scripts and Jupyter Notebook development files
- 🌐 Web frontend using Flask + HTML+CSS templates

---

## 🛠️ Tech Stack

| Category       | Tools Used                        |
|----------------|-----------------------------------|
| Backend        | Python, Flask                     |
| Machine Learning | scikit-learn, pandas, numpy     |
| Data Visualization | matplotlib, Excel             |
| Web Templates  | HTML, CSS                         |
| Model Format   | Pickle (`.pkl`)                   |

---

## 📁 Folder Structure

EV-Range-Predictor/
├── app.py # Flask application backend
├── example.py # Graph plotting with matplotlib
├── model.pkl # Trained Linear Regression model
├── model.ipynb # Jupyter Notebook (model training)
├── evdataset.csv # Primary dataset for predictions
├── rangevsweight.xlsx # Excel graph input
├── rangevsbatterycap.xlsx # Excel graph input
├── Graph.xlsx # Additional data
├── templates/
│ ├── index.html # Home input form
│ └── result.html # Prediction result display
└── static/ (optional) # CSS or image files



## ⚙️ How to Run the Project Locally

### 1.Clone the Repo
git clone https://github.com/your-username/ev-range-predictor.git
cd ev-range-predictor

2. Install Python Dependencies
bash
Copy code
pip install flask pandas numpy scikit-learn matplotlib openpyxl
Note: openpyxl is required for reading .xlsx files.

3. Run the Flask App
bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:8000.

📊 Graphs & Data Exploration
You can explore two core visualizations provided in example.py:
Range vs Weight
Range vs Battery Capacity
These are generated from the corresponding Excel files using matplotlib.

🤖 Model Description
Algorithm: Linear Regression,RandomForestRegressor,RandomForestClassifier,DecisionTreeRegressor
Inputs: EV specs (e.g., weight, battery, voltage)
Outputs: 7 predicted values (e.g., range, torque, efficiency, etc.)
Preprocessing: Normalization using sklearn.preprocessing.normalize

📈 Model Evaluation
The trained Linear Regression model was evaluated on a test set split from the EV dataset. Below are the key evaluation details:

✅ Data Split
Training set: 80%
Testing set: 20%
Random state: 42 (for reproducibility)
Normalization: Applied to feature inputs before training using sklearn.preprocessing.normalize

✅ Target Outputs (Multivariate Regression)
The model predicts the following 7 performance metrics simultaneously:
Range
Efficiency
TopSpeed
PeakPower
Torque
Voltage
EnergyConsumption
