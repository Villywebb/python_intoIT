def välj_sifrra(inp, lägsta, högsta, inte: bool):
    while True:
        try:
            c = float((input(inp)))
            if lägsta<=c<=högsta:
                if inte:
                    ch= int(c)
                else:
                    ch = float(c)
                return ch
            else: 
                print(f'Skriv en siffra mellan {lägsta} och {högsta}')
                continue
        except ValueError, TypeError:
            print("Vänligen skriv en siffra")