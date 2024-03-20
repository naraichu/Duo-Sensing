import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle


# Files path for training data and saving the model
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/ML/traning_data.JSON"
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/Long_strip/long_strip_SVM.pkl"


# Number of frequency sweeping
freq_len   = 200

# Number of actions to be classified
action_num = 6

# Size of data for testing
test_size = 0.6

# Random shuffle
np.random.seed(20)


# Load JSON datasets
with open(json_path, "rb") as f:
    dataset = json.load(f)


# Seperate data into x and y
x = np.array([sample["sfcs_value"] for sample in dataset["long_strip"]])
x = x.reshape((freq_len*action_num),-1)

y = np.array([sample["action"] for sample in dataset["long_strip"]])


# Permutation for 80% / 20% validation
permutation = np.random.permutation(freq_len*action_num)
x = x[permutation]
y = y[permutation]
endpoint = int((freq_len*action_num)*test_size)

x_train = x[:endpoint]
x_test  = x[endpoint:]

y_train = y[:endpoint]
y_test  = y[endpoint:]


# Initialise the SVM classifier
svm_classifier = SVC(C=0.2, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)

# Train the SVM classifier
svm_classifier.fit(x_train, y_train)

# Save the trained model using pickle
with open(pickle_path, 'wb') as f:
    pickle.dump(svm_classifier, f)

# Predictions
y_pred = svm_classifier.predict(x_test)
print("Predicted action : ", y_pred)

# Print accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
