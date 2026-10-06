from logik import boklista, tillgänglig, utlämnade
from användareFunktion import användare
import användareFunktion
class Bok:
    next_id= 0
    def __init__(self, titel, författare, *, bok_id=None, lånad=False):
        self.titel = titel
        self.författare = författare
        self.lånad = lånad

        # ID-hantering: om vi inte fått ett id (ny bok) → skapa ett
        if bok_id is None:
            self.bok_id = Bok.next_id
            Bok.next_id += 1
        else:
            # vid inläsning från JSON: använd befintligt id
            self.bok_id = bok_id
            # se till att nästa id alltid blir högre än alla befintliga
            if bok_id >= Bok.next_id:
                Bok.next_id = bok_id + 1

        # lägg in i listorna exakt en gång
        boklista.append(self)
        if self.lånad:
            if self not in utlämnade:
                utlämnade.append(self)
            if self in tillgänglig:
                tillgänglig.remove(self)
        else:
            if self not in tillgänglig:
                tillgänglig.append(self)
            if self in utlämnade:
                utlämnade.remove(self)
       
    def låna_bok(self):
        import logik
        if användareFunktion.aktiv_användare == None:
            print('Du måste vara inloggad för attt låna!')
            return 
        self.lånad = True
        utlämnade.append(self)
        användareFunktion.aktiv_användare.låna_bok(self)
        try:
            tillgänglig.remove(self)
        except:
            pass

    def radera_bok(self):
        try:
            print(f'{self} raderas')
            boklista.remove(self)
            try:
                utlämnade.remove(self)
            except:
                tillgänglig.remove(self)
        except:
            pass

    def lämna_tillbaka_bok(self):
        self.lånad = False
        tillgänglig.append(self)
        användareFunktion.aktiv_användare.lämna_bok(self)
        try:
            utlämnade.remove(self)
        except:
            pass

    def __str__(self):
        status = 'utlånad' if self.lånad else 'Tillgänglig'
        return f'{self.titel} av {self.författare} ({status})'
    
    
    def till_dict(self):
        return  {
            'titel' : self.titel,
            'författare' : self.författare,
            'lånad' : self.lånad,
            'bok_id' : self.bok_id
        }
    @classmethod
    def från_dict(cls, d:dict):
        return cls(
            d['titel'],
            d['författare'],
            bok_id =d.get('bok_id'),
            lånad=d.get('lånad', False),)
            
            