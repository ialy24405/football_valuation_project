
# ⚽ Football Player Valuation Predictor

## 📌 Project Overview
This project is an end-to-end Machine Learning pipeline designed to predict the fair market value of football players based on their attributes (Age, Overall Rating, Potential, and Playing Positions). Built with Python and scikit-learn, the project culminates in a user-friendly interactive web application using Streamlit.

## 🚀 Features
* **Automated Environment Setup:** Custom PowerShell scripting (`New-AIProject`) utilizing `uv` for lightning-fast project initialization and Git configuration.
* **Advanced Data Preprocessing:** Cleaned FIFA dataset, handling missing values, and implementing **Multi-Hot Encoding** for complex player positions (e.g., players who can play ST, RW, and CAM simultaneously).
* **Machine Learning:** Transitioned from a baseline Linear Regression model to a robust **Random Forest Regressor** to capture the non-linear dynamics of the football transfer market.
* **Out-of-Time Validation:** Successfully tested the model on real-world future transfers (e.g., Antony's 2022 transfer) and non-existent dataset wonders (e.g., Lamine Yamal), proving the model's high accuracy and understanding of market inflation.
* **Interactive Web UI:** A complete Streamlit dashboard for real-time predictions.

## 📊 Model Performance
* **Algorithm:** Random Forest Regressor
* **R-Squared ($R^2$):** 96.80%
* **Mean Absolute Error (MAE):** ~136,000 EUR (Highly accurate for predicting millions in market value).

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Data Manipulation:** pandas, numpy
* **Machine Learning:** scikit-learn
* **Web Framework:** Streamlit
* **Package Management:** uv

## 💻 How to Run Locally

1. **Clone the repository:**
```bash
   git clone [https://github.com/YOUR_USERNAME/football_valuation_project.git](https://github.com/YOUR_USERNAME/football_valuation_project.git)
   cd football_valuation_project

```

2. **Install dependencies:**

```bash
   uv pip install -r requirements.txt

```

3. **Run the Streamlit Web App:**

```bash
   streamlit run app.py

```

## 🧠 Key Learnings

* Tree-based models (Random Forest) do not require feature scaling, unlike distance-based models (Linear Regression).
* Structuring projects using clean code snippets drastically improves development speed and code reusability.

```

---

