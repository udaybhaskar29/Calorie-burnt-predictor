# 🔥 Calorie Burn Prediction using Machine Learning

A machine learning web application that predicts the number of calories burned during exercise based on user information such as age, gender, height, weight, workout duration, heart rate, and body temperature.

The application is built using **Python**, **Random Forest Regressor**, and **Streamlit**.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Features

- Predict calories burned in real time
- Interactive Streamlit web interface
- Machine Learning model using Random Forest Regressor
- Simple and user-friendly design

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

---

## 📊 Model Performance Comparison

| Model | MAE ↓ | RMSE ↓ | R² Score ↑ |
|------|------:|-------:|-----------:|
| Linear Regression | 8.442 | 11.489 | 0.9673 |
| Decision Tree | 3.437 | 5.336 | 0.9929 |
| **Random Forest** | **1.717** | **2.683** | **0.9982** |

> **Best Model:** Random Forest Regressor

---

## 📂 Dataset Features

The model is trained using the following input features:

- Gender
- Age
- Height (cm)
- Weight (kg)
- Workout Duration (minutes)
- Heart Rate (BPM)
- Body Temperature (°C)

Target:

- Calories Burned

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/udaybhaskar29/Calorie-burnt-predictor.git
```

Move into the project folder:

```bash
cd Calorie-burnt-predictor
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

![Home Page](home.png)

![Prediction Page](prediction.png)

---

## 📁 Project Structure

```
Calorie-Burnt-Predictor/
│
├── app.py
├── calorie_burn_prediction_model.pkl
├── exercise.csv
├── calories.csv
├── requirements.txt
├── Calorie_Burn_Prediction.ipynb
└── README.md
```

---

## 📈 Future Improvements

- Improve UI design
- Deploy the application online
- Hyperparameter tuning
- Feature importance visualization
- Model comparison with XGBoost and CatBoost

---

## 👨‍💻 Author

**Uday Bhaskar Dutta**

GitHub: https://github.com/udaybhaskar29

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
