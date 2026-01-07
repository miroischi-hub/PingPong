import socket # Importiert das Modul, um Sockets für Netzwerkkommunikation zu verwenden

# Hostadresse und Portnummer eingeben
HOST = input("IP des Servers eingeben: ")
PORT = int(input("Portnummer eingeben:"))
message = 1
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        # Nachricht an den Server senden
        sock.sendto(str(message).encode(), (HOST, PORT)) # Sendet Nachricht an angegebene IP und Port

        # Antwort vom Server empfangen und Ausgeben
        data, addr = sock.recvfrom(1024) # Wartet auf Antwort vom Server
        print(f"Send: {message}, Received: {data.decode()}")
        message = int(data.decode())

        # Wiederholung
        again = input("Continue? (j/n): ").strip().lower()
        if again != "j":
            message = False
            print("Ping Pong finished!")
        # Nächste Zahl
        else:
            message += 1
