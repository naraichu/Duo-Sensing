import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

# Files path for training data and saving the model
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/ML/datasets.JSON"
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/ML/SVM/SFCS_SVM.pkl"

freq_len = 200

# Load dataset from JSON
with open(json_path, 'r') as f:
    dataset = json.load(f)

# Extract features and labels from the dataset
x = np.arange(freq_len + 1, dtype=int)
y = np.array([data['sfcs_value'] for data in dataset])

# Map the label names to integers
label_mapping = {'None': 0, 'One finger': 1, 'Two fingers': 2, 'Three fingers': 3}  # Update this mapping according to your dataset
y = np.array([label_mapping[label] for label in y])

# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Train SVM with polynomial kernel (degree=3 is default)
svm_classifier = SVC(kernel='poly', C=2.0, degree=3, coef0=1.0, random_state=42)
svm_classifier.fit(x_train, y_train)

# Save the trained model using pickle
with open(pickle_path, 'wb') as f:
    pickle.dump(svm_classifier, f)

# Predictions
y_pred = svm_classifier.predict(x_test)

# Reverse map the predicted integers to label names
reverse_label_mapping = {v: k for k, v in label_mapping.items()}
y_pred_labels = np.array([reverse_label_mapping[label] for label in y_pred])

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Output the predicted labels
print("Predicted labels:", y_pred_labels)
