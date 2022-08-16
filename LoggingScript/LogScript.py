"""
Script for logging test data to run file
"""

# import stuff
from datetime import datetime
import csv


# class to handle all file logging operations
class LogFile:
    def __init__(self, f_id, cols):
        self.f_id = f_id
        self.f_name = None
        self.start_time = None
        self.file = None
        self.file_writer = None
        self.cols = cols

    def create_log(self):
        # create logging file to write to
        self.start_time = datetime.now()
        time_now = self.start_time.strftime("%m-%d-%Y_%H-%M-%S")

        # set file name as time _glog
        self.f_name = self.f_id + '_' + str(time_now) + '_gl.csv'
        self.file = open(self.f_name, "w", newline='')

        # consider with to prevent closing issues...
        self.file_writer = csv.writer(self.file, delimiter=',')

        # write to first row with col_names
        self.file_writer.writerow(self.cols)

    def log(self, data):
        # write to file log

        # insert elapsed time into array...
        t_now = datetime.now()
        td = t_now - self.start_time
        td = td.total_seconds()
        data.insert(0, td)

        # write to file
        self.file_writer.writerow(data)

    def close_log(self):
        # close file...
        self.file.close()


# example on creating, logging and closing file
def log_ex():
    lf = LogFile('test', ['et', 'inc'])
    lf.create_log()

    for x in range(100):
        lf.log([x])

    lf.close_log()

# end

