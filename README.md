# Spam Classifier App

A machine learning web application that classifies SMS/text messages as **Spam** or **Not Spam** using TF-IDF vectorization and Logistic Regression.

---

## Features

* Spam detection for user-entered text messages
* Probability/confidence score for predictions
* Interactive web interface built with Streamlit
* Modular project structure for training, inference, and UI
* Saved trained model for fast predictions

---

## Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas
* Joblib

---

## Project Structure

```bash
spam-classifier-app/
│
├── app/
│   ├── main.py
│   └── predict.py
│
├── model/
│   ├── train.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── data/
│   └── spam.csv
│
├── screenshots/
│   └── app-demo.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Model Pipeline

1. Load SMS spam dataset
2. Preprocess text data
3. Convert text to numerical vectors using TF-IDF
4. Train Logistic Regression classifier
5. Save trained model and vectorizer
6. Use Streamlit app for real-time predictions

---

## Installation

```bash
git clone https://github.com/amshumanshetty/spam-classifier-app.git
cd spam-classifier-app
pip install -r requirements.txt
```

---

## Run Locally

```bash
streamlit run app/main.py
```

---

## Example Predictions

| Input Message            | Prediction |
| ------------------------ | ---------- |
| "WIN FREE MONEY NOW!!!"  | Spam       |
| "Hey bro where are you?" | Not Spam   |

---


