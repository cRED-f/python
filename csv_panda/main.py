# with open("weather-data.csv") as cvs_file_read:
#   file_read=cvs_file_read.readlines()
#   print(file_read)
# import csv

# with open("weather-data.csv") as cvs_file_read:
#     file_read=csv.reader(cvs_file_read)
#     temperature=[]
#     for row in file_read:
#       if row[1]!="temp":
#         temperature.append(int(row[1]))
#     print(temperature)

import pandas
 
file_read=pandas.read_csv("weather-data.csv")
print(file_read)