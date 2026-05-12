#Program to calculate total marks, average percentage and grade based on subject marks.
name = input("Enter student name: ")

subjects = []
marks = []

n = int(input("How many subjects? "))

for i in range(n):
    sub = input("Enter subject name: ")
    mark = int(input("Enter marks: "))
    subjects.append(sub)
    marks.append(mark)

total = sum(marks)
avg=total/n
if avg>80:
	print("A grade")
elif avg>75:
	print("B grade")
elif avg>60:
	print("C grade")
else:
	print("Fail")
print(name)
print(total)
print(avg)
