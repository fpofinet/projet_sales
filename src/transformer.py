import logging

def format(data):
    """cette fonction permet de formatter les donnees pour les rendres pret 
       a l'insertion en base de donnees
    """
    clients=list()
    plans=list()
    transactions=list()
    try:
        for row in data.itertuples():
            clients.append((row.client_id,row.client_nom,row.client_pays))
            plans.append((row.plan_code,row.montant))
            transactions.append((row.transaction_id,row.plan_code,row.client_id,float(row.montant),row.devise,float(row.montant_eur),row.date))
            #on renvoie un tuple contenant les listes
        
        logging.info(f"Formattage du dataframe en tuple contenant les listes d'insertion pour chaque table")
        return(clients,plans,transactions)
    except Exception as e :
        logging.warning(f"Echec lors de la transformation du dataframe en list : {e}")
    
   

def calculateAmountInEur(rates,data):
    """
       cette fonction permet de calculer le montant en euro de chaque transaction 
       en fonction du taux de change du jour. elle prend en param le dict des taux 
       de change et le dataframe et renvoie en retour un dataframe contenant une
       nouvelle colonne 'montant_eur' contenant le montant en euro 
    """
    try:
        #on recupere le taux 
        data['rate'] = data.apply(lambda elt: getRate(elt['date'],elt['devise'],rates),axis=1)
        data['montant_eur'] = data['rate'] * data['montant']
        data['montant_eur'] = data['montant_eur'].apply(lambda x: '{:.2f}'.format(x))
        #data = data.drop(["rate"])
        return data.drop(["rate"],axis=1)
    except Exception as e:
        logging.warning(f"Echec lors du calcule des montants en euro : {e}")

def getRate(date,devise,rates):
    """
       cette fonction permet de recuperer le taux de change en fonction
       du jour et de la devise
    """
    for rate in rates[date]:
        if rate['quote'] == devise:
            return rate['rate']
        elif rate['base'] == devise:   
            #si la device est egale a la devise de base
            return 1
    
    return 0