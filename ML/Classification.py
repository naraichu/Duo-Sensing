# Import general libraries
import json
import numpy as np
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
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
size   = 0.3
random = 42

# Load JSON datasets
with open(json_path, "rb") as j:
    dataset = json.load(j)


# Seperate data into x and y
x = np.array([sample["sfcs_value"] for sample in dataset["SFCS_pad"]])
x = x.reshape(step * action_num,-1)     # [[[x0,y0],[x1,y1]...[x200,y200]]...[[x0,y0],[x1,y1]...[x200,y200]]]  --> [[x0,y0,x1,y1...x200,y200]...[x0,y0,x1,y1...x200,y200]]
print(x)

y = np.array([sample["action"] for sample in dataset["SFCS_pad"]])
print(y)
print("\n")


# Splitting the data (Cross-validation)
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
    svm_classifier = SVC(C=0.03, kernel='poly', degree=3, gamma='scale', coef0=0.01, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
    svm_classifier.fit(x_train_scale, y_train)

    SaveModel(SVM_pickle_path, svm_classifier)

    y_pred = svm_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)
    confuse  = confusion_matrix(y_test, y_pred)
    
    print("SVM ACC : ", accuracy)
    print("SVM CON : \n", confuse)
    print("\n")
    return accuracy, confuse


# Logistic Regression
def LR():
    lr_classifier = LogisticRegression(penalty='l2', max_iter=1000)
    lr_classifier.fit(x_train_scale, y_train)
    
    SaveModel(LR_pickle_path, lr_classifier)

    y_pred = lr_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)
    confuse  = confusion_matrix(y_test, y_pred)
    
    print("LR  ACC : ", accuracy)
    print("LR  CON : \n", confuse)
    print("\n")
    return accuracy, confuse


# Naïve Bayes
def NB():
    nb_classifier = naive_bayes.GaussianNB()
    nb_classifier.fit(x_train, y_train)

    SaveModel(NB_pickle_path, nb_classifier)

    y_pred = nb_classifier.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    confuse  = confusion_matrix(y_test, y_pred)

    print("NB  ACC : ", accuracy)
    print("NB  CON : \n", confuse)
    print("\n")
    return accuracy, confuse


# Multilayer perceptron (Neural Network)
def NN():
    nn_classifier = MLPClassifier(solver='adam', alpha=0.05, hidden_layer_sizes=(200,100), max_iter=1000)
    nn_classifier.fit(x_train_scale, y_train)

    SaveModel(NN_pickle_path, nn_classifier)

    y_pred = nn_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)
    confuse  = confusion_matrix(y_test, y_pred)

    print("NN  ACC : ", accuracy)
    print("NN  CON : \n", confuse)
    print("\n")
    return accuracy, confuse


# Random Forest
def RF():
    rf_classifier = RandomForestClassifier(criterion= "log_loss", n_estimators=100, bootstrap=True, max_features='log2')
    rf_classifier.fit(x_train_scale, y_train)

    SaveModel(RF_pickle_path, rf_classifier)

    y_pred = rf_classifier.predict(x_test_scale)
    accuracy = accuracy_score(y_test, y_pred)
    confuse  = confusion_matrix(y_test, y_pred)

    print("RF  ACC : ", accuracy)
    print("RF  CON : \n", confuse)
    print("\n")
    return accuracy, confuse


# Main functions
if __name__ == '__main__':
    # Train, save and test models
    svm_acc, svm_con = SVM()
    lr_acc , lr_con  = LR()
    nb_acc , nb_con  = NB()
    nn_acc , nn_con  = NN()
    rf_acc , rf_con  = RF()
    
    '''
    # Declare bar graphs
    classifiers = ['SVM', 'LR', 'NB', 'NN', 'RF']
    accuracies = [svm_acc, lr_acc, nb_acc, nn_acc, rf_acc]
    colours = ['#31bbc4', '#60d950', '#eb9c1e', '#d64836', '#d1119b']

    # Round to 2 decimal places
    for i in range (0,len(classifiers)):
        accuracies[i] = round(accuracies[i], 2)

    # Initilisation
    fig, ax = plt.subplots()
    ax.bar(classifiers, accuracies, color=colours)

    # Plot bar graphs
    ax.bar(classifiers, accuracies, label= accuracies, color = colours)
    ax.set_xlabel('Classifiers')
    ax.set_ylabel('Accuracy')
    ax.set_title('Training Classification Algorithms Accuracy')
    ax.legend(title='Accuracy')
    ax.set_ylim(0.50, 1.00)  # Set y-axis limits from 0 to 1

    # Show graph
    plt.show()
    '''
    
    fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(9, 6))
    fig.suptitle('Confusion matrix')

    ax[0].set_title('SVM')
    ax[0].imshow(svm_con, interpolation='none', cmap='viridis')
    ax[0].set_aspect('equal')

    ax[1].set_title('LR')
    ax[1].imshow(lr_con , interpolation='none', cmap='viridis')
    ax[1].set_aspect('equal')

    ax[2].set_title('NB')
    ax[2].imshow(nb_con , interpolation='none', cmap='viridis')
    ax[2].set_aspect('equal')

    ax[3].set_title('NN')
    ax[3].imshow(nn_con , interpolation='none', cmap='viridis')
    ax[3].set_aspect('equal')

    ax[4].set_title('RF')
    ax[4].imshow(rf_con , interpolation='none', cmap='viridis')
    ax[4].set_aspect('equal')
    
    #plt.tight_layout()
    
    plt.show()
    

    
