aktuell_användare = None
aktuell_roll = None
import json, hashlib
from typing import Dict
användare : Dict[str, dict] = {}
anv_fil = 'konton.json'
filnamn = 'bibliotek.json'
boklista = []
tillgänglig = []
utlämnade = []

def ladda_användare():
    import användareFunktion
    try:
        with open(anv_fil, 'r', encoding='utf-8') as fil:
            data = json.load(fil)
        for d in data:
            användareFunktion.användare.från_dict(d)   # din from_dict ska klara detta
    except FileNotFoundError:
        print("Ingen användarfil hittades, börjar med bara admin")     
    except json.JSONDecodeError:
        print("Andvändarfilen verkr vara sönder, börjar med bara admin")
        
    
    finns_admin = any(
    u.användarnamn == 'admin' and u.roll == 'admin'
    for u in användareFunktion.användarlista
    )

    
    if not finns_admin:
        print('skapar admin, då det inte verkar finnas')
        användareFunktion.användare('admin', 'admin_lösen', 'admin')
        try:
            spara_användare()
        except:
            pass


def spara_användare():
    import användareFunktion  # om funktionen inte är i samma modul
    with open(anv_fil, 'w', encoding='utf-8') as fil:
        json.dump(
            [u.till_dict() for u in användareFunktion.användarlista], 
            fil, 
            ensure_ascii=False, 
            indent=2
        )


def ladda_böcker():
    from funktioner import Bok
    boklista.clear() 
    utlämnade.clear()
    tillgänglig.clear()
    try:
        with open(filnamn, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for d in data:
            Bok.från_dict(d)
    except FileNotFoundError:
        print('Filen hittades inte')
    except json.JSONDecodeError:
        print('Filen är trasig/fungerar inte i systemet')

def spara_böcker():    
    from funktioner import Bok
    data = [b.till_dict() for b in boklista]
    with open(filnamn, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

