💰 Personal Expense Classifier



This is a Streamlit-based web application that classifies your personal transactions into predefined categories using a Machine Learning model.



The app takes a transaction description (e.g., "Bought pizza", "Salary credited") and predicts which category it belongs to, such as Essentials, Dining, Entertainment, or Income.

It also includes smart keyword matching to improve accuracy for common entries and displays a visual breakdown of spending.



⚙️ How It Works



1. Preprocessing – The entered description is cleaned (lowercased, special characters removed) and lemmatized using NLTK.



2\. Smart Keyword Matching – Common patterns like "salary" or "fried rice" are instantly matched to categories.



3\. ML Classification – If no keyword is found, the description is passed to a trained scikit-learn model for prediction.



4\. Visualization – A pie chart is generated to show spending distribution across categories.



5\. Session State – All transactions entered during the session are stored and displayed in a history table.



🚀 Run Locally



Follow these steps to set up and run the project on your local machine:



1. Create a Virtual Environment

&nbsp;  python -m venv venv



2\. Activate the Virtual Environment

&nbsp;  venv\\Scripts\\activate



3\. Install Dependencies

&nbsp;  pip install -r requirements.txt



4\. Download NLTK Data (One-Time Setup)

&nbsp;  python download\_nltk\_data.py



5\. Run the Streamlit App

&nbsp;  streamlit run app.py



6\. Interact with the App

&nbsp;  Enter a transaction description and amount.

&nbsp;  The model predicts the category.

&nbsp;  View expense history and a pie chart of spending.

