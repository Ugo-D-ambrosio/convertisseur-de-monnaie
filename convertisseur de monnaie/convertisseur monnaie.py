from forex_python.converter import CurrencyRates

def convertisseur_de_monnaie(montant, devise_origine, devise_destination):
    c = CurrencyRates()

    try:
        taux = c.get_rate(devise_origine, devise_destination)
        montant_converti = montant * taux
        return montant_converti
    except:
        return "Erreur lors de la conversion. Vérifiez les devises sélectionnées."

try:
    montant = float(input( 100))
except ValueError:
    print("Veuillez entrer un montant valide.")
    exit()

devise_origine = input( "USD").upper()
devise_destination = input("EUR").upper()

resultat = convertisseur_de_monnaie(montant, devise_origine, devise_destination)

if isinstance(resultat, float):
    print(f"{montant} {devise_origine} équivaut à {resultat:.2f} {devise_destination}")
else:
    print(resultat)
