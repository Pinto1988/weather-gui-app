import tkinter as tk
import requests

# Funzione eseguita quando si clicca il bottone
def mostra_meteo():
    città = input_città.get().strip().lower()
    url = f"https://wttr.in/{città}?format=3"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            risultato = response.text
            if "Unknown location" in risultato:
                etichetta_risultato.config(text="❌ Città non trovata.")
            else:
                etichetta_risultato.config(text=risultato)
        else:
            etichetta_risultato.config(text="⚠️ Errore nella richiesta.")
    except:
        etichetta_risultato.config(text="❌ Errore di connessione.")

# Crea la finestra
finestra = tk.Tk()
finestra.title("App Meteo")
finestra.geometry("400x200")

# Etichetta "Inserisci città"
etichetta_input = tk.Label(finestra, text="Inserisci la città:")
etichetta_input.pack()

# Casella di input
input_città = tk.Entry(finestra, font=("Arial", 14))
input_città.pack()

# Bottone
bottone = tk.Button(finestra, text="Mostra meteo", command=mostra_meteo)
bottone.pack(pady=10)

# Etichetta dove verrà stampato il meteo
etichetta_risultato = tk.Label(finestra, text="", font=("Arial", 12))
etichetta_risultato.pack()

# Avvia la finestra
finestra.mainloop()
