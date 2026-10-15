import pandas as pd
import sqlite3
from datasets import load_dataset

def create_database(dataset_name, table_name, db_path):
    """
    Downloads a dataset from HuggingFace and converts it into a SQLite database.
    """
    print(f"Loading dataset: {dataset_name}...")
    try:
        ds = load_dataset(dataset_name)
        df = pd.DataFrame(ds['train'])
        
        # Clean column names to be SQL friendly
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        
        # Save to SQLite
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"✅ Database saved at: {db_path}")
    except Exception as e:
        print(f"❌ Error creating database: {e}")

if __name__ == "__main__":
    create_database("Mahadih534/Institutional-Information-of-Bangladesh", "institutions", "databases/institutions.db")
    create_database("Mahadih534/all-bangladeshi-hospitals", "hospitals", "databases/hospitals.db")
    create_database("Mahadih534/Bangladeshi-Restaurant-Data", "restaurants", "databases/restaurants.db")