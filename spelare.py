import random
class person:
    def __init__(self, namn, chans):
        self.namn = namn
        self.poäng = 0
        self.chans = 0.8
        self.vald_chans = chans

    def ett_spel(self):
        self.chans = self.vald_chans
        print(f'{self.namn}s tur')
        träffade = []
        mål = [1, 2, 3, 4, 5]

        for antal_skott in range(0, 5):
            träffade = self.skot(träffade, mål, antal_skott)
            self.chans -= 0.07
        oträffade = [x for x in mål if x not in träffade]
        print(f'Du träffade  {self.tavla(oträffade, mål)}')
        self.poäng += len(träffade)
        print(f'De blir {len(träffade)} till, alltså är din totalsumma {self.poäng} poäng')

    def skot(self, hit, target, antal_skott):
        oträffade = [x for x in target if x not in hit]
        sträng_träffyta = self.tavla(oträffade, target)
        print(f'Detta är ditt {antal_skott} skott')
        print(f'Tavlan ser ut såhär\n{sträng_träffyta}\nDär 1 är träffade och noll är oträffade')
        sikte = int(input("Vilket mål 1-5 vill du skjuta (1-5 i siffror)")) -1
        if target[sikte] in oträffade:
            print(self.chans)
            chans = random.random()
            if chans < self.chans:
                hit.append(target[sikte])
        return hit

    def tavla(self, oträffade, target):
        sträng_träffyta = ""
        for n in target:
                    if n in oträffade:
                        sträng_träffyta += "0  "
                    else:
                        sträng_träffyta += "1  "
        return sträng_träffyta


