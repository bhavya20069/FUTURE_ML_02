# ================================
# Support Ticket Classification & Prioritization
# ================================

# 🔹 Import Libraries
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ================================
# 1. Load Dataset
# ================================
df = pd.read_csv("customer_support_tickets.csv")
df = df[['Ticket Subject', 'Ticket Description', 'Ticket Type', 'Ticket Priority']]

df['text'] = df['Ticket Subject'] + " " + df['Ticket Description']

# Keep only required columns
df = df[['text', 'Ticket Type', 'Ticket Priority']]
df.columns = ['text', 'category', 'priority']
# Remove missing values
df.dropna(inplace=True)


# ================================
# 2. Text Preprocessing
# ================================
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

df['clean_text'] = df['text'].apply(clean_text)


# ================================
# 3. Feature Extraction (TF-IDF)
# ================================
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    stop_words='english'
)

X = vectorizer.fit_transform(df['clean_text'])


# ================================
# 4. Prepare Labels
# ================================
y_category = df['category']
y_priority = df['priority']


# ================================
# 5. Train-Test Split
# ================================
X_train, X_test, y_cat_train, y_cat_test = train_test_split(
    X, y_category, test_size=0.2, random_state=42)

_, _, y_pri_train, y_pri_test = train_test_split(
    X, y_priority, test_size=0.2, random_state=42)


# ================================
# 6. Train Models
# ================================
model_cat = LogisticRegression(max_iter=200)
model_cat.fit(X_train, y_cat_train)

model_pri = LogisticRegression(max_iter=200)
model_pri.fit(X_train, y_pri_train)


# ================================
# 7. Model Evaluation
# ================================
print("\n========== CATEGORY RESULTS ==========")
cat_pred = model_cat.predict(X_test)
print("Accuracy:", accuracy_score(y_cat_test, cat_pred))
print(classification_report(y_cat_test, cat_pred))

print("\n========== PRIORITY RESULTS ==========")
pri_pred = model_pri.predict(X_test)
print("Accuracy:", accuracy_score(y_pri_test, pri_pred))
print(classification_report(y_pri_test, pri_pred))


# ================================
# 8. Prediction Function
# ================================
def predict_ticket(text):
    cleaned = clean_text(text)
    vect = vectorizer.transform([cleaned])

    category = model_cat.predict(vect)[0]
    priority = model_pri.predict(vect)[0]

    return category, priority


# ================================
# 9. Sample Predictions
# ================================
print("\n========== SAMPLE PREDICTIONS ==========")

test_tickets = [
    "My payment failed and money got deducted",
    "Unable to login to my account",
    "I want to cancel my order",
    "App is not working properly",
    "Need refund for my purchase"
]

for ticket in test_tickets:
    cat, pri = predict_ticket(ticket)
    print("\nInput:", ticket)
    print("Predicted Category:", cat)
    print("Predicted Priority:", pri)