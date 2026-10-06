from logik import boklista, tillgänglig, utlämnade
import unicodedata, re
from difflib import SequenceMatcher
from funktioner import Bok
def _normalize(s: str) -> str:
    s = s.casefold()
    s = unicodedata.normalize('NFKD', s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9åäö\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def similer(a: str, b : str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def sök_bok(lista = boklista):
    rå = input(f'Vilken bok vill du söka upp? sök antingen på titel, författare eller båda. Skriv "av" mellan titel och författare för bästa resultat')
    if not rå:
        print('Tom sökterm, odern misslyckades')
        return

    q = _normalize(rå)
    kandidater = []

    for bok in lista:
        bok_sträng_titel = _normalize(bok.titel)
        bok_sträng_författare = _normalize(bok.författare)
        likhet = max(similer(bok_sträng_titel, q), similer(bok_sträng_titel, bok_sträng_författare), similer(f'{bok_sträng_titel} av {bok_sträng_författare}', q))
        if likhet > 0.65:
            kandidater.append((likhet, bok))
    if kandidater:
        if len(kandidater) == 1:
            print(f'Denna bok hittades {kandidater[0][1]}')
            return kandidater[0][1]
        else:
            kandidater.sort(key=lambda x: x[0], reverse=True)
            for i, (sc, bok) in enumerate(kandidater, start = 1):
                print(f'{i}. {bok} likheten var {round(sc*100)}%')
            bok_val =int(input('Vilken bok vill du välja?'))
            return kandidater[bok_val - 1][1]
    else:
        print('Ingen bok matchande din sökning hittades')
