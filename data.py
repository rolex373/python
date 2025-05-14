def get_mark(subject):
    while True:
        try:
            mark = int(input(f"Enter marks for {subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("" \
                "Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("Enter your marks (0–100):")
tam = get_mark("Tamil")
eng = get_mark("English")
maths = get_mark("Maths")
data = get_mark("Data Science")
dbms = get_mark("DBMS")
total = tam + eng + maths + data + dbms
subjects = [tam, eng, maths, data, dbms]
if all(mark >= 35 for mark in subjects):
    result = "Pass"
else:
    result = "Fail"
print("Total Marks:", total)
print("Result:", result)