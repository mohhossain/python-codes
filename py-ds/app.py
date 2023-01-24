from operator import iadd


students = ["Annabelle", "Sarah", "Jack", "Jones"]
print(students[0])

print(students[1:3])  # slice
print(students[-1])  # last index
# also
print(students[len(students) - 1])  # length
print(students[-2:])  # last 2 items
print('Annabelle' in students)  # returns true if Annabelle exists in students
# returns true if Talent doesn't exists in students
print('Talent' not in students)

more_students = ["Mike", "John"]
students += more_students  # adding two lists together

someText = "hello world"
print("(" + min(someText) + ")")  # ascii code


def fib(n):
    fibArr = []

    for i in range(n):
        if i == 0:
            fibArr.append(i)
        elif i == 1:
            fibArr.append(i)
        else:
            fibArr.append(fibArr[i-1] + fibArr[i-2])

    print(fibArr)


fib(9)
