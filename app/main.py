import streamlit as st 
from predict import predict_spam

st.title("Spam Classifier")

user_input = st.text_area("Enter your message:")

if st.button("check"):
    if user_input.strip() == "":
        st.warning("Please enter your message")

    else:
        result, proba = predict_spam(user_input)

        if result == "spam":
            st.error(f"Spam ({proba:.2f} confidence)")

        else:
            st.success(f"Not Spam({proba:.2f} confidence)")
