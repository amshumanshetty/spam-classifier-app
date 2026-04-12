import joblib
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_spam(text):
    vec = vectorizer.transform([text])

    prob = model.predict_proba(vec)[0][1]

    if prob>0.5:
        return "spam", prob

    else:
        return "not spam", prob


text = "Hey how are you"
print(predict_spam(text))
