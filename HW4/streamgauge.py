import numpy as np
import matplotlib.pyplot as plt

def read_guage_file(fid):
    """
    Read USGS Guage data and convert date and time to minutes since start

    parameters
    fid (str): path to data

    returns
    timestamp (list): minutes since September first 
    hgt (np.array): guage height in feet
    """
    date, time, hgt = np.loadtxt(fid, skiprows=28, usecols=[2,3,5], 
                                    dtype=str).T

    hgt = hgt.astype(float)
    days = [float(d[-2:]) for d in date]  # get DD from YYYY-MM-DD
    hours = [float(t.split(":")[0]) for t in time]  # get HH from HH:MM
    mins = [float(t.split(":")[1]) for t in time]  # get MM from HH:MM

    timestamps = []
    for d, h, m in zip(days, hours, mins):
        timestamp = (d * 24 * 60) + (h * 60) + m
        timestamps.append(timestamp)

    return timestamps, hgt

# if __name__ == "__main__":
#     df = read_guage_file('phelan_creek_stream_guage_2024-09-07_to_2024-09-14.txt')
#     timestamp = df[0]
#     hgt = df[1]
#     plt.plot(timestamp, hgt, color='blue', linestyle='-')
#     plt.xlabel("Timestamp (minutes since September first)")
#     plt.ylabel("Gauge height (feet)")
#     plt.show()

class StreamGauge():
    """
    StreamGauge class reads USGS Gauge data reports, analyzes the data, and plots it
    """

    # function to __init__ constructor to create attributes
    def __init__(self, fid, station_id, station_name, starttime):
        self.fid = fid
        self.station_id = station_id
        self.station_name = station_name
        self.starttime = starttime
        self.time = []
        self.data = []
        self.units = 'ft'
    
    # function to read dataset provided and extract usable timestamps and gauge height data
    def read_gauge_file(self):
            date, time, hgt = np.loadtxt(self.fid, skiprows=28, usecols=[2,3,5], 
                                    dtype=str).T

            hgt = hgt.astype(float)
            days = [float(d[-2:]) for d in date]  # get DD from YYYY-MM-DD
            hours = [float(t.split(":")[0]) for t in time]  # get HH from HH:MM
            mins = [float(t.split(":")[1]) for t in time]  # get MM from HH:MM

            timestamps = []
            for d, h, m in zip(days, hours, mins):
                timestamp = (d * 24 * 60) + (h * 60) + m
                timestamps.append(timestamp)

            self.time = timestamps
            self.data = hgt

            return self.time, self.data
         
    # function to plot gauge height vs. time 
    def plot(self):
        plt.plot(self.time, self.data, color='blue', linestyle='-')
        plt.xlabel("Time (minutes since start of month)")
        plt.ylabel("Gauge height" + " " + self.units)
        plt.title("Stream Gauge" + " " + self.station_id + " " + self.station_name + " " + str(np.max(self.data)) + " " + self.units)
        plt.show()

    # function to convert data from ft to m
    def convert(self):
        self.data = self.data * 0.3048
        self.units = 'm'
        return self.data, self.units
    
    # function that subtracts the mean value of the data array from the data array
    def demean(self):
        mean = np.mean(self.data)
        self.data = np.subtract(self.data, mean)
        return self.data

    # function that offsets the time axis by user-selected offset
    def shift_time(self, offset):
        self.time = np.add(offset, self.time)
        return self.time
    
    # function that pulls together an ordered list of functions to run when called
    def main (self):
        self.read_gauge_file()
        self.plot()
        self.convert()
        self.demean()
        self.shift_time(-100)
        self.plot()

class NOAAStreamGauge(StreamGauge):
    """
    NOAAStreamGauge class - inherits from StreamGauge
    """
    
    # run StreamGauge's init function and overwrite StreamGauge's units
    def __init__(self, fid, station_id, station_name, starttime):
        super().__init__(fid, station_id, station_name, starttime)
        self.units = 'm'
    
    # remove convert function because StreamGauge.convert is written to convert from ft to m and this data is already in m
    def convert(self):
        pass
    
    # run StreamGauge's read_gauge_file and after that print a statement 
    def read_gauge_file(self):
        super().read_gauge_file()
        print("I am a NOAA stream gauge")

# #Test the StreamGauge class
# if __name__ == "__main__":
#     fid = "phelan_creek_stream_guage_2024-09-07_to_2024-09-14.txt"
#     sg = StreamGauge(fid=fid, station_id="15478040", 
#                      station_name="PHELAN CREEK", starttime="2024-09-07 00:00")
#     assert(len(sg.data) == 0)  # check that we haven't read data yet
    
#     sg.read_gauge_file()
#     assert(len(sg.time) == len(sg.data))  # check that data and time are equal

#     sg.plot()

# #Implement the StreamGauge class, while specifying functions to run
# if __name__ == "__main__":
#     fid = "phelan_creek_stream_guage_2024-09-07_to_2024-09-14.txt"
#     sg = StreamGauge(fid, "15478040", "PHELAN CREEK", "2024-09-07 00:00")  
#     sg.read_gauge_file()   
#     sg.plot()   

#     sg.convert()   
#     sg.demean()   
#     sg.shift_time(-1000)
#     sg.plot()   


# #Implement multiple files to run through the StreamGauge class
# if __name__ == "__main__":
#     files = [
#         "phelan_creek_stream_guage_2024-09-07_to_2024-09-14.txt",
#         "phelan_creek_stream_guage_2024-10-07_to_2024-10-14.txt"
#     ]
    
#     for fid in files:
#         sg = StreamGauge(fid, "15478040", "PHELAN CREEK", "2024-09-07 00:00")
#         sg.main()

# Implement multiple files to run through the NOAAStreamGauge class
if __name__ == "__main__":
    files = [
         "phelan_creek_stream_guage_2024-09-07_to_2024-09-14.txt",
         "phelan_creek_stream_guage_2024-10-07_to_2024-10-14.txt"
    ]
    
    for fid in files:
        sg = NOAAStreamGauge(fid, "15478040", "PHELAN CREEK", "2024-09-07 00:00")
        sg.main()       
         



