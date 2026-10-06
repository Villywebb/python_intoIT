from logik import boklista, tillgänglig, utlämnade
from sök import sök_bok
import kontohantering

def kräver_roll(*roller):
    import användareFunktion
    def dekoratör(func):
        def wrapper(*args, **kwargs):
            if användareFunktion.aktiv_användare.roll not in roller:
                print(f'Åtkoms nekad, kräver roll: {roller}')
                return
            return func(*args, **kwargs)
        return wrapper
    return dekoratör

def låna_bok():
    if tillgänglig:
        for i, bok in enumerate(tillgänglig, start = 1):
            print(f'{i}. {bok}')
        try:
            låna = input('Skriv siffran på den bok du vill låna, eller sök om du vill söka upp boken')
            if låna.lower() == 'sök':
                bok = sök_bok(tillgänglig)
                bok.låna_bok()
                if bok is None:
                    print('Ingen träff.')
                    return
            else:
                låna = int(låna)
                tillgänglig[låna - 1].låna_bok()
        except:
            print(f'Vänligen skriv bokens nummer, alernativt annat ordermisslyckande. Orden gick inte igenom')
    else:
        print(f'Finns inga böcker att hämta')

def lämna_tillbaka_bok():
    import användareFunktion
    if utlämnade:
        for i, bok in enumerate(användareFunktion.aktiv_användare.lista, start = 1):
            print(f'{i}. {bok}')
        try:
            lämna = input('Skriv siffran på den bok du vill lämna tillbaka, eler ök om du vill söka upp boken')
            if lämna.lower() == 'sök':
                bok = sök_bok(utlämnade)
                bok.lämna_tillbaka_bok()
            else:
                lämna = int(lämna)
                utlämnade[lämna- 1].lämna_tillbaka_bok()
        except:
            print(f'Vänligen skriv siffran boken har, orden gick inte igenom')
    else:
        print(f'finns inga böcker utlämnade')
@kräver_roll('admin')
def radera_bok():
    if not boklista:
        print('Det finns inga böcker att radera.')
        return
    for i, bok in enumerate(boklista, start = 1):
        print(f'{i}. {bok}')
    try:
        radera = input('Skriv siffran på den bok du vill radera eller sök om du vill söka upp en bok')
        if radera.lower() == 'sök':
            bok = sök_bok()
            bok.radera_bok()
        else:
            radera = int(radera)
            print(f'{boklista[radera - 1]} raderas')
            boklista[radera - 1].radera_bok()
    except:
        print(f'vänligen skriv en siffra som har en bok. Om du sökte, kontrollera att du stavade rätt')
                     
        
def visa_bibliotek():
    import användareFunktion
    if not boklista:
        print("Inga böcker i biblioteket.")
        return
    for i, bok in enumerate(boklista, start=1):
        if bok.lånad == True:
            for användare in användareFunktion.användarlista:
                for b in användare.lista:
                    if b.titel == bok.titel and b.författare == bok.författare:
                        print(f'{i} {bok} lånad av {användare}')
        else:
            print(f'{i} {bok}')


@kräver_roll('admin')
def lägg_till_bok():
    titel = input("Titel: ").strip()
    författare = input("Författare: ").strip()
    if not titel or not författare:
        print("Titel/författare får inte vara tomt.")
        return
    from funktioner import Bok
    ny = Bok(titel, författare, lånad = False)
    tillgänglig.append(ny)
    print("Bok tillagd!")

def mina_böcker():
    from användareFunktion import aktiv_användare
    for b in aktiv_användare.lista:
        print(b)

def skapa_andvändare():
    import logik
    from användareFunktion import användare
    import användareFunktion
    anv = input('Andvändarnamn')
    for user in användareFunktion.användarlista:
        if user.användarnamn == anv:
            print('användarnamn upptaget')
            return
    lös = input('Lösenord:')
    lös1 = input('Bekräfta lösenord')
    if lös1 != lös:
        print('lösenorden matchade inte')
        return
    roll = 'gäst'
    try:
        if användareFunktion.aktiv_användare.roll == 'admin':
            ny= input('Skriv ja om du vill att nya rollen ska vara admin')
            if ny == 'ja':
                roll = 'admin'
    except:
        pass
    nya = användare(anv, lös, roll)
    print(nya)
    #logik.spara_användare()

def visa_användaruppgifter():
    import användareFunktion
    for användare in användareFunktion.användarlista:
        if användare.roll == 'gäst':
            print(f'Användarnamn: {användare.användarnamn}\n Lösenord {användare.lösenord}')