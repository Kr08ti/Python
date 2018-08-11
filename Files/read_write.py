with open("name.txt", mode='w') as f:
    f.write("Name: Krati Jain \n")
    f.write("Age: 26 \n")

with open ("name.txt" , mode='a') as f2:
    f2.write("Gender: Female")

with open ("name.txt" , mode='r') as f1:
    print(f1.read())
    print(f1.name)
    print(f1.mode)



#with open("name.txt") as f1:
#    print(f1.read())


