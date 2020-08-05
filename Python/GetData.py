import csv

def data_from_keyword_RF():
    value_list = []
    with open("../RobotFramework/keyword.csv", "r", newline="") as f:
        for i in f:
            i = i.split(",")
            value_list.append(i)



data_from_keyword_RF()