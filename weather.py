import requests

# Chiedi all’utente la città
city = input("Inserisci il nome della città: ")

# Costruisci l’URL per wttr.in
url = f"https://wttr.in/{city}?format=3"

# Prova a mandare la richiesta
try:
    response = requests.get(url)

    # Se tutto va bene (codice 200)
    if response.status_code == 200:
        print("\n☀️ Risultato meteo:")
        print(response.text)
    else:
        print("⚠️ Errore nel recuperare i dati.")
except:
    print("❌ Connessione fallita.")
