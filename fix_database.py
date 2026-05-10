import sqlite3
import os

def check_and_fix_database():
    db_path = 'alicedelice.db'
    
    if not os.path.exists(db_path):
        print("Database not found!")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check current schema
    cursor.execute("PRAGMA table_info(orders)")
    columns = cursor.fetchall()
    print("Current orders table columns:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
    
    # Check if observations column exists
    has_observations = any(col[1] == 'observations' for col in columns)
    
    if not has_observations:
        print("\nAdding 'observations' column...")
        cursor.execute("ALTER TABLE orders ADD COLUMN observations TEXT")
        conn.commit()
        print("Column added successfully!")
    else:
        print("\n'observations' column already exists.")
    
    conn.close()

if __name__ == "__main__":
    check_and_fix_database()
