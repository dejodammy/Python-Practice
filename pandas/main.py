import csv
import pandas

#  READ CSV
data = pandas.read_csv("pandas\weather_data.csv")

# FIND MEAN , MODE, MEDIAN , MAX
temprature = data.temp
mean = temprature.mean()
median = temprature.median()
mode  = temprature.mode()
max = temprature.max()

print(f"The mean temprature is: {mean}\nThe median temprature is: {median}\nThe mode temprature is: {int(mode.iloc[0])} \nthe max temprature is: {max}")

# Turn data to list, dictionary 
print(temprature.to_list())
print(temprature.to_dict())

#PRINT COLUMN
print(data.temp)
print(data["temp"])

# PRINT ROW
print(data[data.day == "Monday"])
print(data[data.temp == max])

# FIND A VALUE IN A ROW 
monday = data[data.day == "Monday"]
print(monday.condition)

# FIND VALUE AND CONVERT IT 
celsius = monday.temp
fahrenhite = celsius * 1.8 + 32
print(f"The temperature on Monday was {int(fahrenhite.iloc[0])} Fahrenheit")


#  HOW TO CREATE A DATA FRAME

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

# SQUIRELL DATA
squirell_data = pandas.read_csv("pandas\squirrel.csv")
grey_color = len(squirell_data[squirell_data["Primary Fur Color"] == "Gray"])
red_color = len(squirell_data[squirell_data["Primary Fur Color"] == "Cinnamon"])
black_color = len(squirell_data[squirell_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : [ "Gray", "Red", "Black"],
    "Number" : [grey_color,red_color,black_color]
}

df = pandas.DataFrame(data_dict)
df.to_csv("count.csv")