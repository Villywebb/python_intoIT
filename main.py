import spelare
spelar_lista = []
spelar_antal = int(input("Antal splare (en siffra)"))

for n in range(1,spelar_antal+1):
    n = str(n)
    inpu = "Namn på spelare " + n
    namn = input(inpu)
    inp = namn + "s valde chans"
    import hjälp_funktioner
    ch = hjälp_funktioner.välj_sifrra(inp,0,1,False)
    s = spelare.person(namn, ch)
    spelar_lista.append(s)
antal_spel = hjälp_funktioner.välj_sifrra("Välj antal omgångar", 1, float("inf"), True)
for o in range(1, antal_spel+1):
    print(f'Omgång {o} av {antal_spel}')
    for s in spelar_lista:
        s.ett_spel()
for p in spelar_lista:
    print("Resultat")
    spelar_lista.sort(key = lambda s: s.poäng, reverse=True)
    for nummer, p in enumerate(spelar_lista, start = 1):
        print(f'{nummer}. {p.namn} ----  {p.poäng} poäng')

