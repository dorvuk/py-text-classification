from funkcije import load_text, build_model, classify_text

# učitavanje datoteka
categories = ['informatika', 'muzika', 'paleontologija']
training_data = {category: load_text(f'{category}-training.txt') for category in categories}
test_data = {category: load_text(f'{category}-test.txt') for category in categories}

# treniranje modela
models = {category: build_model([" ".join(training_data[category])]) for category in categories}

# klasificiranje podskupova
correct_predictions = 0
total_predictions = 0

for category, rows in test_data.items():
    podskup = 1
    print(f'\n**Rezultati za {category}-test.txt:**')
    for row in rows:
        predicted_category = classify_text(row, models)
        total_predictions += 1
        if predicted_category == category:
            correct_predictions += 1
        print(f'Podskup {podskup}: Tema: {category}, Predviđeno: {predicted_category}')
        podskup += 1

# izračun točnosti
accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
print(f'\n**Točnost modela nad svim podskupovima:** {accuracy:.4f}')