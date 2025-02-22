dziennik = []
saldo_magazynu = 10000.0
zawartosc_magazynu = [
    {
        "artykuł": "młotek",
        "numer_ID": 1234,
        "ilosc_dostepnych_produktow": 20,
        "cena_produktu": 10.0,
    },
    {
        "artykuł": "kombinerki",
        "numer_ID": 2345,
        "ilosc_dostepnych_produktow": 7,
        "cena_produktu": 15.0,
    },
    {
        "artykuł": "piła",
        "numer_ID": 3456,
        "ilosc_dostepnych_produktow": 10,
        "cena_produktu": 12.0,
    },
    {
        "artykuł": "śrubokręt",
        "numer_ID": 4567,
        "ilosc_dostepnych_produktow": 15,
        "cena_produktu": 7.0,
    }
]
kontynuuj_program = True
print("Witaj w prostym systemie księgowym - mini magazyn")
while kontynuuj_program:
    opcja_uzytkownika = int(input("Wybierz co chcesz zrobić.\n"
                                  "1. Saldo\n"
                                  "2. Sprzedaż\n"
                                  "3. Zakup\n"
                                  "4. Konto\n"
                                  "5. Lista\n"
                                  "6. Magazyn\n"
                                  "7. Przegląd\n"
                                  "8. Koniec programu\n"))
    if opcja_uzytkownika == 1:
        print(f"Saldo magazynu wynosi: {saldo_magazynu}")
        continue
    elif opcja_uzytkownika == 2:
        numer_ID = int(input("Podaj proszę numer ID produktu: "))
        znaleziony_produkt = False
        for produkt in zawartosc_magazynu:
            if produkt.get("numer_ID") == numer_ID:
                znaleziony_produkt = True
                ilosc_zakupow = int(input("Podaj proszę ilość, którą chcesz kupić: "))
                if produkt.get("ilosc_dostepnych_produktow") >= ilosc_zakupow:
                    produkt["ilosc_dostepnych_produktow"] -= ilosc_zakupow
                    saldo_magazynu += produkt.get("cena_produktu") * ilosc_zakupow
                    print(f"Gratulacje, kupiłles {produkt.get('artykuł')}")
                else:
                    if produkt.get("ilosc_dostepnych_produktow") == 0:
                        print("Niestety ten produkt jest niedostępny. Sprawdź później.")
                    else:
                        print(f"Niestety nie mamy wymaganej ilości produktu, dostępna ilość to {produkt.get('ilosc_dostepnych_produktow')}")
                        continue
        if not znaleziony_produkt:
            print("Niestety nie mamy produktu z takim numerem ID")
    elif opcja_uzytkownika == 3:
        artykuł = input("Podaj nazwę artykułu: ")
        numer_ID = input("Podaj numer ID artykułu: ")
        ilosc_zakupionego_towaru = input("Podaj ilość zakupionego towaru: ")
        cena_zakupu = float(input("Podaj koszt jednego artykułu: "))
        cena_sprzedazy = float(input("Podaj cenę sprzedaży artykułu: "))
        zawartosc_magazynu.append({
            "artykuł": artykuł,
            "numer_ID": numer_ID,
            "ilosc_dostepnych_produktow": ilosc_zakupionego_towaru,
            "cena_produktu": cena_sprzedazy,
        })
        dziennik.append(f"Zakup towarów: {ilosc_zakupionego_towaru} szt {artykuł}")
        saldo_magazynu -= ilosc_zakupionego_towaru * cena_zakupu
    elif opcja_uzytkownika == 4:
        print(f"Saldo magazynu wynosi: {saldo_magazynu}")
    elif opcja_uzytkownika == 5:
        print(f"Dane twojego magazynu:")
        for produkt in zawartosc_magazynu:
            print(f"{produkt.get('artykuł')} - {produkt.get('ilosc_dostepnych_produktow')}")

    elif opcja_uzytkownika == 6:
        artykuł = input("Podaj proszę nazwę artkułu: ")
        znaleziony_produkt = False
        for produkt in zawartosc_magazynu:
            if produkt.get("artykuł") == artykuł:
                print(f" nazwa artykułu -{produkt.get('artykuł')}\n ilość - {produkt.get('ilosc_dostepnych_produktow')}\n cena - {produkt.get('cena_produktu')} PLN")
                znaleziony_produkt = True
                break
        if not znaleziony_produkt:
            print("Niestety nie mamy takiego artykułu")
    elif opcja_uzytkownika == 7:
        od = int(input("Podaj poczatkowy zakres historii: "))
        do = int(input("Podaj koncowy zakres historii: "))
        print(dziennik[od:do])
    elif opcja_uzytkownika == 8:
        kontynuuj_program = False
    else:
        print("Niestety nie mamy takiej operacji. ")
print("Kończymy na dzisiaj :)")

