import csv

# Données avec les nouveaux élèves ajoutés
data = [
    ["Krystal BELLAY", "ProjetA", "ProjetC", "", "ProjetE", "ProjetA"],
    ["Yanis CESTO", "ProjetB", "", "ProjetD", "", "ProjetB"],
    ["Lee-Lyan CHONG-WING", "ProjetA", "ProjetB", "", "ProjetC", "ProjetA"],
    ["Kendrick CLIO", "ProjetC", "", "ProjetD", "", "ProjetC"],
    ["Clement DEPLANQUE", "ProjetA", "", "ProjetC", "", "ProjetA"],
    ["Renald DESIRE", "ProjetD", "ProjetE", "", "", "ProjetD"],
    ["Thimothee DRAPIN", "ProjetA", "ProjetB", "ProjetC", "", "ProjetA"],
    ["Andy GUSTAVE", "ProjetE", "", "ProjetD", "", "ProjetE"],
    ["Jean-Michel HARROW", "ProjetC", "ProjetD", "", "", "ProjetC"],
    ["Alexis LEGENDRE", "ProjetB", "", "ProjetE", "", "ProjetB"],
    ["Jahyna LOUIS SIDNEY", "ProjetA", "ProjetC", "ProjetE", "", "ProjetA"],
    ["Rhonny LOUISY-LOUIS", "ProjetD", "", "ProjetB", "", "ProjetD"],
    ["Jimmy MATHURINA", "ProjetE", "ProjetA", "", "", "ProjetE"],
    ["Matthieu MORNET-HELOISE", "ProjetB", "", "ProjetD", "ProjetC", "ProjetB"],
    ["Steven PAJOUL", "ProjetA", "ProjetC", "", "ProjetE", "ProjetA"],
    ["Quentin RETORY", "ProjetD", "", "ProjetB", "", "ProjetD"],
    ["Talia TRAQUE", "ProjetC", "ProjetE", "ProjetA", "", "ProjetC"]
]

# Nom du fichier CSV
filename = "repartition_projets.csv"

# Écriture des données dans le fichier CSV
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Écriture de l'en-tête
    header = ["Nom Prénom de l'étudiant", "Nom de code du projet 1", "Nom de code du projet 2", 
              "Nom de code du projet 3", "Nom de code du projet 4", "Choix du projet 1"]
    writer.writerow(header)
    
    # Écriture des données
    writer.writerows(data)

print(f"Le fichier CSV '{filename}' a été créé avec succès.")
