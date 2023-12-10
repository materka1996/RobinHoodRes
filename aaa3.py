import binascii
from tkinter import (
    filedialog, 
    Label, 
    StringVar, 
    Tk,
    ttk,
)

mapowanie_wartosci = {
    '80 44 00 00 40 44': '640x480',
    '20 44 00 00 F0 43': '800x600',
    '48 44 00 00 16 44': '1024x768',
    '80 44 00 00 10 44': '1024x576',
    'A0 44 00 00 34 44': '1280x720',
    'F0 44 00 00 87 44': '1920x1080',
    'C8 44 00 00 61 44': '1600x900',
    'AA 44 00 00 40 44': '1360x768',
    'F0 44 00 00 B4 44': '1920x1440',
    '20 45 00 00 B4 44': '2560x1440',
    '00 B4 44 00 61 44': '1440x900',
}
szukane_wartosci = list(mapowanie_wartosci)

Tk().withdraw()  # Ukryj główne okno Tkinter
nazwa_pliku = filedialog.askopenfilename(title="Wybierz plik do przeszukania", filetypes=[("Wszystkie pliki", "*.*"), ("Pliki binarne", "*.bin;*.dat;*.sav")])

if not nazwa_pliku:
    print("Anulowano wybór pliku.")

def znajdz_sekwencje(nazwa_pliku, szukane_wartosci):
    with open(nazwa_pliku , 'rb') as f:
        file_contents = f.read()

    hex_data = ' '.join([binascii.hexlify(file_contents[i:i+1]).decode('utf-8') for i in range(0, len(file_contents), 1)])

    for szukana_wartosc in szukane_wartosci:
        if szukana_wartosc in hex_data:
            print(f"Znaleziono sekwencję {mapowanie_wartosci[szukana_wartosc]} w pliku.")
        else:
            continue

znajdz_sekwencje(nazwa_pliku, szukane_wartosci)


def interpretuj_wartosc(szukana_wartosc):
    return mapowanie_wartosci.get(szukana_wartosc, 'Nieznana wartość')

def znajdz_i_zmien_sekwencje(nazwa_pliku, szukana_sekwencja, nowa_sekwencja_var):
    with open(nazwa_pliku, 'rb') as f:
        file_contents = f.read()

    hex_data = binascii.hexlify(file_contents).decode('utf-8')

    if szukana_sekwencja in hex_data:
        interpretacja = interpretuj_wartosc(szukana_sekwencja)
        print(f"Znaleziono sekwencję '{interpretacja}' w pliku.")

        # Wybór nowej sekwencji przez użytkownika
        nowa_sekwencja = nowa_sekwencja_var.get()
        print(f"Użytkownik wybrał nową sekwencję: {nowa_sekwencja}")

        # Zamień sekwencję
        hex_data = hex_data.replace(szukana_sekwencja, nowa_sekwencja)
        print(f"Zamieniono sekwencję na '{interpretuj_wartosc(nowa_sekwencja)}'.")
        
        # Zapisz zmienione dane do nowego pliku
        nazwa_pliku_docelowego = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Pliki binarne", "*.bin")])
        with open(Profil2, 'wb') as f:
            f.write(binascii.unhexlify(hex_data))
        print(f"Plik z zamienioną sekwencją zapisano jako '{nazwa_pliku_docelowego}'.")
    else:
        print("Nie znaleziono szukanej sekwencji w pliku.")

def utworz_interfejs():
    okno = Tk()
    okno.title("Wybór Nowej Sekwencji")

    Label(okno, text="Wybierz Nową Sekwencję:").pack(pady=10)

    nowa_sekwencja_var = StringVar(okno)
    nowa_sekwencja_var.set(list(mapowanie_wartosci.values())[0])  # Domyślna wartość

    rozwijana_lista = ttk.Combobox(okno, textvariable=nowa_sekwencja_var, values=list(mapowanie_wartosci.values()))
    rozwijana_lista.pack(pady=10)

    przycisk_zmien = ttk.Button(okno, text="Zmień Sekwencję", command=lambda: znajdz_i_zmien_sekwencje(nazwa_pliku, szukane_wartosci, nowa_sekwencja_var))
    przycisk_zmien.pack(pady=10)

    okno.mainloop()

nazwa_pliku = filedialog.askopenfilename(title="Wybierz plik do przeszukania", filetypes=[("Wszystkie pliki", "*.*"), ("Pliki binarne", "*.bin;*.dat;*.sav")])

if not nazwa_pliku:
    print("Anulowano wybór pliku.")
else:
    utworz_interfejs()  
