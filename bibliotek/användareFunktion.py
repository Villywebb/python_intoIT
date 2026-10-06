användarlista = []
aktiv_användare = None
import logik
class användare:
    def __init__(self, användarnamn, lösenord, roll):
        self.användarnamn = användarnamn
        self.lösenord = lösenord
        self.roll = roll
        self.lista = []
        användarlista.append(self)

    def __str__(self):
        return f'{self.användarnamn} roll: {self.roll}'
    
    def låna_bok(self, bok):
        self.lista.append(bok)
        
        print('Alla böcker lånade av {self}')
        for b in self.lista:
            print(b)

    def lämna_bok(self, bok):
        print(f'{bok} lämnas tillbaka av {self}')
        for böcker in self.lista:
            if böcker.titel == bok.titel and böcker.författare == bok.författare:
                self.lista.remove(bok)

    def till_dict(self):
        return {
            "användarnamn": self.användarnamn,
            "lösenord": self.lösenord,     # OBS: klartext, byt till hash senare
            "roll": self.roll,
            "lista": [b.bok_id for b in self.lista]   # sparar bok-ID:n
        }

    @classmethod
    def från_dict(cls, d: dict):
    # Skapa användaren
        u = cls(
            d.get("användarnamn", ""),
            d.get("lösenord", ""),          # klartext just nu
            d.get("roll", "user")
        )

    # Koppla tillbaka bokobjekten
        import logik  # late import för att undvika importcykel
        bokregister = {bok.bok_id: bok for bok in logik.boklista}

        for bok_id in d.get("lista", []):
            b = bokregister.get(bok_id)
            if b is not None:
                u.lista.append(b)
            else:
            # ID saknas – antingen ignorera tyst eller logga
            # print(f"Varning: bok-id {bok_id} saknas i biblioteket.")
                pass

        return u
