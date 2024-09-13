import mysql.connector

try:
    # Connessione al database MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotelpy"  # Nome del database
    )

    cursor = db.cursor()

    # Creazione delle tabelle per hotelpy
    # tabella hotel
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotel (
        ID_hotel VARCHAR(10) PRIMARY KEY,
        nome VARCHAR(20),
        indirizzo VARCHAR(100),
        numero_telefono BIGINT,
        numero_stelle INT
    )
    ''')

    # Tabella Dipendenti
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dipendenti (
        ID_dipendente VARCHAR(20) PRIMARY KEY,
        ID_hotel VARCHAR(10),
        nome VARCHAR(50),
        cognome VARCHAR(50),
        posizione VARCHAR(50),
        salario DECIMAL(10, 2),
        FOREIGN KEY (ID_hotel) REFERENCES hotel(ID_hotel)
    )
    ''')

    # Tabella Camere
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Camere (
        numero_camera INT PRIMARY KEY,
        prezzo INT,
        capienza INT
    )
    ''')

    # Tabella Manutenzioni
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Manutenzioni (
        ID_manutenzione VARCHAR(20) PRIMARY KEY,
        numero_camera INT,
        ID_dipendente VARCHAR(20),
        data DATE,
        descrizione TEXT,
        FOREIGN KEY (ID_dipendente) REFERENCES Dipendenti(ID_dipendente),
        FOREIGN KEY (numero_camera) REFERENCES Camere(numero_camera)
    )
    ''')

    # Tabella Clienti
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clienti (
        ID_cliente VARCHAR(20) PRIMARY KEY,
        email VARCHAR(100),
        nome VARCHAR(50),
        cognome VARCHAR(50),
        documento VARCHAR(50)
    )
    ''')

    # Tabella Prenotazioni
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prenotazioni (
        ID_prenotazione VARCHAR(20) PRIMARY KEY,
        ID_cliente VARCHAR(20),
        numero_camera INT,
        checkin DATE,
        checkout DATE,
        FOREIGN KEY (ID_cliente) REFERENCES Clienti(ID_cliente)
    )
    ''')

    # Tabella Recensioni
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recensioni (
        ID_recensioni VARCHAR(20) PRIMARY KEY,
        ID_cliente VARCHAR(20),
        valutazione INT,
        commento TEXT,
        FOREIGN KEY (ID_cliente) REFERENCES Clienti(ID_cliente)
    )
    ''')

    # Tabella Servizi
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Servizi (
        nome_servizio VARCHAR(50),
        ID_dipendente VARCHAR(20),
        descrizione TEXT,
        prezzo DECIMAL(10, 2),
        FOREIGN KEY (ID_dipendente) REFERENCES Dipendenti(ID_dipendente)
    )
    ''')

    # Tabella Prenotazione_servizi
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prenotazione_servizi (
        ID_prenotazione_servizi VARCHAR(20) PRIMARY KEY,
        ID_prenotazione VARCHAR(20),
        nome_servizio VARCHAR(50),
        data DATE,
        ora TIME,
        FOREIGN KEY (ID_prenotazione) REFERENCES Prenotazioni(ID_prenotazione)
    )
    ''')

    # Tabella Fatture
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fatture (
        ID_fattura VARCHAR(20) PRIMARY KEY,
        ID_prenotazione VARCHAR(20),
        data_emissione DATE,
        totale DECIMAL(10, 2),
        FOREIGN KEY (ID_prenotazione) REFERENCES Prenotazioni(ID_prenotazione)
    )
    ''')

    # Inserimento dati nella tabella hotel
    cursor.execute('''
    INSERT INTO hotel (ID_hotel, nome, indirizzo, numero_telefono, numero_stelle) VALUES
    ('rm0212', 'Hotel Claila Roma', 'Via montenapoleone 5', 3452763988, 4)
    ''')

    # Inserimento dati nella tabella Dipendenti
    cursor.executemany('''
    INSERT INTO Dipendenti (ID_dipendente, ID_hotel, nome, cognome, posizione, salario) VALUES (%s, %s, %s, %s, %s, %s)
    ''', [
        ('dip0001', 'rm0212', 'Francesco', 'Di Crescenzo', 'cuoco', 1500.00),
        ('dip0002', 'rm0212', 'Caterina', 'Bianchi', 'cameriera ai piani', 1200.00),
        ('dip0004', 'rm0212', 'Maurizio', 'Di Gregorio', 'massaggiatrice', 1400.00),
        ('dip0005', 'rm0212', 'Francesca', 'Donofrio', 'receptionist', 1400.00),
        ('dip0006', 'rm0212', 'Michele', 'Santoro', 'tuttofare', 1700.00),
        ('dip0003', 'rm0212', 'Ludovica', 'Rossi', 'guida turistica', 1200.00),
        ('dip0007', 'rm0212', 'Andrea', 'Francesconi', 'tuttofare', 1700.00)
    ])

    # Inserimento dati nella tabella Camere
    cursor.executemany('''
    INSERT INTO Camere (numero_camera, prezzo, capienza) VALUES (%s, %s, %s)
    ''', [
        (1, 250, 2),
        (2, 250, 4),
        (13, 120, 4),
        (98, 135, 2),
        (117, 390, 8)
    ])

    # Inserimento dati nella tabella Manutenzioni
    cursor.executemany('''
    INSERT INTO Manutenzioni (ID_manutenzione, numero_camera, ID_dipendente, data, descrizione) VALUES (%s, %s, %s, %s, %s)
    ''', [
        ('MAN0082', 117, 'dip0006', '2024-07-12', 'Riparazione armadio'),
        ('MAN0095', 98, 'dip0007', '2024-07-12', 'Riparazione doghe letto'),
        ('MAN0238', 13, 'dip0006', '2024-07-12', 'sostituzione climatizzatore')
    ])

    # Inserimento dati nella tabella Clienti
    cursor.executemany('''
    INSERT INTO Clienti (ID_cliente, email, nome, cognome, documento) VALUES (%s, %s, %s, %s, %s)
    ''', [
        ('CL009843', 'simrossi@gmail.com', 'Simone', 'Rossi', 'AY 73690'),
        ('CL000964', 'alessandrocantadori@virgilio.it', 'Alessandro', 'Cantadori', 'CA39423'),
        ('CL019736', 'francydidomenico@gmail.com', 'Francesca', 'Di Domenico', 'CA30633'),
        ('CL003429', 'riccardopescini@hotmail.com', 'Riccardo', 'Pescini', 'AY002467')
    ])

    # Inserimento dati nella tabella Prenotazioni
    cursor.executemany('''
    INSERT INTO Prenotazioni (ID_prenotazione, ID_cliente, numero_camera, checkin, checkout) VALUES (%s, %s, %s, %s, %s)
    ''', [
        ('PR002134', 'CL009843', 1, '2022-04-18', '2022-04-22'),
        ('PR000327', 'CL000964', 13, '2018-05-01', '2018-05-08'),
        ('PR011756', 'CL019736', 117, '2024-09-10', '2024-09-17'),
        ('PR004787', 'CL003429', 1, '2018-05-01', '2018-05-08')
    ])

    # Inserimento dati nella tabella Recensioni
    cursor.executemany('''
    INSERT INTO Recensioni (ID_recensioni, ID_cliente, valutazione, commento) VALUES (%s, %s, %s, %s)
    ''', [
        ('REC02382', 'CL000964', 4, 'Ben curato e accogliente, stra consigliato'),
        ('REC00394', 'CL003429', 1, 'camera sporchissima, cibo di bassa qualità, posizione super vicino il centro, non ritornerei'),
        ('REC00034', 'CL019736', 3, 'mi sono trovata molto bene, personale gentile ed accogliente, la posizione è ottima per chi vuole visitare la città')
    ])

    # Inserimento dati nella tabella Servizi
    cursor.executemany('''
    INSERT INTO Servizi (nome_servizio, ID_dipendente, descrizione, prezzo) VALUES (%s, %s, %s, %s)
    ''', [
        ('massaggio orientale', 'dip0004', 'un’ora di completo relax nel nostro centro massaggi', 45),
        ('sauna con vista', 'VOID', 'imperdibile per godersi del sano relax con vista Colosseo al tramonto', 20),
        ('passeggiata a cavallo', 'VOID', 'un giro per le fanatiche vie della città in compagnia del nostro Birillo, simpaticissimo amico a 4 zampe', 70),
        ('visita guidata', 'dip0003', 'immersiva visita per le Vie della città accompagnati da un’eccelsa guida turistica', 100),
        ('cena in camera', 'dip0001', 'gusta le prelibatezze dello chef comodamente nella sala da pranzo della tua camera', 150)
    ])

    # Inserimento dati nella tabella Prenotazione_servizi
    cursor.executemany('''
    INSERT INTO Prenotazione_servizi (ID_prenotazione_servizi, ID_prenotazione, nome_servizio, data, ora) VALUES (%s, %s, %s, %s, %s)
    ''', [
        ('PRS07839', 'PR002134', 'massaggio orientale', '2022-04-20', '11:00'),
        ('PRS45174', 'PR011756', 'sauna con vista', '2024-09-15', '17:30'),
        ('PRS08392', 'PR011756', 'passeggiata a cavallo', '2024-09-16', '19:00')
    ])

    # Inserimento dati nella tabella Fatture
    cursor.executemany('''
    INSERT INTO Fatture (ID_fattura, ID_prenotazione, data_emissione, totale) VALUES (%s, %s, %s, %s)
    ''', [
        ('F001394', 'PR000327', '2018-05-08', 840),
        ('F0019355', 'PR004787', '2018-05-08', 1750),
        ('F002934', 'PR002134', '2022-04-22', 1000)
    ])

    # Commit delle operazioni
    db.commit()

    # Recupero dei dati per verificarne l'inserimento
    cursor.execute("SELECT * FROM Dipendenti")
    dipendenti_results = cursor.fetchall()
    print("Dati Dipendenti:", dipendenti_results)

except mysql.connector.Error as err:
    print(f"Errore: {err}")

finally:
    cursor.close()
    db.close()