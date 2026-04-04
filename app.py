import streamlit as st
import pickle 

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.title("Spam Email Classifier")
st.write("Enter a message below to check if it's Spam or Not Spam")

message = st.text_area("Enter your message:")

if st.button("Check"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:    
        msg_vec = vectorizer.transform([message])
        prediction = model.predict(msg_vec)[0]
        probability = model.predict_proba(msg_vec)[0][1]

        if probability > 0.2:
            st.error(f"🚨 Spam (Confidence: {probability:.2f})")
        else:
            st.success(f"✅ Not Spam (Confidence: {1 - probability:.2f})")