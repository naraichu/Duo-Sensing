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

# Load JSON datasets
with open(json_path, "rb") as f:
    dataset = json.load(f)

# SFCS values in 2D array
x = np.array([data['sfcs_value'] for data in dataset])
x = x.reshape(-1, 2)

# Action for classification
y = np.array([[data['action'] for _ in range(freq_len + 1)] for data in dataset])
y = y.reshape(-1)

# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Initialize SVM classifier with custom parameters
svm_classifier = SVC(C=0.2, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)

# Train the SVM classifier
svm_classifier.fit(x_train, y_train)

# Save the trained model using pickle
with open(pickle_path, 'wb') as f:
    pickle.dump(svm_classifier, f)

# Predictions
y_pred = svm_classifier.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)






'''
import json
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

# Files path for training data and saving the model
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/ML/datasets.JSON"
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/ML/SVM/SFCS_SVM.pkl"

freq_len = 200

# Load JSON datasets
with open(json_path, "rb") as f:
    dataset = json.load(f)

# SFCS values in 2D array
x = np.array([data['sfcs_value'] for data in dataset])
x = x.reshape(-1, 2)

# Action for classification
y = np.array([[data['action'] for _ in range(freq_len + 1)] for data in dataset])
y = y.reshape(-1)

# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


print(">> Hyperparameter Tuning...")

# Define the parameters grid
param_grid = {'C': [0.1, 1, 10, 100],
              'gamma': [1, 0.1, 0.01, 0.001],
              'kernel': ['rbf'],
              }

# Initialize SVM classifier
svm_classifier = SVC(random_state=42)

# Initialize Grid Search with 5-fold cross-validation
grid_search = GridSearchCV(estimator=svm_classifier, param_grid=param_grid, cv=2, scoring='accuracy', verbose=2)

# Perform Grid Search to find the best parameters
grid_search.fit(x_train, y_train)

# Get the best parameters and estimator
best_params = grid_search.best_params_
best_estimator = grid_search.best_estimator_

print("Best Parameters:", best_params)

# Save the trained model using pickle
with open(pickle_path, 'wb') as f:
    pickle.dump(best_estimator, f)

# Predictions
y_pred = best_estimator.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
'''

'''
Best Parameters: {'C': 100, 'gamma': 1, 'kernel': 'rbf'}
Accuracy: 0.5856826976229962
'''