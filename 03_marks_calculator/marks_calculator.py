print("===== Marks Calculator =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
ai = float(input("Enter AI marks: "))
english = float(input("Enter English marks: "))
dsa = float(input("Enter DSA marks: "))

total = maths + python + ai + english + dsa
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
