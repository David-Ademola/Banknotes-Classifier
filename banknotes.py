import csv
import os

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

# Read data in from file
file_path = os.path.join(os.getcwd(), 'banknotes.csv')

with open(file_path, newline='') as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

# Separate data into training and testing groups
evidence = [dictionary["evidence"] for dictionary in data]
labels = [dictionary["label"] for dictionary in data]

x_training, x_testing, y_training, y_testing = train_test_split(evidence, labels, test_size=0.4)

# Fit model
model.fit(x_training, y_training)

# Make predictions on the testing set
predictions = model.predict(x_testing)

# Compute how well we performed
correct = (y_testing == predictions).sum()
incorrect = (y_testing != predictions).sum()
total = len(predictions)

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")