import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Download NLTK stopwords
nltk.download('stopwords')

# Load the dataset
df = pd.read_csv('data/sentimentdataset.csv')  # Update the path as needed
print(df.head())

# Function to clean the text data
def clean_text(text):
    text = re.sub(r'http\\S+|www\\S+|https\\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'@\\w+|#', '', text)  # Remove mentions and hashtags
    text = text.lower()  # Lowercase
    text = re.sub(r'\\d+', '', text)  # Remove numbers
    return text

# Clean the text column
df['cleaned_text'] = df['Text'].apply(clean_text)

# Remove stop words
stop_words = set(stopwords.words('english'))
df['cleaned_text'] = df['cleaned_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# Prepare data for training
X = df['cleaned_text']
y = df['Sentiment']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Model training
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Make predictions
y_pred = model.predict(X_test_counts)

# Print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Classification report
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\\n", cm)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Positive', 'Negative', 'Neutral'], yticklabels=['Positive', 'Negative', 'Neutral'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()

# Summarize results
def summarize_results(y_test, y_pred):
    report = classification_report(y_test, y_pred, output_dict=True)
    return {
        "Positive": report['positive']['support'],
        "Negative": report['negative']['support'],
        "Neutral": report['neutral']['support']
    }

summary = summarize_results(y_test, y_pred)
print("Summary of Sentiment Analysis:\\n", summary)

