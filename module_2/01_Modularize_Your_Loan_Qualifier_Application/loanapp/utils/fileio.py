#importing csv functions
#this module helps define functions for file reading/writing
import csv


#this function loads a CSV file from the filepath defined under 'csvpath'
def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
