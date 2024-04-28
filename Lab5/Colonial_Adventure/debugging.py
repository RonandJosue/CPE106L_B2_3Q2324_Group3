import sqlite3

conn = sqlite3.connect('/home/vboxuser/LocalRepo/G3Labs/CPE106L_B2_3Q2324_Group3/Lab5/Colonial_Adventure/ColonialAdv.db') #path to the db file

cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM Renter")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("Error executing SQLite query:", e)

finally:
    cursor.close()
    conn.close()
