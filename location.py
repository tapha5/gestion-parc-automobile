from date import Date
from client import Client
from vehicule import Vehicule

class Location:
    """Classe représentant une location de véhicule"""
    
    def __init__(self, id_location, client, vehicule, date_debut, date_fin=None):
        """
        Initialise une location avec son ID, le client, le véhicule, la date de début et optionnellement la date de fin
        
        Args:
            id_location (str): L'identifiant unique de la location
            client (Client): Le client qui loue le véhicule
            vehicule (Vehicule): Le véhicule loué
            date_debut (Date): La date de début de la location
            date_fin (Date, optional): La date de fin de la location. Defaults to None.
        
        Raises:
            ValueError: Si le véhicule n'est pas disponible
            TypeError: Si les types des arguments ne sont pas corrects
        """
        # Vérification des types
        if not isinstance(client, Client):
            raise TypeError("Le client doit être une instance de la classe Client")
        if not isinstance(vehicule, Vehicule):
            raise TypeError("Le véhicule doit être une instance de la classe Vehicule")
        if not isinstance(date_debut, Date):
            raise TypeError("La date de début doit être une instance de la classe Date")
        if date_fin is not None and not isinstance(date_fin, Date):
            raise TypeError("La date de fin doit être une instance de la classe Date")
        
        # Vérification de la disponibilité du véhicule
        if not vehicule.est_disponible():
            raise ValueError("Le véhicule n'est pas disponible pour la location")
        
        self._id_location = id_location
        self._client = client
        self._vehicule = vehicule
        self._date_debut = date_debut
        self._date_fin = date_fin
        self._prix = None
        
        # Marquer le véhicule comme loué
        vehicule.louer()
    
    # Getters et setters pour id_location
    def get_id_location(self):
        """Retourne l'identifiant de la location"""
        return self._id_location
    
    def set_id_location(self, id_location):
        """
        Modifie l'identifiant de la location
        
        Args:
            id_location (str): Le nouvel identifiant de la location
        """
        self._id_location = id_location
    
    # Getters et setters pour client
    def get_client(self):
        """Retourne le client de la location"""
        return self._client
    
    def set_client(self, client):
        """
        Modifie le client de la location
        
        Args:
            client (Client): Le nouveau client de la location
        
        Raises:
            TypeError: Si le client n'est pas une instance de la classe Client
        """
        if not isinstance(client, Client):
            raise TypeError("Le client doit être une instance de la classe Client")
        self._client = client
    
    # Getters et setters pour vehicule
    def get_vehicule(self):
        """Retourne le véhicule de la location"""
        return self._vehicule
    
    def set_vehicule(self, vehicule):
        """
        Modifie le véhicule de la location
        Cette méthode n'est pas recommandée car elle peut créer des incohérences
        
        Args:
            vehicule (Vehicule): Le nouveau véhicule de la location
        
        Raises:
            TypeError: Si le véhicule n'est pas une instance de la classe Vehicule
            ValueError: Si le véhicule n'est pas disponible
        """
        if not isinstance(vehicule, Vehicule):
            raise TypeError("Le véhicule doit être une instance de la classe Vehicule")
        if not vehicule.est_disponible():
            raise ValueError("Le véhicule n'est pas disponible pour la location")
        
        # Rendre l'ancien véhicule disponible
        self._vehicule.rendre()
        
        # Mettre à jour le véhicule et le marquer comme loué
        self._vehicule = vehicule
        vehicule.louer()
    
    # Getters et setters pour date_debut
    def get_date_debut(self):
        """Retourne la date de début de la location"""
        return self._date_debut
    
    def set_date_debut(self, date_debut):
        """
        Modifie la date de début de la location
        
        Args:
            date_debut (Date): La nouvelle date de début de la location
        
        Raises:
            TypeError: Si la date de début n'est pas une instance de la classe Date
            ValueError: Si la nouvelle date de début est postérieure à la date de fin
        """
        if not isinstance(date_debut, Date):
            raise TypeError("La date de début doit être une instance de la classe Date")
        
        if self._date_fin is not None and date_debut.difference(self._date_fin) < 0:
            raise ValueError("La date de début ne peut pas être postérieure à la date de fin")
        
        self._date_debut = date_debut
        self._prix = None  # Réinitialiser le prix car la durée a changé
    
    # Getters et setters pour date_fin
    def get_date_fin(self):
        """Retourne la date de fin de la location"""
        return self._date_fin
    
    def set_date_fin(self, date_fin):
        """
        Modifie la date de fin de la location
        
        Args:
            date_fin (Date): La nouvelle date de fin de la location
        
        Raises:
            TypeError: Si la date de fin n'est pas une instance de la classe Date
            ValueError: Si la nouvelle date de fin est antérieure à la date de début
        """
        if date_fin is not None:
            if not isinstance(date_fin, Date):
                raise TypeError("La date de fin doit être une instance de la classe Date")
            
            if self._date_debut.difference(date_fin) < 0:
                raise ValueError("La date de fin ne peut pas être antérieure à la date de début")
        
        self._date_fin = date_fin
        self._prix = None  # Réinitialiser le prix car la durée a changé
    
    def duree(self):
        """
        Calcule la durée de la location en jours
        
        Returns:
            int: Le nombre de jours de la location, ou None si la date de fin n'est pas définie
        """
        if self._date_fin is None:
            return None
        
        return self._date_debut.difference(self._date_fin)
    
    def terminer(self, date_fin):
        """
        Termine la location à la date spécifiée
        
        Args:
            date_fin (Date): La date de fin de la location
        
        Returns:
            float: Le prix final de la location
        
        Raises:
            TypeError: Si la date de fin n'est pas une instance de la classe Date
            ValueError: Si la date de fin est antérieure à la date de début
        """
        self.set_date_fin(date_fin)
        
        # Rendre le véhicule disponible
        self._vehicule.rendre()
        
        # Calculer et retourner le prix
        return self.calcul_prix()
    
    def calcul_prix(self):
        """
        Calcule le prix de la location
        
        Returns:
            float: Le prix de la location, ou None si la date de fin n'est pas définie
        """
        if self._date_fin is None:
            return None
        
        nb_jours = self.duree()
        
        if nb_jours == 0:
            nb_jours = 1  # Minimum 1 jour de location
        
        self._prix = self._vehicule.calculer_prix_location(nb_jours)
        
        return self._prix
    
    def get_prix(self):
        """
        Retourne le prix de la location
        
        Returns:
            float: Le prix de la location, ou None s'il n'a pas encore été calculé
        """
        # Si le prix n'a pas encore été calculé, le calculer
        if self._prix is None and self._date_fin is not None:
            self._prix = self.calcul_prix()
        
        return self._prix
    
    def afficher(self):
        """
        Affiche les informations de la location
        
        Returns:
            str: Une chaîne contenant les informations de la location
        """
        info = (f"Location #{self.get_id_location()}\n"
                f"Client: {self.get_client().get_nom()} {self.get_client().get_id_client()}\n"
                f"Véhicule: {self.get_vehicule().afficher_info()}\n"
                f"Date de début: {self.get_date_debut().to_string()}")
        
        if self.get_date_fin() is not None:
            info += f"\nDate de fin: {self.get_date_fin().to_string()}"
            info += f"\nDurée: {self.duree()} jour(s)"
            info += f"\nPrix: {self.calcul_prix():.2f}€"
        else:
            info += "\nLocation en cours"
        
        return info