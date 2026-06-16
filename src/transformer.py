

def calculateAmountInEur(rates,data):
    """
       cette fonction permet de calculer le montant en euro de chaque transaction 
       en fonction du taux de change du jour. elle prend en param le dict des taux 
       de change et le dataframe et renvoie en retour un dataframe contenant une
       nouvelle colonne 'montant_eur' contenant le montant en euro 
    """
    #on recupere le taux 
    data['rate'] = data.apply(lambda elt: getRate(elt['date'],elt['devise'],rates),axis=1)
    data['montant_eur'] = data['rate'] * data['montant']
    data['montant_eur'] = data['montant_eur'].apply(lambda x: '{:.2f}'.format(x))
    #data = data.drop(["rate"])
    return data.drop(["rate"],axis=1)

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