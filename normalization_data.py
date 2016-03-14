import csv
folder = "trained_data/"
filename = "train.csv"

gender = {
    'male' : 0,
    'female': 1
}

data = []

def prepare_data():
    with open(folder + filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            del row['Name']
            #del row['PassengerId']
            if int(row['Pclass']) == 1:
                print row['PassengerId'] + ", " + row['Cabin'] + ", " +row['Fare'] + ", " +row['Ticket']
            # text_row = ', '.join(row)
            # row_items = text_row.split(',')
            # print row_items
            # data.append(text_row)

    #print data

prepare_data()
