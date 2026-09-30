import spelare
spelar_lista = []
spelar_antal = int(input("Antal splare (en siffra)"))

for n in range(1,spelar_antal+1):
    n = str(n)
    inpu = "Namn på spelare " + n
    namn = input(inpu)
    inp = namn + "s valde chans"
    ch = float(input(inp))
    s = spelare.person(namn, ch)
    spelar_lista.append(s)
antal_spel = int(input("Välj antal spel"))
for o in range(1, antal_spel+1):
    print(f'Omgång {o} av {antal_spel}')
    for s in spelar_lista:
        s.ett_spel()

