# Anleitung
1. Echo Server im Terminal starten. Befehl: python3 /home/miro/Dokumente/Python-Projekt/echo-server.py
2. Echo Client in einem zweiten Terminal starten. Befehl: python3 /home/miro/Dokumente/Python-Projekt/echo-client.py
3. IP-Adresse und Port des Servers angeben. In meinem Fall: 127.0.0.1, 65432
4. Der Client schickt automatisch den Wert "1" an den Server und dieser sollte nun mit dem Wert "2" antworten
5. j oder n tippen um fortzufahren oder beenden.

### Anleitung mit Proxy
1. Echo Server im Terminal starten. Befehl: python3 /home/miro/Dokumente/Python-Projekt/echo-server.py
2. Echo Proxy im Terminal starten. Befehl: python3 /home/miro/Dokumente/Python-Projekt/echo-proxy.py
3. Echo Client in einem zweiten Terminal starten. Befehl: python3 /home/miro/Dokumente/Python-Projekt/echo-client.py
4. IP-Adresse und Port des Proxys angeben. In meinem Fall: 127.0.0.1, 50001
5. Der Client schickt automatisch den Wert "1" an den Proxy und dieser leitet ihn an den Server weiter.
6. Der Server antwortet mit dem Wert "2" und sendet diesen an den Proxy. Der Proxy leitet den Wert wiederum zum Client.
7. j oder n um fortzufahren oder beenden.


<img width="742" height="410" alt="Bildschirmfoto vom 2026-01-07 14-21-26" src="https://github.com/user-attachments/assets/76c5c5ec-a73f-484a-8e8a-fe5d2797dde2" />
<img width="750" height="410" alt="Bildschirmfoto vom 2026-01-07 14-21-30" src="https://github.com/user-attachments/assets/90567f12-56e3-4b01-9f5e-5ea69f5928b8" />
<img width="750" height="572" alt="Bildschirmfoto vom 2026-01-07 14-21-33" src="https://github.com/user-attachments/assets/8692333d-dd3e-42b6-97c0-c3212dadc703" />
