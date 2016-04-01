import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

folder = "trained_data/"
filename = "train.csv"

gender_to_number = {
    'male' : 0,
    'female': 1
}

port_to_number = {
    '' : 0,
    'S': 0,
    'C': 1,
    'Q': 2
}

keys_to_remove = [
    'Name',
    'Fare',
    'Ticket',
    'PassengerId'
]

def normalize_data():
    data = []
    with open(folder + filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            for key in keys_to_remove:
                del row[key]

            row['Sex'] = gender_to_number[row['Sex']]
            row['Embarked'] = port_to_number[row['Embarked']]
            row['Age'] = 0 if row['Age'] == "" else float(row['Age'])
            row['Parch'] = 0 if row['Parch'] == "" else int(row['Parch'])
            row['Pclass'] = 3 if row['Pclass'] == "" else int(row['Pclass'])
            row['Survived'] = int(row['Survived'])
            row['SibSp'] = 0 if row['SibSp'] == "" else int(row['SibSp'])
            row['Cabin'] = 0 if row['Cabin'] == "" else 1

            data.append(row)

    return data

def remove_data_keys(data):
    data_matrix = []

    for data_row in data:
        row = []
        for key in data_row:
            print key
            row.append(data_row[key])
        data_matrix.append(row)
    return data_matrix

data = normalize_data()
matrix = remove_data_keys(data)

####################################################

#
# X = matrix[:, :8]
# print X

survived = []

for row in matrix:
    survived.append(row[5])

print survived
#
# # # import some data to play with
# # iris = datasets.load_iris()
# # X = iris.data[:, :2]  # we only take the first two features.
# # X = matrix
# # # Y = iris.target
#
# h = .02  # step size in the mesh
#
# logreg = linear_model.LogisticRegression(C=1e5)
#
# # we create an instance of Neighbours Classifier and fit the data.
# logreg.fit(X, Y)
#
# # Plot the decision boundary. For that, we will assign a color to each
# # point in the mesh [x_min, m_max]x[y_min, y_max].
# x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
# y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])
#
# # Put the result into a color plot
# Z = Z.reshape(xx.shape)
# plt.figure(1, figsize=(4, 3))
# plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
#
# # Plot also the training points
# plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
#
# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())
# plt.xticks(())
# plt.yticks(())
#
# plt.show()
