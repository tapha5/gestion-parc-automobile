from abc import ABC, abstractmethod

class Vehicule(ABC):
    """Classe abstraite représentant un véhicule"""
    
    def __init__(self, marque, modele, annee):
        """
        Initialise un véhicule avec sa marque, son modèle et son année
        
        Args:
            marque (str): La marque du véhicule
            modele (str): Le modèle du véhicule
            annee (int): L'année de fabrication du véhicule
        """
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._disponible = True
    
    # Getters et setters pour marque
    def get_marque(self):
        """Retourne la marque du véhicule"""
        return self._marque
    
    def set_marque(self, marque):
        """
        Modifie la marque du véhicule
        
        Args:
            marque (str): La nouvelle marque du véhicule
        """
        self._marque = marque
    
    # Getters et setters pour modele
    def get_modele(self):
        """Retourne le modèle du véhicule"""
        return self._modele
    
    def set_modele(self, modele):
        """
        Modifie le modèle du véhicule
        
        Args:
            modele (str): Le nouveau modèle du véhicule
        """
        self._modele = modele
    
    # Getters et setters pour annee
    def get_annee(self):
        """Retourne l'année de fabrication du véhicule"""
        return self._annee
    
    def set_annee(self, annee):
        """
        Modifie l'année de fabrication du véhicule
        
        Args:
            annee (int): La nouvelle année de fabrication du véhicule
        """
        self._annee = annee
    
    # Getters et setters pour disponible
    def est_disponible(self):
        """Retourne True si le véhicule est disponible, False sinon"""
        return self._disponible
    
    def set_disponible(self, disponible):
        """
        Modifie la disponibilité du véhicule
        
        Args:
            disponible (bool): La nouvelle disponibilité du véhicule
        """
        self._disponible = disponible
    
    def louer(self):
        """
        Marque le véhicule comme loué
        
        Returns:
            bool: True si le véhicule était disponible et a été loué, False sinon
        """
        if self._disponible:
            self._disponible = False
            return True
        return False
    
    def rendre(self):
        """
        Marque le véhicule comme disponible
        
        Returns:
            bool: True si le véhicule était loué et a été rendu, False sinon
        """
        if not self._disponible:
            self._disponible = True
            return True
        return False
    
    @abstractmethod
    def afficher_info(self):
        """Méthode abstraite pour afficher les informations du véhicule"""
        pass
    
    @abstractmethod
    def calculer_prix_location(self, nb_jours):
        """
        Méthode abstraite pour calculer le prix de location du véhicule
        
        Args:
            nb_jours (int): Le nombre de jours de location
        
        Returns:
            float: Le prix de la location
        """
        pass


class Voiture(Vehicule):
    """Classe représentant une voiture, hérite de Vehicule"""
    
    def __init__(self, marque, modele, annee, nb_portes):
        """
        Initialise une voiture avec sa marque, son modèle, son année et son nombre de portes
        
        Args:
            marque (str): La marque de la voiture
            modele (str): Le modèle de la voiture
            annee (int): L'année de fabrication de la voiture
            nb_portes (int): Le nombre de portes de la voiture
        """
        super().__init__(marque, modele, annee)
        self._nb_portes = nb_portes
    
    # Getter et setter pour nb_portes
    def get_nb_portes(self):
        """Retourne le nombre de portes de la voiture"""
        return self._nb_portes
    
    def set_nb_portes(self, nb_portes):
        """
        Modifie le nombre de portes de la voiture
        
        Args:
            nb_portes (int): Le nouveau nombre de portes de la voiture
        """
        self._nb_portes = nb_portes
    
    def afficher_info(self):
        """
        Affiche les informations de la voiture
        
        Returns:
            str: Une chaîne contenant les informations de la voiture
        """
        disponibilite = "Disponible" if self.est_disponible() else "Non disponible"
        return f"Voiture {self.get_marque()} {self.get_modele()} ({self.get_annee()}) - {self.get_nb_portes()} portes - {disponibilite}"
    
    def calculer_prix_location(self, nb_jours):
        """
        Calcule le prix de location de la voiture
        
        Args:
            nb_jours (int): Le nombre de jours de location
        
        Returns:
            float: Le prix de la location (base de 50€/jour)
        """
        # Tarif de base pour une voiture: 50€/jour
        return 50 * nb_jours


class Camion(Vehicule):
    """Classe représentant un camion, hérite de Vehicule"""
    
    def __init__(self, marque, modele, annee, capacite):
        """
        Initialise un camion avec sa marque, son modèle, son année et sa capacité
        
        Args:
            marque (str): La marque du camion
            modele (str): Le modèle du camion
            annee (int): L'année de fabrication du camion
            capacite (float): La capacité en tonnes du camion
        """
        super().__init__(marque, modele, annee)
        self._capacite = capacite
    
    # Getter et setter pour capacite
    def get_capacite(self):
        """Retourne la capacité du camion en tonnes"""
        return self._capacite
    
    def set_capacite(self, capacite):
        """
        Modifie la capacité du camion
        
        Args:
            capacite (float): La nouvelle capacité du camion en tonnes
        """
        self._capacite = capacite
    
    def afficher_info(self):
        """
        Affiche les informations du camion
        
        Returns:
            str: Une chaîne contenant les informations du camion
        """
        disponibilite = "Disponible" if self.est_disponible() else "Non disponible"
        return f"Camion {self.get_marque()} {self.get_modele()} ({self.get_annee()}) - Capacité: {self.get_capacite()} tonnes - {disponibilite}"
    
    def calculer_prix_location(self, nb_jours):
        """
        Calcule le prix de location du camion
        
        Args:
            nb_jours (int): Le nombre de jours de location
        
        Returns:
            float: Le prix de la location (base de 80€/jour + 10€ par tonne de capacité)
        """
        # Tarif de base pour un camion: 80€/jour + 10€ par tonne de capacité
        return (80 + (10 * self.get_capacite())) * nb_jours