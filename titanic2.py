import csv as csv
import numpy as np

def load_data():
    # Open up the csv file in to a Python object
    csv_file_object = csv.reader(open('trained_data/train.csv', 'rb'))
    header = csv_file_object.next()  # The next() command just skips the
                                     # first line which is a header
    data=[]                          # Create a variable called 'data'.
    for row in csv_file_object:      # Run through each row in the csv file,
        data.append(row)             # adding each row to the data variable
    data = np.array(data) 	         # Then convert from a list to an array
    			                     # Be aware that each item is currently
                                     # a string in this format
    return data

def normalize_matrix(data):
    normalised_data = data

    np.size(normalised_data[0::,1].astype(np.float))

    return normalised_data

data_matrix = load_data()
matrix_normalised = normalize_matrix(data_matrix)

print matrix_normalised[0]
