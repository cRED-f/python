# with open("weather-data.csv") as cvs_file_read:
#   data=cvs_file_read.readlines()
#   print(data)
# import csv
#
# with open("weather-data.csv") as cvs_file_read:
#     data=csv.reader(cvs_file_read)
#     temperature=[]
#     for row in data:
#       if row[1]!="temp":
#         temperature.append(int(row[1]))
#     print(temperature)

import pandas

# using panda module to read the csv file
data = pandas.read_csv("weather-data.csv")

# print(data)
# print("this is temperature data:")
# print(data["temp"])
# print("this is day data")
# print(data["day"])


# csv data convert into dictionary
dic = data.to_dict()
print(dic)
# dictionary convert into list
list_data_temp = data["temp"].to_list()
print(list_data_temp)
print(f"length of list data of temp:{len(list_data_temp)}")

# average of temp list
# average_temp_list = sum(list_data_temp) / len(list_data_temp)
# print(f"this is average of temp:{average_temp_list}")


# we can get the average value by using panda
average_temp_list = data["temp"].mean()
print(f"this is average of temp:{average_temp_list}")

# largest value from temp list
largest_temp_list = data["temp"].max()
print(f"the largest value from temp list:{largest_temp_list}")

# get data in row
print("data print in row")
print(data[data["day"] == "Monday"])
print(data[data["day"] == "Saturday"])

# max data in row
# max_data_in_row=data[data["temp"]==data["temp"].max()]
# we can write this way also
max_data_in_row = data[data.temp == data.temp.max()]
print(f"max data in row:\n{max_data_in_row}")

# monday temp convert celsius to farenhite
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
# c-f
converted_farenhite_value = (1.8 * monday_temp) + 32
print(f"\nmonday temp c value convert to f value:{converted_farenhite_value}")

# create dataframe from scratch
data_dic = {
    "students": ["fahim", "jahid", "asif"],
    "score": [90, 92, 93]
}
new_data = pandas.DataFrame(data_dic)
new_data.to_csv("new-data.csv")
print("\n\nnew data:")
print(new_data)

# lowest score from new_data
print("\n")
lowest_data_score = new_data[new_data.score == new_data.score.min()]
print(f"this is new data lowest score:\n{lowest_data_score}")
