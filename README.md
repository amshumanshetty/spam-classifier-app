# 📧 Spam Email Classifier (AI Web App)

##  Overview

This project is an **AI-powered Spam Email Classifier** that detects whether a message is **Spam or Not Spam** using Natural Language Processing (NLP).

It is built using:

* TF-IDF for text feature extraction
* Naive Bayes for classification
* Streamlit for an interactive web interface

---

##  Features

* Classifies messages as **Spam ** or **Not Spam **
* Displays **confidence score**
* Handles real-time user input
* Clean and simple web interface

---

##  How It Works

1. **Text Preprocessing**

   * Converts text to lowercase
   * Removes special characters
   * Removes stopwords

2. **Feature Extraction**

   * Uses TF-IDF to convert text → numerical vectors

3. **Model Training**

   * Trained using **Multinomial Naive Bayes**

4. **Prediction**

   * Uses probability threshold to classify messages

---

##  Tech Stack

* Python
* scikit-learn
* pandas
* NumPy
* Streamlit

---

##  Model Performance

| Metric           | Value                |
| ---------------- | -------------------- |
| Accuracy         | ~97%                 |
| Precision (Spam) | High                 |
| Recall (Spam)    | Improved with tuning |

---

##  Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/spam-classifier-app.git
cd spam-classifier-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

##  Usage

1. Enter a message in the text box
2. Click **Check Message**
3. View prediction and confidence score

---

##  Project Structure

```
spam-classifier-app/
│
├── app.py              # Streamlit app
├── model.pkl           # Trained Naive Bayes model
├── vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt
└── README.md
```

---

##  Example

Input:

```
Win money now!!! Free offer!!!
```

Output:

```
 Spam Message (Confidence: 0.23)
```

---

##  Future Improvements

* Use deep learning (LSTM / Transformers)
* Improve preprocessing (stemming, lemmatization)
* Add more training data
* Deploy with custom domain

---
