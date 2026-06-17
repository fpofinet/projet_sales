import pandas as pd
import logging
import src.extractor as ex
import src.transformer as tr
import src.loader as ld

# Configuration des logs (écriture dans un fichier + affichage console)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

def run_pipeline():
    """pipeline principale"""

    raw_trans = pd.read_csv('data/transactions.csv')
    logging.info("Lecture du fichier des transactions")
    # extraction des dates uniques et recuperation des taux de changes pour chaque date
    unique_date = raw_trans["date"].unique()
    rates = ex.retrieveExchangeRate(unique_date)
    #on creer la colonne avec le montant en euro
    transformed = tr.calculateAmountInEur(rates=rates,data=raw_trans)
    #on recuperer les listes pres pour l'insertion dans chaque table
    clients,plans,trans=tr.format(transformed)
    #on persist les donnees en base de donnees
    ld.persist_data(clients,plans,trans)

    print("####################### ==> FIN DU SCRIPT")
    

if __name__ == "__main__":
    run_pipeline()