from collections import deque

class DQ:
    def __init__(self, data_name):
        self.data_name = data_name
        self.que = deque


import csv
import time


with open("csvlog.csv", 'w') as log_file:
    logwriter = csv.writer(log_file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    logwriter.writerow(["Init grey's beast logger"])

    # initialize logging data stuff
    d1 = deque
    d2 = deque
    d3 = deque
    ds = [d1, d2, d3]

    for i in range(5):
        logwriter.writerow([i, i+1, i+2])
        print("log")
        time.sleep(.5)
