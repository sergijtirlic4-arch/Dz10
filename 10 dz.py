import sqlite3

conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Назва_звіра TEXT,
    Тип_звіра TEXT
)
""")

animals = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
]

cursor.executemany("INSERT INTO Animals (Назва_звіра, Тип_звіра) VALUES (?, ?)", animals)

cursor.execute("""
UPDATE Animals
SET Назва_звіра = 'Сокіл'
WHERE Назва_звіра = 'Орел'
""")

print("Ссавці:")
cursor.execute("SELECT * FROM Animals WHERE Тип_звіра = 'Ссавець'")
for row in cursor.fetchall():
    print(row)

print("\nВсі звірі:")
cursor.execute("SELECT * FROM Animals")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
