import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

acc = linear.score(x_test, y_test)

print("Your Model Accuracy is: ", acc)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print("Predicted Grade: ", round(predictions[x], 2), " \nActual Grade: ", y_test[x])
