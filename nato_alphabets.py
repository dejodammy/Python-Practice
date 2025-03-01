import random
import pandas
# LIST COMPREHENSION
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

new_number = []
for n in numbers:
    new_number.append(n+1)
print(new_number)

name = "dejo"
split_name = [split for split in name]
print(split_name)

split_names = []
for n in name:
    split_names.append(n)
print(split_names)

double_numbers = [n*2 for n in range(1 , 5)]
print(double_numbers)

double_number = []
for n in range(1,5):
    o = n*2
    double_number.append(o)
print(double_number)

names = ["dejo","felami", "jeffery", "tonias", "tolu","amira","bolu","tobi"]
good_names = [n for n in names if len(n) == 4]
big_names = [n.upper() for n in names if len(n) > 4]

print(good_names)
print(big_names)

# DICTIONARY COMPREHENSION
students_score = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student,score) in students_score.items() if score > 50}
print(students_score)
print(passed_students)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:temp*9/5 + 32 for day,temp in weather_c.items()}

print(weather_f)

students_dictionary = {
    "student": ["dejo","sam","lily"],
    "score" : [99,20,50]
}

student_df = pandas.DataFrame(students_dictionary)
print(student_df)

for (index,row) in student_df.iterrows():
    print(row)



data = pandas.read_csv("nato_alphabet.csv")

nato_letter = data.Letter.to_list()
nato_word = data.Word.to_list()

nato_pair = {letter:word for (letter,word) in zip(nato_letter,nato_word)}

user_name = str(input("Input Username: ")).upper()
splited_name = [s for s in user_name]
nato_spelling = [nato_pair[letter] for letter in splited_name if letter in nato_pair]

print(nato_spelling)





