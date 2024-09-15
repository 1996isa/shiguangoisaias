import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('torneo_futbol.db')
c = conn.cursor()

# Crear tablas
c.execute('''
CREATE TABLE IF NOT EXISTS equipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS jugadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    id_equipo INTEGER,
    FOREIGN KEY (id_equipo) REFERENCES equipos (id)
)
''')

# Función para agregar un equipo
def agregar_equipo(nombre):
    c.execute('INSERT INTO equipos (nombre) VALUES (?)', (nombre,))
    conn.commit()

# Función para agregar un jugador
def agregar_jugador(nombre, edad, id_equipo):
    c.execute('INSERT INTO jugadores (nombre, edad, id_equipo) VALUES (?, ?, ?)', (nombre, edad, id_equipo))
    conn.commit()

# Función para listar todos los jugadores y equipos
def listar_jugadores_y_equipos():
    c.execute('''
    SELECT jugadores.nombre, jugadores.edad, equipos.nombre 
    FROM jugadores
    LEFT JOIN equipos ON jugadores.id_equipo = equipos.id
    ''')
    return c.fetchall()

# Ejemplo de uso
agregar_equipo('Equipo A')
agregar_equipo('Equipo B')
agregar_jugador('Juan Pérez', 22, 1)
agregar_jugador('Ana Gómez', 25, 2)

print(listar_jugadores_y_equipos())

# Cerrar la conexión
conn.close()
