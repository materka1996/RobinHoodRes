import binascii
import os
import sys
from tkinter import (
    messagebox,
    filedialog,
    Label,
    StringVar,
    Tk,
    ttk,
)

mapowanie_wartosci = {
    '640x480': '804400004044',
    '800x600': '20440000F043',
    '1024x768': '484400001644',
    '1024x576': '804400001044',
    '1280x720': 'A04400003444',
    '1920x1080': 'F04400008744',
    '1600x900': 'C84400006144',
    '1360x768': 'AA4400004044',
    '1920x1440': 'F0440000B444',
    '2560x1440': '20450000B444',
    '1440x900': '00B444006144',
}
messagebox.showinfo("Ważne!", "Drogi Użytkowniku \nProszę wybrać plik Profiles z Data/Savegame/Profiles")
open_file = filedialog.askopenfilename(title="Wybierz plik Profiles z savegames direction", filetypes=[("All file", "*.*"), ("Pliki binarne", "*.bin;*.dat;*.sav")])
if not open_file:
    sys.exit()
def read_file_contents():
    with open(open_file, 'rb') as f:
        file_contents = f.read()

    return binascii.hexlify(file_contents).decode('utf-8')

def write_file_contents(file_path, contents):
    with open(file_path, 'wb') as f:
        f.write(binascii.unhexlify(contents))

root = Tk()
root.geometry("300x200")

combobox = ttk.Combobox(root, values=list(mapowanie_wartosci.keys()))
combobox.pack(pady=20)

label = ttk.Label(root, text="Wybierz nową rozdzielczość i kliknij: Wybierz, a \nnastępnie Zamknij program")
label.pack()
def on_button_click():
    result = read_file_contents().upper()

    selected_value = combobox.get()

    if selected_value in mapowanie_wartosci.keys():
        for key, value in mapowanie_wartosci.items():
            if value in result:
                result = result.replace(value, mapowanie_wartosci[selected_value], 1)
                write_file_contents(open_file, result)
                print(f"Nowa wartość zmiennej result po zamianie {value} na {mapowanie_wartosci[selected_value]}:", result)
                print("Plik został nadpisany.")
                button['state'] = 'disabled'
                messagebox.showinfo("Informacja", "Plik został nadpisany")
    else:
        print(f"Podana wartość {selected_value} nie jest poprawną wartością z mapowania.")
        print(list(mapowanie_wartosci.keys()))

def on_button2_click():
    # Funkcja, która zamyka program
    os._exit(0)

button = ttk.Button(root, text="Wybierz", command=on_button_click)
button.pack()
button2 = ttk.Button(root, text="Zamknij program", command=on_button2_click)
button2.pack()

root.mainloop()
