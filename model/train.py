import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/spam.csv",encoding='latin-1')
df = df[["spamORham", "Message"]]
df.columns = ["label","message"]

X = df["message"]
y= df["label"]

print(df.head())

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec,y)

joblib.dump(model,"model/model.pkl")
joblib.dump(vectorizer,"model/vectorizer.pkl")

print("Succesful")