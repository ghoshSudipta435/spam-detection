from flask import Flask, render_template, request, session
import pickle
import string
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from datetime import datetime

nltk.download('stopwords', quiet=True)

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # Change this in production

# Load model and vectorizer
try:
    with open("spam_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("Error: spam_model.pkl not found. Please ensure the model file is in the same directory as app.py")
    raise
except Exception as e:
    print(f"Error loading model: {e}")
    raise

try:
    with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError:
    print("Error: tfidf_vectorizer.pkl not found. Please ensure the vectorizer file is in the same directory as app.py")
    raise
except Exception as e:
    print(f"Error loading vectorizer: {e}")
    raise

# Text preprocessing
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    words = text.split()
    cleaned_words = []
    for word in words:
        word = word.strip(string.punctuation)
        if word not in stop_words and word.isalpha():
            cleaned_words.append(ps.stem(word))
    return " ".join(cleaned_words)

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize message history in session if not exists
    history = session.get('history', [])
    
    prediction_result = None
    
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        
        if message:
            cleaned_message = preprocess_text(message)
            vectorized_message = vectorizer.transform([cleaned_message])
            
            # Get prediction and probability
            result = model.predict(vectorized_message)[0]
            probabilities = model.predict_proba(vectorized_message)[0]
            
            # Calculate confidence (probability of predicted class)
            confidence = probabilities[result] * 100
            is_spam = bool(result == 1)
            
            # Create prediction result dictionary (all values must be JSON serializable)
            prediction_result = {
                'message': message[:100] + "..." if len(message) > 100 else message,  # Truncate for display
                'full_message': message,
                'is_spam': is_spam,
                'confidence': float(round(confidence, 2)),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Add to session history (keep last 10 predictions)
            history = [prediction_result] + history
            history = history[:10]
            session['history'] = history
    
    return render_template("index.html", 
                         prediction=prediction_result,
                         history=history)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
