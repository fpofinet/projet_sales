import pandas as pd

def run_pipeline():
    """pipeline principale"""
    raw_trans = pd.read_csv('data/transactions.csv')
    print(raw_trans.info())

if __name__ == "__main__":
    run_pipeline()