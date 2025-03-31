import re
import math

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def tokenize(text):
    return re.findall(r'\w+', text.lower())

def build_model(training_data):
    word_counts = {}
    total_words = 0

    for text in training_data:
        tokens = tokenize(text)
        for token in tokens:
            if token in word_counts:
                word_counts[token] += 1
            else:
                word_counts[token] = 1
            total_words += 1

    # zaglađivanje
    vocabulary_size = len(word_counts)
    model = {word: (count + 1) / (total_words + vocabulary_size) for word, count in word_counts.items()}
    model['<UNK>'] = 1 / (total_words + vocabulary_size)  # vjerojatnost za nepoznate riječi

    return model

def classify_text(text, models):
    tokens = tokenize(text)
    scores = {}

    for label, model in models.items():
        score = 0
        for token in tokens:
            score += math.log(model.get(token, model['<UNK>']))
        scores[label] = score

    return max(scores, key=scores.get)

