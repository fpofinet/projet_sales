import csv
import random
from datetime import datetime, timedelta

def generate_transactions(filename="data/transactions.csv", num_rows=200):
    # Données de référence pour les dimensions
    clients = [
        {"id": "CLT01", "nom": "Alice Dupont", "pays": "France", "devise": "EUR"},
        {"id": "CLT02", "nom": "Bob Smith", "pays": "USA", "devise": "USD"},
        {"id": "CLT03", "nom": "Charlie Brown", "pays": "UK", "devise": "GBP"},
        {"id": "CLT04", "nom": "Diana Prince", "pays": "Canada", "devise": "CAD"},
        {"id": "CLT05", "nom": "Emi Sato", "pays": "Japan", "devise": "JPY"},
        {"id": "CLT06", "nom": "Fabien Morel", "pays": "France", "devise": "EUR"},
        {"id": "CLT07", "nom": "George Costanza", "pays": "USA", "devise": "USD"}
    ]
    
    plans = [
        {"code": "PLAN_BASIC", "prix_base": 29.99},
        {"code": "PLAN_PRO", "prix_base": 99.99},
        {"code": "PLAN_PREMIUM", "prix_base": 199.99}
    ]

    # Génération des dates (sur les 10 derniers jours)
    today = datetime(2026, 6, 15) # Basé sur la date actuelle
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 11)]

    # Création du fichier CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # En-têtes du CSV
        writer.writerow(["transaction_id", "client_id", "client_nom", "client_pays", "plan_code", "date", "montant", "devise"])

        for i in range(1, num_rows + 1):
            transaction_id = f"TXN{1000 + i}"
            client = random.choice(clients)
            plan = random.choice(plans)
            date_txn = random.choice(dates)
            
            # On simule un montant avec une petite variation selon la devise pour plus de réalisme
            variation = random.uniform(0.9, 1.1)
            montant_brut = plan["prix_base"] * variation
            
            # Ajustement grossier pour le Yen (qui n'a pas de centimes et une valeur très différente)
            if client["devise"] == "JPY":
                montant_brut = montant_brut * 160 
            
            montant_final = round(montant_brut, 2)

            writer.writerow([
                transaction_id, 
                client["id"], 
                client["nom"], 
                client["pays"], 
                plan["code"], 
                date_txn, 
                montant_final, 
                client["devise"]
            ])

    print(f"Succès : Le fichier '{filename}' a été généré avec {num_rows} lignes.")

if __name__ == "__main__":
    generate_transactions()