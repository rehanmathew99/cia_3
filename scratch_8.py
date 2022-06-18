def data():
    f = open("data.txt", "a")
    li=[name,phone_num,email]
    f.write(li)
    f.close()
i=0
while i==0:
    name=str(input("Enter Name "))
    phone_num=int(input("Enter Phone Number "))
    email=str(input("Enter Email ID "))
    i=int(input("to continue press 0 and to exit press any other value"))
f = open("data.txt", "r")
print(f.read())
f.close()
print("rehan_cia3")
