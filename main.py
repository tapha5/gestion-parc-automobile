from vehicule import Voiture, Camion
from client import Client
from date import Date
from location import Location
from parc_auto import ParcAuto

def main():

    print("\n===== DÉMARRAGE DU SYSTÈME DE GESTION DU PARC AUTOMOBILE AUTOPLUS =====\n")
    
    print("Création du parc automobile AutoPlus...")
    parc = ParcAuto("AutoPlus")
    print(f"Parc automobile '{parc.get_nom()}' créé avec succès!")
    
    print("\n===== CRÉATION DES VÉHICULES =====")
    
    # Création de voitures
    voiture1 = Voiture("Renault", "Clio", 2022, 4)
    voiture2 = Voiture("Peugeot", "308", 2021, 5)
    voiture3 = Voiture("Citroën", "C3", 2023, 3)
    voiture4 = Voiture("Ford", "Fiesta", 2020, 4)
    
    # Création de camions
    camion1 = Camion("Renault", "Master", 2021, 3.5)
    camion2 = Camion("Iveco", "Daily", 2022, 7.2)
    camion3 = Camion("Mercedes", "Sprinter", 2020, 5.0)
    
    # Affichage des informations des véhicules
    print("Voici les véhicules créés:")
    print(voiture1.afficher_info())
    print(voiture2.afficher_info())
    print(voiture3.afficher_info())
    print(voiture4.afficher_info())
    print(camion1.afficher_info())
    print(camion2.afficher_info())
    print(camion3.afficher_info())
    
    print("\n===== AJOUT DES VÉHICULES AU PARC =====")
    
    # Ajout des véhicules au parc
    parc.ajouter_vehicule(voiture1)
    parc.ajouter_vehicule(voiture2)
    parc.ajouter_vehicule(voiture3)
    parc.ajouter_vehicule(voiture4)
    parc.ajouter_vehicule(camion1)
    parc.ajouter_vehicule(camion2)
    parc.ajouter_vehicule(camion3)
    
    print("Tous les véhicules ont été ajoutés au parc.")
    
    print("\n===== AFFICHAGE DU PARC AUTOMOBILE =====")
    print(parc.afficher_parc())
    
    print("\n===== CRÉATION DES CLIENTS =====")
    
    # Création de clients
    client1 = Client("CL001", "Moustapha")
    client2 = Client("CL002", "Rokhaya")
    client3 = Client("CL003", "Ahmady")
    
    # Affichage des informations des clients
    print("Voici les clients créés:")
    print(client1.infos())
    print("\n" + client2.infos())
    print("\n" + client3.infos())
    
    print("\n===== CRÉATION DES DATES =====")
    
    # Création de dates
    date1 = Date(15, 5, 2025)
    date2 = Date(20, 5, 2025)
    date3 = Date(25, 5, 2025)
    date4 = Date(1, 6, 2025)
    
    print(f"Dates créées: {date1}, {date2}, {date3}, {date4}")
    print(f"Différence entre {date1} et {date2}: {date1.difference(date2)} jours")
    print(f"Différence entre {date1} et {date3}: {date1.difference(date3)} jours")
    print(f"Différence entre {date1} et {date4}: {date1.difference(date4)} jours")
    
    print("\n===== CRÉATION DES LOCATIONS =====")
    
    # Création de locations
    location1 = Location("LOC001", client1, voiture1, date1, date2)
    print("Location 1 créée:")
    print(location1.afficher())
    
    location2 = Location("LOC002", client2, camion1, date2, date3)
    print("\nLocation 2 créée:")
    print(location2.afficher())
    
    location3 = Location("LOC003", client3, voiture3, date3)
    print("\nLocation 3 créée (sans date de fin):")
    print(location3.afficher())
    
    print("\n===== AFFICHAGE DES VÉHICULES DISPONIBLES =====")
    
    # Affichage des véhicules disponibles
    vehicules_disponibles = parc.lister_vehicules_disponibles()
    print(f"Nombre de véhicules disponibles: {len(vehicules_disponibles)}")
    
    if vehicules_disponibles:
        print("Véhicules disponibles:")
        for i, vehicule in enumerate(vehicules_disponibles, 1):
            print(f"{i}. {vehicule.afficher_info()}")
    else:
        print("Aucun véhicule disponible.")
    
    print("\n===== RECHERCHE DE VÉHICULES =====")
    
    # Recherche de véhicules par marque
    print("Recherche de véhicules Renault:")
    resultats = parc.rechercher_vehicule(marque="Renault")
    for vehicule in resultats:
        print(vehicule.afficher_info())
    
    # Recherche de voitures disponibles
    print("\nRecherche de voitures disponibles:")
    resultats = parc.rechercher_vehicule(disponible=True, type_vehicule="Voiture")
    for vehicule in resultats:
        print(vehicule.afficher_info())
    
    print("\n===== RETOUR D'UN VÉHICULE =====")
    
    # Terminer une location
    print(f"Fin de la location LOC001 le {date3}:")
    prix = location1.terminer(date3)
    print(f"Prix final: {prix:.2f}€")
    print(location1.afficher())
    
    # Vérifier que le véhicule est à nouveau disponible
    print("\nVérification de la disponibilité du véhicule rendu:")
    print(voiture1.afficher_info())
    
    print("\n===== ÉTAT FINAL DU PARC AUTOMOBILE =====")
    print(parc.afficher_parc())
    
    print("\n===== FIN DU PROGRAMME =====")


if __name__ == "__main__":
    main()