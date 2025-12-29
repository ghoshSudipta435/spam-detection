from flask import Flask, render_template, request
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

app = Flask(__name__)

# Load model and vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

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
    prediction = ""
    if request.method == "POST":
        message = request.form["message"]
        print("User input:", message)   # 👈 debug
        cleaned_message = preprocess_text(message)
        vectorized_message = vectorizer.transform([cleaned_message])
        result = model.predict(vectorized_message)[0]
        prediction = "Spam 🚫" if result == 1 else "Not Spam ✅"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
