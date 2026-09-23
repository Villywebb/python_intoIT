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
    print("Nästa: ",end = "")
    ans = flippblipp(i)
    if input() != ans:
        print("Fel -",ans,"\n")
        print("Game Over")
        break
    i+=1