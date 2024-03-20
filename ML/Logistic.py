import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Random shuffle
np.random.seed(20)

# Files path for training data and saving the model
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/ML/traning_data.JSON"
pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/Long_strip/long_strip_SVM.pkl"

freq_len   = 200
action_num = 6


# Load JSON datasets
with open(json_path, "rb") as f:
    dataset = json.load(f)


# Seperate data into x and y
x = np.array([sample["sfcs_value"] for sample in dataset["long_strip"]])
x = x.reshape((freq_len*action_num),-1)

y = np.array([sample["action"] for sample in dataset["long_strip"]])

# Permutation for 80% 20% validation
permutation = np.random.permutation(freq_len*action_num)
x = x[permutation]
y = y[permutation]
endpoint = int((freq_len*action_num)*0.8)

x_train = x[:endpoint]
x_test = x[endpoint:]

y_train = y[:endpoint]
y_test = y[endpoint:]


lr_classifier = LogisticRegression()
lr_classifier.fit(x_train, y_train)

y_pred = lr_classifier.predict(x_test)
print(y_pred)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)




