import random
import sqlite3

# --- CONEXIÓN BASE DE DATOS ---
conexion = sqlite3.connect("puntuaciones.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS historial (
        nombre TEXT,
        intentos INTEGER
    )
""")
conexion.commit()

# --- EL JUEGO ---
print("\n--- 🐳 ADIVINA EL NÚMERO (VERSIÓN DOCKER) 🐳 ---")
nombre = input("Jugador, ¿cuál es tu nombre?: ")
secreto = random.randint(1, 10)
intentos = 0
gano = False

while not gano:
    try:
        entrada = input(f"{nombre}, adivina (1-10): ")
        numero = int(entrada)
        intentos += 1
        
        if numero < secreto:
            print("🔽 Muy bajo")
        elif numero > secreto:
            print("🔼 Muy alto")
        else:
            print(f"✨ ¡CORRECTO! Ganaste en {intentos} intentos.")
            gano = True
    except ValueError:
        print("❌ Por favor ingresa un número válido.")

# --- GUARDAR Y MOSTRAR ---
print("\n💾 Guardando en base de datos...")
cursor.execute("INSERT INTO historial VALUES (?, ?)", (nombre, intentos))
conexion.commit()

print("\n🏆 --- HALL OF FAME --- 🏆")
cursor.execute("SELECT * FROM historial ORDER BY intentos ASC")
ganadores = cursor.fetchall()
for g in ganadores:
    print(f"👤 {g[0]} | 🎲 {g[1]} intentos")

conexion.close()