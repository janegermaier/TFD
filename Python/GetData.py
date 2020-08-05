import csv

def data_from_keyword_RF():
    value_list = []
    time_value_list = [["Open Browser"], ["Start web-browser"], ["Go To"], ['Close Browser'], ['Close web-browser']]
    steptest = ["Open Browser", "Start web-browser", "Go To", 'Close Browser', 'Close web-browser']
    date = []

    with open("../RobotFramework/keyword.csv", "r", newline="") as f:
        for i in f:
            i = i.split(",")
            value_list.append(i)
    print(value_list)

    i = 0
    while i < len(steptest):
        for x in value_list:
            if x[0] == steptest[i]:
                time_value_list[i].append(x[2])

            date.append(x[1][0:7])
        i += 1


    print(time_value_list)
    print(date)


data_from_keyword_RF()