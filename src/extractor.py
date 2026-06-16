import requests
import logging


def retrieveExchangeRate(dates):
    """Cette fonction nous permet de recuperer les taux de changes
        d'une date. elle renvoie un dictionnaire avec pour chaque 
        date la liste des taux de change
    """

    rates = dict()
    for date in dates:
        try :
            response = requests.get(url=f"https://api.frankfurter.dev/v2/rates?date={date}")
            response.raise_for_status()
            logging.info(f"Recuperation des taux pour la date {date}")
            rates[date]=response.json()
        except requests.exceptions.RequestException as e:
            logging.warning(f"Echec de recuperation des taux pour la date {date} : {e}")
            return None
    
    return rates
