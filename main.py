import pandas as pd
import logging
import src.extractor as ex

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
    unique_date = raw_trans["date"].unique()
    #recuperation des taux de changes pour chaque date
    rates = ex.retrieveExchangeRate(unique_date)
    print(rates)

if __name__ == "__main__":
    run_pipeline()