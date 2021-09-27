import csv
import numpy as np


def getDataSource(data_path):
    size_of_tv = []
    Average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            Average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return {"x" : size_of_tv, "y": Average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of Tv and Average time spent watching Tv in a week :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Size of TV,	Average time spent watching TV in a week (hours).csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
