# maListe= ["a","b","chien","trois","b","b"]
# maListe.append("cinq")
# print(maListe.insert(2, "chat"))
# print(maListe.remove("chien"))
# print(maListe.pop(3))

# print(maListe)

# print(maListe.index("chat"))
# print(maListe.count("b"))
# print(maListe.sort())
# print(maListe.reverse())
# print(maListe.clear())
# print(maListe.extend([6, 7]))
# len(maListe)
# sum([1, 2, 3])
# min([2, 5, 3])
# max([2, 5, 3])
# sorted([3, 1, 4])
# list("abc")


# print(maListe)


# ma_liste = [1, 2, 3, 4, 5]



# ma_liste = [1, "ip", True, 3.14]


# print(ma_liste[0])  # Affiche le premier élément


# print(ma_liste[-1])  # Affiche le dernier élément


iot_devices = ["Caméra - Actif", "Thermostat - Inactif", "Capteur de mouvement - Actif"]
# iot_devices[1] = "Thermostat - Actif"
# print(iot_devices)


# iot_devices.append(6)
# iot_devices.insert(2, "nouveau")
# print(iot_devices)


# # ips_actives = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]


# logs_securite = [
#     "Tentative de connexion échouée",
#     "Accès non autorisé détecté",
#     "Scan de port détecté"
# ]

# logs_securite.append("DDoS détecté")
# logs_securite.insert(1, "Malware critique détecté")


# # Liste des adresses IP bloquées par le pare-feu
# ip_bloquees = ["192.168.1.10", "10.0.0.5", "172.16.0.8", "192.168.1.15"]

# # Supprimer une adresse IP spécifique si elle n'est plus considérée comme une menace
# ip_bloquees.remove("10.0.0.5")

# # Supprimer l'adresse IP à la position 2 (index 2)
# ip_bloquees.pop(2)


# ma_liste = ["192.168.1.10", "10.0.0.5", "172.16.0.8", "192.168.1.15"]

# for element in ma_liste:
#     print(element)



# print(len(ma_liste))



# Liste des adresses IP suspectes
ips_suspectes = ["192.168.0.100", "10.0.0.45", "172.16.0.7", "192.168.1.200"]


index = 0
while index < len(ips_suspectes):
    print(f"Analyse de l'adresse IP : {ips_suspectes[index]}")
    index += 1



logs_securite = ["Tentative d'intrusion", "Accès non autorisé", "DDoS détecté"]

# Réinitialiser la liste des logs
logs_securite.clear()

# Afficher la liste vide
print(logs_securite)  # Affiche []



ips_suspectes = ["192.168.1.1", "10.0.0.2", "172.16.0.3", "192.168.1.5"]

# Trouver l'index de l'IP "172.16.0.3"
position = ips_suspectes.index("172.16.0.3")

print(f"L'IP est à l'index {position}")  # Affiche : L'IP est à l'index 2


# Liste des tentatives de connexion avec les adresses IP
tentatives_connexion = [
    "192.168.0.10", "10.0.0.5", "192.168.0.10", "172.16.0.8", 
    "192.168.0.10", "192.168.1.50", "10.0.0.5", "192.168.0.10"
]

nb_tentatives_ip = tentatives_connexion.count("192.168.0.10")

print(f"L'adresse IP 192.168.0.10 a tenté de se connecter {nb_tentatives_ip} fois.")


