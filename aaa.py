import binascii
from tkinter import Tk, filedialog, Label, StringVar, ttk

szukana_wartosc1 = '80 44 00 00 40 44' #ustawienia 640x480
szukana_wartosc2 = '20 44 00 00 F0 43' #ustawienia 800x600
szukana_wartosc3 = '48 44 00 00 16 44' #ustawienia 1024x768

nowa_wartosc1 = '80 44 00 00 10 44' # ustawienia 1024x576
nowa_wartosc2 = 'A0 44 00 00 34 44' # ustawienia 1280x720
nowa_wartosc3 = 'F0 44 00 00 87 44' # ustawienia 1920x1080
nowa_wartosc4 = 'C8 44 00 00 61 44' # ustawienia 1600x900
nowa_wartosc5 = 'AA 44 00 00 40 44' # ustawienia 1360x768
nowa_wartosc6 = 'F0 44 00 00 B4 44' # ustawienia 1920x1440
nowa_wartosc7 = '20 45 00 00 B4 44' # ustawienia 2560x1440
nowa_wartosc8 = '00 B4 44 00 61 44' # ustawienia 1440x900

def interpretuj_wartosc(szukana_wartosc):
    if szukana_wartosc == szukana_wartosc1:
        return '640x480'
    elif szukana_wartosc == szukana_wartosc2:
        return '800x600'
    elif szukana_wartosc == szukana_wartosc3:
        return '1024x768'
    elif szukana_wartosc == nowa_wartosc1:
        return '1024x576'
    elif szukana_wartosc == nowa_wartosc2:
        return '1280x720'
    elif szukana_wartosc == nowa_wartosc3:
        return '1920x1080'
    elif szukana_wartosc == nowa_wartosc4:
        return '1600x900'
    elif szukana_wartosc == nowa_wartosc5:
        return '1360x768'
    elif szukana_wartosc == nowa_wartosc6:
        return '1920x1440'
    elif szukana_wartosc == nowa_wartosc7:
        return '2560x1440'
    elif szukana_wartosc == nowa_wartosc8:
        return '1440x900'
    else:
        return 'Nieznana wartość'

Tk().withdraw()  # Ukryj główne okno Tkinter
nazwa_pliku = filedialog.askopenfilename(title="Wybierz plik do przeszukania", filetypes=[("Wszystkie pliki", "*.*"), ("Pliki binarne", "*.bin;*.dat;*.sav")])

if not nazwa_pliku:
    print("Anulowano wybór pliku.")
    
with open(nazwa_pliku, 'rb') as f:
        file_contents = f.read()


# Konwersja na format szesnastkowy z odstępem co dwie litery
hex_data = ' '.join([binascii.hexlify(file_contents[i:i+1]).decode('utf-8') for i in range(0, len(file_contents), 1)])

#print(hex_data)

def znajdz_sekwencje(nazwa_pliku, szukane_wartosci):
    with open(nazwa_pliku , 'rb') as f:
        file_contents = f.read()
    for szukana_wartosc in szukane_wartosci:
        if szukana_wartosc in hex_data:
            interpretacja = interpretuj_wartosc(szukana_wartosc)
            print(f"Znaleziono sekwencję {interpretacja} w pliku.")
        else:
            continue

#plik_do_przeszukania = "F:/Robin Hood - The Legend of Sherwood/DATA/Savegame/Profiles"

szukane_wartosci = [szukana_wartosc1, szukana_wartosc2, szukana_wartosc3, nowa_wartosc1, nowa_wartosc2, nowa_wartosc3, nowa_wartosc4, nowa_wartosc5, nowa_wartosc6, nowa_wartosc7, nowa_wartosc8]
znajdz_sekwencje(nazwa_pliku, szukane_wartosci)


"""
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
"""