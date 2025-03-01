import pandas

data = pandas.read_csv("file1.txt")
numbers = data.numbers
numbers1 = numbers.to_list()

datas = pandas.read_csv("file2.txt")
number = datas.numbers
numbers2 = number.to_list()

result = [int(n) for n in numbers1 if n in numbers2 ]

print(result)