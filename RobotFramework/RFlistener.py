import csv


class RFlistener:
    ROBOT_LISTENER_API_VERSION = 2

    # robot --listener RFlistener.py:keyword.csv main.robot

    def __init__(self, csv_keyword="", csv_test=""):
        self.keyword = csv_keyword
        self.test = csv_test

    def end_keyword(self, name, data):
        with open(self.keyword, "a", newline='') as csvfile:
            csvfile.write(data.get("kwname") + "," + str(data.get("elapsedtime")) + "," + data.get("status") + "\n")

    def end_test(self, name, data):
        pass
