# 📩 SMS Spam Detection using Machine Learning

## 🔍 Overview
This project is an end-to-end Machine Learning application that classifies SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques and a Naive Bayes classifier.

The trained model is deployed using **Flask** to provide real-time predictions through a web interface.

---

## 🚀 Features
- Text preprocessing using NLP techniques
- Feature extraction using TF-IDF
- Spam classification using Naive Bayes
- Model serialization using Pickle
- Real-time prediction using Flask web app

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- NLTK
- Scikit-learn
- Flask
- HTML

---

## 📊 Dataset
- **SMS Spam Collection Dataset**
- Total Messages: 5,574
- Labels: Spam / Ham

---

## 🧠 Machine Learning Pipeline
1. Data Cleaning & EDA
2. Text Preprocessing (Tokenization, Stopwords, Stemming)
3. Feature Extraction using TF-IDF
4. Model Training (Naive Bayes, Logistic Regression)
5. Model Evaluation & Selection
6. Model Serialization
7. Deployment using Flask

---

## 📈 Model Performance
- Naive Bayes Accuracy: ~97%
- Spam Precision: 100%

---

## ▶️ How to Run the Project
```bash
pip install -r requirements.txt
python app.py


Then open:

http://127.0.0.1:5000/


🔮 Future Improvements
Use Lemmatization instead of Stemming
Add deep learning models (LSTM, BERT)
Improve UI
Deploy on cloud (AWS / Render)



# SMS Spam Detection using Machine Learning

**Author:** Sudipta Ghosh  
**Degree:** B.E. in Computer Science & Engineering  
**University:** Jadavpur University  
**Year:** 2025  

---



---

# 📄 2. ATS-OPTIMIZED RESUME POINTS (USE THESE)

### 🔹 Project: SMS Spam Detection using ML

- Built an end-to-end SMS spam detection system using **NLP and Machine Learning**
- Performed text preprocessing including **tokenization, stopword removal, and stemming**
- Applied **TF-IDF vectorization** for feature extraction from text data
- Trained and compared **Naive Bayes and Logistic Regression** models
- Achieved **97% accuracy with 100% spam precision** using Naive Bayes
- Deployed the trained model using **Flask** for real-time prediction
- Serialized the ML model and vectorizer using **Pickle** for production inference

💡 **Tip:** Put this under **Projects** section.

---

# 🎤 3. 20 INTERVIEW QUESTIONS WITH ANSWERS

### 1. What type of problem is spam detection?
**Binary classification using supervised learning and NLP.**

---

### 2. Why is text preprocessing required?
**ML models need numerical input; preprocessing removes noise and standardizes text.**

---

### 3. Why did you use TF-IDF?
**It captures word importance by penalizing common words and highlighting rare ones.**

---

### 4. Why Naive Bayes for spam detection?
**It works well with high-dimensional sparse text data and is computationally efficient.**

---

### 5. Why precision is more important than recall here?
**Because marking genuine messages as spam is more harmful than missing spam.**

---

### 6. What is class imbalance?
**When one class has significantly more samples than the other.**

---

### 7. How did you handle class imbalance?
**By focusing on precision and recall instead of accuracy alone.**

---

### 8. Difference between TF and TF-IDF?
**TF counts word frequency; TF-IDF also considers word rarity across documents.**

---

### 9. What is stemming?
**Reducing words to their root form (e.g., winning → win).**

---

### 10. Why save the vectorizer?
**To ensure the same feature space during inference as training.**

---

### 11. Why use Flask?
**Lightweight framework ideal for ML model deployment.**

---

### 12. What happens if vectorizer changes?
**Model predictions become incorrect due to feature mismatch.**

---

### 13. What is a sparse matrix?
**A matrix with mostly zero values, common in text data.**

---

### 14. How does Naive Bayes work?
**Uses Bayes’ theorem with conditional independence assumption.**

---

### 15. Why Logistic Regression was not selected?
**Naive Bayes provided higher spam precision in this dataset.**

---

### 16. How do you avoid overfitting?
**Feature limiting, proper train-test split, and simple models.**

---

### 17. Can this model work on emails?
**Yes, with retraining on email-specific data.**

---

### 18. What are false positives?
**Ham messages incorrectly classified as spam.**

---

### 19. How can you improve this project?
**Using lemmatization, deep learning models, and cloud deployment.**

---

### 20. How would this scale in production?
**Using APIs, batch inference, and cloud-based deployment.**

---

# 🏁 FINAL STATUS

✅ ML concepts  
✅ NLP pipeline  
✅ Deployment  
✅ Resume  
✅ Interview ready  

🎯 **You can confidently explain this project in interviews for 5–10 minutes.**

If you want next:
- Mock interview (HR + Tech)
- GitHub README beautification
- Cloud deployment (AWS / Render)

Just say **what you want next** 👌


