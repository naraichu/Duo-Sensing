# Import general libraries
import json
import numpy as np
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 


# Import models libraries
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn import naive_bayes
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier



# Files path for training data and saving the models
json_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/dataset_SFCS_Pad.JSON"

SVM_pickle_path = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/SVM_SFCS_Pad.pkl"
LR_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/LR_SFCS_Pad.pkl"
NB_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/NB_SFCS_Pad.pkl"
NN_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/NN_SFCS_Pad.pkl"
RF_pickle_path  = "C:/Users/acer/OneDrive - University of Bath/Subjects/Year 3/CM30082 Individual Project/Software/Duo_Tactile_Software/Use_cases/SFCS_Pad/RF_SFCS_Pad.pkl"


# Number of frequency sweeping
freq_len   = 200

# Number of actions to be classified
action_num = 5

# Number of step for data in each action
step = 200

# Spliting parameters
size   = 0.2
random = 42

# Load JSON datasets
with open(json_path, "rb") as j:
    dataset = json.load(j)


# Seperate data into x and y
x = np.array([sample["sfcs_value"] for sample in dataset["SFCS_pad"]])
x = x.reshape(freq_len * action_num,-1)     # [[[x0,y0],[x1,y1]...[x200,y200]]...[[x0,y0],[x1,y1]...[x200,y200]]]  --> [[x0,y0,x1,y1...x200,y200]...[x0,y0,x1,y1...x200,y200]]
print(x)

y = np.array([sample["action"] for sample in dataset["SFCS_pad"]])
print(y)
print("\n")


# Splitting the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=size, random_state=random)


# Scaling x datasets
scaler = StandardScaler()
x_train_scale = scaler.fit_transform(x_train)
x_test_scale  = scaler.transform(x_test)


# Save model using Pickle
def SaveModel(path, model):
    with open(path, 'wb') as f:
        pickle.dump(model, f)
        f.close()
    print(">> Model saved")


# Support Vector Machine
def SVM():
    svm_classifier = SVC(C=0.05, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
    svm_classifier.fit(x_train_scale, y_train)

    SaveModel(SVM_pickle_path, svm_classifier)

    y_pred = svm_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)
    
    print("SVM : ", accuracy)
    print("\n")
    return accuracy


# Logistic Regression
def LR():
    lr_classifier = LogisticRegression(penalty='l2', max_iter=1000)
    lr_classifier.fit(x_train_scale, y_train)
    
    SaveModel(LR_pickle_path, lr_classifier)

    y_lr_pred = lr_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_lr_pred)
    
    print("LR  : ", accuracy)
    print("\n")
    return accuracy


# Naïve Bayes
def NB():
    nb_classifier = naive_bayes.GaussianNB()
    nb_classifier.fit(x_train, y_train)

    SaveModel(NB_pickle_path, nb_classifier)

    y_pred = nb_classifier.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("NB  : ", accuracy)
    print("\n")
    return accuracy


# Multilayer perceptron (Neural Network)
def NN():
    nn_classifier = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(200,10), max_iter=1000)
    nn_classifier.fit(x_train_scale, y_train)

    SaveModel(NN_pickle_path, nn_classifier)

    y_pred = nn_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)

    print("NN  : ", accuracy)
    print("\n")
    return accuracy


# Random Forest
def RF():
    rf_classifier = RandomForestClassifier(n_estimators=20)
    rf_classifier.fit(x_train_scale, y_train)

    SaveModel(RF_pickle_path, rf_classifier)

    y_pred = rf_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)

    print("RF  : ", accuracy)
    print("\n")
    return accuracy


# Main functions
if __name__ == '__main__':
    
    # Train, save and test models
    svm_acc = round(SVM(), 2)
    lr_acc  = round(LR() , 2)
    nb_acc  = round(NB() , 2)
    nn_acc  = round(NN() , 2)
    rf_acc  = round(RF() , 2)

    # Initilised bar chart
    fig, ax = plt.subplots()
    
    # Declare bar graphs
    classifiers = ['SVM', 'LR', 'NB', 'NN', 'RF']
    accuracies = [svm_acc, lr_acc, nb_acc, nn_acc, rf_acc]
    colours = ['#31bbc4', '#60d950', '#eb9c1e', '#d64836', '#d1119b']

    # Plot bar graphs
    ax.bar(classifiers, accuracies, label= accuracies, color = colours)
    ax.set_xlabel('Classifiers')
    ax.set_ylabel('Accuracy')
    ax.set_title('Classification Algorithms Accuracy')
    ax.legend(title='Accuracy')
    ax.set_ylim(0.30, 1.00)  # Set y-axis limits from 0 to 1

    # Show graph
    plt.show()

    
