n = 40
for i in range(1,n+1):
    text = ""
    if i % 3 == 0: text += "flipp "    
    if i % 5 == 0: text += "blipp"
    if text == "": print(i)
    else: print(text)