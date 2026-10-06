import logik
import användareFunktion
from användareFunktion import användare

def logga_in():
    anv = input('Andvändarnamn: ').strip()
    pwd = input('Lösenord: ').strip()

    for user in användareFunktion.användarlista:
        if anv == user.användarnamn:
            if pwd == user.lösenord:
                print(f'inloggad som {user}')
                användareFunktion.aktiv_användare = user
                return
    print('Användare inte hittad')
    
def logga_ut():
    print(f'Du loggar ut från {användareFunktion.aktiv_användare}')
    användareFunktion.aktiv_användare = None

