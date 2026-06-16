import sqlite3;
import logging

#ouverture de la connexion



def persist_data(client_data,plan_data,transaction_data):

    insert_dim_client = """
        INSERT OR IGNORE INTO dim_client (id_client,nom,pays) VALUES (?,?,?);
    """
    insert_dim_plan = """
        INSERT OR IGNORE INTO dim_plans (code_plan,prix_base) VALUES (?,?);
    """
    insert_fact_transaction = """
        INSERT OR IGNORE INTO fact_transactions (transaction_id,code_plan,id_client,montant_original,devise_origine,montant_eur,date_transaction)
        VALUES (?,?,?,?,?,?,?);
    """
    try :
        conn = sqlite3.connect("data/database.db")
        cursor = conn.cursor()
        #ouverture du fichier des schemas et creation des tables
        with open("sql/Schema.sql", 'r', encoding='utf-8') as schema:
            sql_schema = schema.read()
            cursor.executescript(sql_schema)
        
        #insertion des donnees
        cursor.executemany(insert_dim_client,client_data)
        cursor.executemany(insert_dim_plan,plan_data)
        cursor.executemany(insert_fact_transaction,transaction_data)
        conn.commit()
        logging.info(f"Insertion dans la base de donnees termine avec succes")
        return None
    except sqlite3.Error  as e :
       logging.warning(f"Echec lors de l'insertion des donnees en base : {e}")
    finally:
        #fermeture de la connexion
        conn.close()
        logging.info(f"Connexion avec la base de donnees ferme avec succes")
    
    return None