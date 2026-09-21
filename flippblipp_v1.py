print("hur många tal? ")
n = int(input())
for i in range(1,n + 1):
    if(i % 3 == 0 and i % 5 == 0):
        print("flippblipp")
    elif(i % 3 == 0):
        print("flipp")
    elif(i % 5 == 0):
        print("blipp")
    else:
        print(i)
