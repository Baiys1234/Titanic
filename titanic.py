import csv
import numpy as np
from sklearn import linear_model

folder = "trained_data/"
filename = "train.csv"

gender = {
    'male' : 0,
    'female': 1
}

port = {
    '' : 0,
    'S': 0,
    'C': 1,
    'Q': 2
}

removeKey = [
    'Name',
    'Fare',
    'Ticket',
    'PassengerId'
]

def prepare_data():
    data = []
    with open(folder + filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            for key in removeKey:
                del row[key]

            row['Sex'] = gender[row['Sex']]
            row['Embarked'] = port[row['Embarked']]
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
            row.append(data_row[key])
        data_matrix.append(row)
    return data_matrix


    #
    # for data_row in data:
    #     # row = []
    #     row = []
    #     for key in row:
    #         col.append(key)
    #
    #
    #     print key
    #     rpw[]

data = prepare_data()
matrix = remove_data_keys(data)

clf = linear_model.LinearRegression()
clf.fit(matrix);

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
# >>> clf.coef_
# array([ 0.5,  0.5])
