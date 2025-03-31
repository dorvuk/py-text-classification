# 🧠 Topic Classifier for `.txt` Files

A simple yet effective **Python script** that uses basic machine learning principles to **classify the topic of plain-text files**. Drop in a `.txt` file and let the script predict what it’s about.

---

## ✨ Features

- 📂 Accepts any `.txt` file as input
- 🏷️ Predicts the **topic/category** of the text
- 📊 Uses basic machine learning concepts:
  - Bag of Words / TF-IDF
  - Naive Bayes or Logistic Regression (customizable)
- 🧠 Trained on a small, curated dataset of labeled topics

---

## 🧠 How It Works

1. **Load `.txt` file**
2. **Preprocess**: remove stopwords, punctuation, tokenize, etc.
3. **Vectorize**: convert words to numerical features
4. **Classify**: predict the topic based on trained model
5. **Output**: print or save the prediction
