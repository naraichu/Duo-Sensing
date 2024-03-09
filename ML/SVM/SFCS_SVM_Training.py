import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

# Files path for training data and saving the model
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year_3/CM30082_Individual_Project/Software/Duo_Tactile_Software/ML/datasets.JSON"
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year_3/CM30082_Individual_Project/Software/Duo_Tactile_Software/ML/SVM/SFCS_SVM.pkl"


# Load dataset from JSON
with open(json_path, 'r') as f:
    dataset = json.load(f)

# Extract features and labels from the dataset
X = np.array([data['sfcs_value'] for data in dataset])
y = np.array([data['action'] for data in dataset])

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train SVM with polynomial kernel (degree=3 is default)
svm_classifier = SVC(kernel='poly', C=2.0, degree=3, coef0=1.0, random_state=42)
svm_classifier.fit(X_train, y_train)

# Save the trained model using pickle
with open(pickle_path, 'wb') as f:
    pickle.dump(svm_classifier, f)

# Predictions
y_pred = svm_classifier.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
