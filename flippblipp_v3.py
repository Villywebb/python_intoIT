def flippblipp(n):
    if(n % 3 == 0 and n % 5 == 0):
        return "flipp blipp"
    elif(n % 3 == 0):
        return "flipp"
    elif(n % 5 == 0):
        return "blipp"
    else:
        return str(n)


n = 5
print(1)
i = 2
while True:
    print("Nästa: ", end = "")
    answer = flippblipp(i)
    if str(input()) != answer:
        print("Fel - " + answer)
        print()
        print("Game Over")
        break
    i = i + 1