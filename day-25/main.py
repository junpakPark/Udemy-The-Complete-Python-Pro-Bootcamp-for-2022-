# with open("weather_data.csv") as file:
#     data = file.readlines()

# print(data)
# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))

# print(temp)
import pandas

# data = pandas.read_csv("weather_data.csv")

# # Data to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Data to List
# temp_list = data["temp"].to_list()
# print(temp_list)

# # Data apply
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(max(data["temp"]))
# print(data["temp"].max())

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# # Get Data in Row and apply
# monday = data[data.day == "Monday"]


# def f(c):
#     return (c * 9 / 5) + 32


# print(monday.temp.apply(f))


# # Create a dataframe from scratch
# data_dic = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dic)
# data.to_csv("student_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_list = data["Primary Fur Color"].to_list()
color_list = list(set(data_list))
count = []

for i in range(len(color_list)):
    count.append(len(data[data["Primary Fur Color"] == color_list[i]]))

print(count)

data_dic = {
    "Fur Color": color_list,
    "Count": count
}

data = pandas.DataFrame(data_dic)
data.to_csv("squirrel_count.csv")
