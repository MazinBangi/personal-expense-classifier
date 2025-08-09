import streamlit as st
import pandas as pd
import joblib
import re
from nltk.stem import WordNetLemmatizer
import nltk
import matplotlib.pyplot as plt

lemmatizer = WordNetLemmatizer()

# Load model & vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

# Classifier function
def classify_expense(text):
    processed = preprocess_text(text)
    vectorized = vectorizer.transform([processed])
    prediction = model.predict(vectorized)
    return prediction[0]

income_keywords = ["salary", "income", "paycheck", "wages", "bonus", "stipend"]
dining_keywords = ["restaurant", "fried rice", "pizza", "burger", "coffee", "dine", "snack"]

def smart_classifier(text):
    lower_text = text.lower()
    
    # Step 1: Income override
    if any(word in lower_text for word in income_keywords):
        return "Income"
    
    # Step 2: Dining override
    if any(word in lower_text for word in dining_keywords):
        return "Dining"
    
    # Step 3: Fallback to ML model
    return classify_expense(text)

# --- Streamlit App ---
st.title("💰 Personal Expense Classifier")
st.write("Enter your expense and let the model classify it!")

# Initialize session state for history
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Input fields
desc = st.text_input("Expense Description")
amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")

if st.button("Add Expense"):
    if desc and amount > 0:
        category = smart_classifier(desc)
        st.session_state.expenses.append({
            "Description": desc,
            "Amount": amount,
            "Category": category
        })
        st.success(f"Added: {desc} — {category} — ₹{amount}")
    else:
        st.warning("Please enter both a description and an amount.")

# Show expense history
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📜 Expense History")
    st.dataframe(df)

    # Pie chart for spending distribution
    st.subheader("📊 Spending Breakdown")
    category_totals = df.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
