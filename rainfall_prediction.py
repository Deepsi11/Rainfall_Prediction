# -*- coding: utf-8 -*-
"""RAINFALL_PREDICTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17TLi2Fef2uaQIYMzu4H490K4o1TvbbM2

**PROJECT: RAINFALL PREDICTION ON WEATHER DATASET**

**IMPORTING NEEDED LIBRARIES**
"""

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

"""**UPLOADING THE DATASET**"""

# Uploading The Dataset
df = pd.read_csv("/content/weatherAUS.csv")
df.head()

"""**DATA PREPROCESSING**"""

# Finding the Statistical Measures of the Dataset
df.describe()

# Checking the Dimention of the Dataset
df.shape

# Checking the Data type of the Dataset
df.info()

# Dropping the Less Important Features from the Dataset
df = df.drop(["Evaporation", "Sunshine", "Cloud9am", "Cloud3pm", "Location", "Date"], axis=1)
df.head()

# Removing rows from the Dataset that contains missing values (NaN).
df = df.dropna(axis = 0)
df.shape

# Printing All the Columns from the Dataset
df.columns

"""**LABEL ENCODING**"""

# Using Label Encoding to change the Categorical Values to Numerical Values
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["WindGustDir"] = le.fit_transform(df["WindGustDir"])
df["WindDir9am"] = le.fit_transform(df["WindDir9am"])
df["WindDir3pm"] = le.fit_transform(df["WindDir3pm"])
df["RainToday"] = le.fit_transform(df["RainToday"])
df["RainTomorrow"] = le.fit_transform(df["RainTomorrow"])

# Dropping the column "RainTomorrow" from the Dataset and storing that to new variable called "Y"
X = df.drop(['RainTomorrow'], axis = 1)
Y = df['RainTomorrow']

X.head()

"""**DATA STANDARDIZATION**"""

#This Method Computes the Mean and Standard Deviation of each feature in 'X' and then
# Performs Standardization by Centering and Scaling the features.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit_transform(X)

standardized_data = X
X = standardized_data
Y = df['RainTomorrow']

print(X)
print(Y)

"""**DATA VISUALIZATION**"""

# Displaying the prediction, whether it will rain tomorrow or not through Scatter Plot, considering "MaxTemp" and "MinTemp".
plt.figure(figsize = (8,8))
sns.scatterplot(x = 'MaxTemp', y = 'MinTemp', hue = 'RainTomorrow', palette = 'inferno', data = df)

# Displaying the prediction, whether it will rain tomorrow or not through Scatter Plot, considering "Humidity9am" and "Temp9am".
plt.figure(figsize = (8,8))
sns.scatterplot(x = 'Humidity9am', y = 'Temp9am', hue = 'RainTomorrow', palette = 'inferno', data = df)

"""**HEATMAP**"""

# Displaying the Correlations among dataset through Heatmap, to compute the pairwise correlation between its columns.
corrmat = df.corr()
plt.figure(figsize=(20,20))
g=sns.heatmap(corrmat, annot=True)

"""**TRAIN-TEST-SPLIT**"""

# Splitting the Dataset into Training and Testing Dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

"""**DECISION TREE**"""

# Taining the Model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
model_1 = DecisionTreeClassifier()
model_1.fit(X_train, Y_train)

# Finding the Accuracy score of Training Data
X_train_prediction = model_1.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Finding the Accuracy Score of Testing Data

X_test_prediction = model_1.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# Printing the Confusion Matrix, Classification Report, and Accuray Score
print('Matrix', confusion_matrix(Y_test, X_test_prediction))
print('f1', classification_report(Y_test, X_test_prediction))
print('Accuracy', accuracy_score(Y_test, X_test_prediction))

# Printing the Accuracy of Training Data and Test Data.
print('Accuracy on Training Data : ', training_data_accuracy)
print('Accuracy on Test Data : ', test_data_accuracy)

"""**ARTIFICIAL NEURAL NETWORK**"""

# Training the Model
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
model_2 = MLPClassifier()
model_2.fit(X_train, Y_train)

# Finding the Accuracy score of Training Data
X_train_prediction = model_1.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Finding the Accuracy Score of Testing Data

X_test_prediction = model_1.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# Printing the Confusion Matrix, Classification Report, and Accuray Score
print('Matrix', confusion_matrix(Y_test, X_test_prediction))
print('f1', classification_report(Y_test, X_test_prediction))
print('Accuracy', accuracy_score(Y_test, X_test_prediction))

# Printing the Accuracy of Training Data and Test Data.
print('Accuracy on Training Data : ', training_data_accuracy)
print('Accuracy on Test Data : ' , accuracy_score(Y_test, X_test_prediction))

"""**RANDOM FOREST CLASSIFIER**"""

# Training the Model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
model_3 = DecisionTreeClassifier()
model_3.fit(X_train, Y_train)

# Finding the Accuracy score of Training Data
X_train_prediction = model_1.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Finding the Accuracy Score of Testing Data

X_test_prediction = model_1.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# Printing the Confusion Matrix, Classification Report, and Accuray Score
print('Matrix', confusion_matrix(Y_test, X_test_prediction))
print('f1', classification_report(Y_test, X_test_prediction))
print('Accuracy', accuracy_score(Y_test, X_test_prediction))

# Printing the Accuracy of Training Data and Test Data.
print('Accuracy on Training Data : ', training_data_accuracy)
print('Accuracy on Test Data : ' , accuracy_score(Y_test, X_test_prediction))

"""**XGBOOST CLASSIFIER**"""

# Training the Model
import xgboost as xgb
from sklearn.metrics import accuracy_score
xgb = xgb.XGBClassifier()
xgb.fit(X_train, Y_train)

# Finding the Accuracy score of Training Data
X_train_prediction = model_1.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Finding the Accuracy Score of Testing Data

X_test_prediction = model_1.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# Printing the Confusion Matrix, Classification Report, and Accuray Score
print('Matrix', confusion_matrix(Y_test, X_test_prediction))
print('f1', classification_report(Y_test, X_test_prediction))
print('Accuracy', accuracy_score(Y_test, X_test_prediction))

# Printing the Accuracy of Training Data and Test Data.
print('Accuracy on Training Data : ', training_data_accuracy)
print('Accuracy on Test Data : ' , accuracy_score(Y_test, X_test_prediction))

"""**BUILDING A PREDICTIVE MODEL**"""

input_data = (12.9,25.7,0.0,15,46.0,13,15,19.0,26.0,38.0,30.0,1007.6,1008.7,21.0,23.2,0,0.0)

# Changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)


# Standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = xgb.predict(std_data)
print(prediction)

if (prediction[0]==0):
    print("It will not rain Tomorrow")
else:
    print("It will rain Tomorrow")