import pandas as pd
import os


CSV_FILE = 'data/data.csv'

def read_csv():
    """Reads the CSV file and returns a pandas Dataframe."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=['id','nome','cognome','codice_fiscale'])
        df.to_csv(CSV_FILE, index = False)
    return pd.read_csv(CSV_FILE)

def write_csv(df):
    """Writes the pandas Dataframe to csv file."""
    df.to_csv(CSV_FILE, index=False)

