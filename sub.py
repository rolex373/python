print("enter your mark")
tam = (input("Enter marks for tam: "))
eng = (input("Enter marks for eng: "))
maths = (input("Enter marks for maths: "))
data = (input("Enter marks for data: "))
dbms = (input("Enter marks for dbms: "))
tam=int(tam)
eng=int(eng)
maths=int(maths)
data=int(data)
dbms=int(dbms)

total = tam + eng + maths + data + dbms
print("Total Marks:",total)
