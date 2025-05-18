Projet AutoPlus - Gestion de Parc Automobile
Ce projet Python implémente un système de gestion pour un parc automobile de location, utilisant les principes de la Programmation Orientée Objet (POO).
Structure du Projet
Le projet est composé de plusieurs modules Python :

vehicule.py : Contient la classe abstraite Vehicule et ses sous-classes Voiture et Camion
client.py : Implémente la classe Client pour gérer les informations des clients
date.py : Fournit la classe Date pour manipuler les dates
location.py : Gère les locations de véhicules
parc_auto.py : Implémente la gestion du parc automobile
main.py : Script principal démontrant les fonctionnalités du système

Fonctionnalités

Création et gestion de différents types de véhicules (voitures, camions)
Gestion des clients
Système de réservation et de location de véhicules
Calcul automatique des prix de location
Recherche de véhicules selon divers critères
Suivi de l'état du parc automobile

Principes de POO utilisés

Encapsulation : Utilisation d'attributs privés (préfixés par _) et de getters/setters
Héritage : Voiture et Camion héritent de la classe abstraite Vehicule
Abstraction : Vehicule est une classe abstraite avec des méthodes abstraites
Polymorphisme : Les sous-classes implémentent leurs propres versions des méthodes comme afficher_info() et calculer_prix_location()

Comment exécuter le projet

Assurez-vous d'avoir Python 3.6 ou supérieur installé
Placez tous les fichiers du projet dans le même répertoire
Exécutez le script principal :

bashpython main.py
Exemple d'utilisation
Le script main.py fournit un exemple complet d'utilisation du système. Il démontre :

La création de véhicules, clients et dates
L'ajout de véhicules au parc
La création et la gestion des locations
La recherche de véhicules selon différents critères
La fin d'une location et la vérification de la disponibilité du véhicule rendu
