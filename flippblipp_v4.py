def flippblipp(n):
    text = ""
    if n % 3 == 0: text += "flipp"    
    if n % 5 == 0:
        if text != "":
            text += " "
        text += "blipp"
    if text == "": return str(n)
    else: return text

print("      ",1)
i = 2
while True:
    svar = input("Nästa: ")
    ans = flippblipp(i)
    if svar != ans:
        print("Fel -",ans,"\n")
        print("Game Over")
        break
    i+=1