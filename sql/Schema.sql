CREATE TABLE IF NOT EXISTS dim_client(
    id_client INT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    pays VARCHAR(50) NOT NULL,
);

CREATE TABLE IF NOT EXISTS dim_plans(
    code_plan VARCHAR(50) NOT NULL,
    prix_base FLOAT ,
);

CREATE TABLE IF NOT EXISTS fact_transactions(
    transaction_id INTEGER PRIMARY KEY,
    id_client INTEGER, 
    code_plan VARCHAR(50),
    date_transaction DATETIME,
    montant_original FLOAT,
    devise_origine VARCHAR (10),
    montant_eur FLOAT,
    FOREIGN KEY (code_plan) references dim_plans(code_plan),
    FOREIGN KEY (id_client) references dim_client(id_client)
);