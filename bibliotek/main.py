
val = ''
from logik import spara_böcker, ladda_böcker, ladda_användare, spara_användare
from meny import (visa_bibliotek,
    lägg_till_bok,
    låna_bok,
    lämna_tillbaka_bok,
    radera_bok,
    sök_bok,
    mina_böcker,
    skapa_andvändare,
    visa_användaruppgifter)
from kontohantering import logga_in, logga_ut
import användareFunktion
ladda_böcker()
ladda_användare()
avsluta = False
print('Hej och välkommna')
while avsluta == False:
    if användareFunktion.aktiv_användare == None:
        val = input('1. logga in \n 2. skapa andvändare')
        if val == '1':
            logga_in()
        elif val == '2':
            skapa_andvändare()
    elif användareFunktion.aktiv_användare.roll == 'gäst':
        val = input('1. Låna bok \n 2.Lämna tillbaka bok \n 3. Sök bok \n 4. Visa mina böcker \n 5. logga ut \n 6. avsluta')
        if val == '1':
            låna_bok()
        elif val == '2':
            lämna_tillbaka_bok()
        elif val == '3':
            sök_bok()
        elif val == '4':
            mina_böcker()
        elif val == '5':
            logga_ut()
        elif val == '6':
            avsluta = True
            print('Programmet avslutas, ändringar sparas')
            spara_användare()
            spara_böcker()
        else: 
            print('Vänligen skriv en siffra 1 - 5')
    elif användareFunktion.aktiv_användare.roll == 'admin':
        val = input('1. lägg till bok \n 2. visa biblotek \n 3. radera bok \n 4. sök bok \n 5. Skapa ny andvändare \n 6. Visa användaruppgifter \n 7. logga ut \n 8. avsluta')
        if val =='1':
            lägg_till_bok()
        elif val == '2': 
            visa_bibliotek()
        elif val == '3':
            radera_bok()
        elif val=='4':
            print(sök_bok())
        elif val == '7':
            logga_ut()
        elif val == '5':
            skapa_andvändare()
        elif val == '6':
            visa_användaruppgifter()
        elif val == '8':
            avsluta = True
            spara_böcker()
            spara_användare()
            print(f'Programmet avslutas, och böckerna sparas')
        else:
            print(f'Vänligen välj en siffra 1-11')
