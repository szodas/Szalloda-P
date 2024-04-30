from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, tipus="Egyágyas"):
        super().__init__(szobaszam, ar)
        self.tipus = tipus

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, tipus="Kétágyas"):
        super().__init__(szobaszam, ar)
        self.tipus = tipus

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas.szoba.ar
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    def listaz(self):
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

    def listaz_szalloda_szerint(self, szalloda):
        print(f"Foglalások a(z) {szalloda.nev} szállodában:")
        for foglalas in self.foglalasok:
            if foglalas.szoba in szalloda.szobak:
                print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")


# Szállodák, szobák és foglalások létrehozása
szalloda1 = Szalloda("Hotel Python")
szalloda2 = Szalloda("Hotel Object")

szalloda1.add_szoba(EgyagyasSzoba("101", 14999))
szalloda1.add_szoba(EgyagyasSzoba("102", 18999))
szalloda1.add_szoba(KetagyasSzoba("103", 23999))

szalloda2.add_szoba(EgyagyasSzoba("201", 14999))
szalloda2.add_szoba(EgyagyasSzoba("202", 18999))
szalloda2.add_szoba(KetagyasSzoba("203", 23999))

# Foglalások hozzáadása
foglalaskezelo1 = FoglalasKezelo(szalloda1)
foglalaskezelo2 = FoglalasKezelo(szalloda2)

foglalaskezelo1.foglalas("101", datetime(2024, 5, 1))
foglalaskezelo1.foglalas("102", datetime(2024, 5, 2))
foglalaskezelo1.foglalas("103", datetime(2024, 5, 3))

foglalaskezelo2.foglalas("201", datetime(2024, 5, 4))
foglalaskezelo2.foglalas("202", datetime(2024, 5, 5))
foglalaskezelo2.foglalas("203", datetime(2024, 5, 6))

# Felhasználói interfész
while True:
    print("\n1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása szálloda alapján")
    print("4. Kilépés")

    print("\nKészítette: Gyurenka Richárd-X3I5VM")

    valasztas = input("\nVálassz egy műveletet: ")

    if valasztas == "1":
        # Szálloda választás
        print("Válassz szállodát:")
        print("1. Hotel Python")
        print("2. Hotel Object")
        szalloda_valasztas = input("Válassz egy szállodát (1 vagy 2): ")

        
        if szalloda_valasztas == "1":
            foglalas_szalloda = szalloda1
            foglalaskezelo = foglalaskezelo1
            print("Választható szobaszámok:")
            print("101 - Classic egyágyas")
            print("102 - Superior egyágyas")
            print("103 - Classic kétágyas")
        elif szalloda_valasztas == "2":
            foglalas_szalloda = szalloda2
            foglalaskezelo = foglalaskezelo2
            print("Választható szobaszámok:")
            print("201 - Classic egyágyas")
            print("202 - Superior egyágyas")
            print("203 - Classic kétágyas")
        else:
            print("Érvénytelen szálloda választás.")
                

        #szobafoglalása
        
        szobaszam_input = input("Add meg a szobaszámot: ")
        try:
            szobaszam = int(szobaszam_input)
        except ValueError:
            print("Hibás szobaszám formátum.")
            continue

        if szalloda_valasztas == "1" and (100 < szobaszam < 104 or 200 < szobaszam < 204):
            print("Választott szobaszám:", szobaszam)
        elif szalloda_valasztas == "2" and (100 < szobaszam < 104 or 200 < szobaszam < 204):
            print("Választott szobaszám:", szobaszam)
        else:
            print("A hotel nem rendelkezik ilyen számú szobával")
            continue
        
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("A foglalás csak jövőbeli dátumra lehetséges.")
            else:
                szobaszam = str(szobaszam)
                ar = foglalaskezelo.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"A foglalás ára: {ar} Ft/éjszaka")
                else:
                    print("Nincs ilyen szobaszám.")
        except ValueError:
            print("Hibás dátum formátum.")

    elif valasztas == "2":
        #foglalás lemondás
        print("Válassz szállodát a foglalás lemondásához:")
        print("1. Hotel Python")
        print("2. Hotel Object")
        szalloda_valasztas = input("Válassz egy szállodát (1 vagy 2): ")

        if szalloda_valasztas == "1":
            foglalaskezelo1.listaz_szalloda_szerint(szalloda1)
            foglalaskezelo = foglalaskezelo1
        elif szalloda_valasztas == "2":
            foglalaskezelo2.listaz_szalloda_szerint(szalloda2)
            foglalaskezelo = foglalaskezelo2
        else:
            print("Érvénytelen szálloda választás.")
            continue

        foglalas_szobaszam = input("Add meg a foglalt szoba számát: ")
        foglalas_szobaszam = str(foglalas_szobaszam)
        foglalas_datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            foglalas_datum = datetime.strptime(foglalas_datum, "%Y-%m-%d")
            foglalas = None
            for fogl in foglalaskezelo.foglalasok:
                if fogl.szoba.szobaszam == foglalas_szobaszam and fogl.datum == foglalas_datum:
                    foglalas = fogl
                    break
            if foglalas:
                if foglalaskezelo.lemondas(foglalas):
                    print("A foglalás sikeresen lemondva.")
                else:
                    print("Hiba történt a foglalás törlése közben.")
            else:
                print("Nincs ilyen foglalás.")
        except ValueError:
            print("Hibás dátum formátum.")

    elif valasztas == "3":
        #foglalások listázása szálloda szerint
        print("Válassz szállodát a foglalások listázásához:")
        print("1. Hotel Python")
        print("2. Hotel Object")
        szalloda_valasztas = input("Válassz egy szállodát (1 vagy 2): ")

        if szalloda_valasztas == "1":
            foglalaskezelo1.listaz_szalloda_szerint(szalloda1)
        elif szalloda_valasztas == "2":
            foglalaskezelo2.listaz_szalloda_szerint(szalloda2)
        else:
            print("Érvénytelen szálloda választás.")

    elif valasztas == "4":
        #kilépés
        break
    else:
        print("Érvénytelen választás.")
