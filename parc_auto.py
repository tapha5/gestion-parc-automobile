from vehicule import Vehicule, Voiture, Camion

class ParcAuto:
    """Classe représentant le parc automobile"""
    
    def __init__(self, nom):
        """
        Initialise un parc automobile avec son nom
        
        Args:
            nom (str): Le nom du parc automobile
        """
        self._nom = nom
        self._vehicules = []
    
    # Getters et setters pour nom
    def get_nom(self):
        """Retourne le nom du parc automobile"""
        return self._nom
    
    def set_nom(self, nom):
        """
        Modifie le nom du parc automobile
        
        Args:
            nom (str): Le nouveau nom du parc automobile
        """
        self._nom = nom
    
    # Getters pour vehicules (pas de setter direct pour la liste complète)
    def get_vehicules(self):
        """
        Retourne la liste des véhicules du parc automobile
        
        Returns:
            list: La liste des véhicules du parc automobile
        """
        return self._vehicules
    
    def ajouter_vehicule(self, vehicule):
        """
        Ajoute un véhicule au parc automobile
        
        Args:
            vehicule (Vehicule): Le véhicule à ajouter
        
        Returns:
            bool: True si le véhicule a été ajouté, False sinon
        
        Raises:
            TypeError: Si le véhicule n'est pas une instance de la classe Vehicule
        """
        if not isinstance(vehicule, Vehicule):
            raise TypeError("Le véhicule doit être une instance de la classe Vehicule")
        
        # Vérifier que le véhicule n'est pas déjà dans le parc
        for v in self._vehicules:
            if (v.get_marque() == vehicule.get_marque() and 
                v.get_modele() == vehicule.get_modele() and 
                v.get_annee() == vehicule.get_annee()):
                # Véhicule similaire déjà présent
                return False
        
        self._vehicules.append(vehicule)
        return True
    
    def supprimer_vehicule(self, vehicule):
        """
        Supprime un véhicule du parc automobile
        
        Args:
            vehicule (Vehicule): Le véhicule à supprimer
        
        Returns:
            bool: True si le véhicule a été supprimé, False s'il n'était pas dans le parc
        """
        if vehicule in self._vehicules:
            self._vehicules.remove(vehicule)
            return True
        return False
    
    def rechercher_vehicule(self, marque=None, modele=None, annee=None, disponible=None, type_vehicule=None):
        """
        Recherche des véhicules dans le parc automobile selon différents critères
        
        Args:
            marque (str, optional): La marque des véhicules recherchés. Defaults to None.
            modele (str, optional): Le modèle des véhicules recherchés. Defaults to None.
            annee (int, optional): L'année des véhicules recherchés. Defaults to None.
            disponible (bool, optional): La disponibilité des véhicules recherchés. Defaults to None.
            type_vehicule (str, optional): Le type des véhicules recherchés ("Voiture" ou "Camion"). Defaults to None.
        
        Returns:
            list: La liste des véhicules correspondant aux critères
        """
        resultats = []
        
        for vehicule in self._vehicules:
            match = True
            
            if marque is not None and vehicule.get_marque().lower() != marque.lower():
                match = False
                
            if modele is not None and vehicule.get_modele().lower() != modele.lower():
                match = False
                
            if annee is not None and vehicule.get_annee() != annee:
                match = False
                
            if disponible is not None and vehicule.est_disponible() != disponible:
                match = False
                
            if type_vehicule is not None:
                if type_vehicule.lower() == "voiture" and not isinstance(vehicule, Voiture):
                    match = False
                elif type_vehicule.lower() == "camion" and not isinstance(vehicule, Camion):
                    match = False
            
            if match:
                resultats.append(vehicule)
        
        return resultats
    
    def lister_vehicules_disponibles(self):
        """
        Liste tous les véhicules disponibles dans le parc automobile
        
        Returns:
            list: La liste des véhicules disponibles
        """
        return self.rechercher_vehicule(disponible=True)
    
    def compter_vehicules(self, disponible=None, type_vehicule=None):
        """
        Compte le nombre de véhicules dans le parc automobile selon différents critères
        
        Args:
            disponible (bool, optional): La disponibilité des véhicules à compter. Defaults to None.
            type_vehicule (str, optional): Le type des véhicules à compter ("Voiture" ou "Camion"). Defaults to None.
        
        Returns:
            int: Le nombre de véhicules correspondant aux critères
        """
        return len(self.rechercher_vehicule(disponible=disponible, type_vehicule=type_vehicule))
    
    def afficher_parc(self):
        """
        Affiche les informations du parc automobile
        
        Returns:
            str: Une chaîne contenant les informations du parc automobile
        """
        nb_total = len(self._vehicules)
        nb_voitures = self.compter_vehicules(type_vehicule="Voiture")
        nb_camions = self.compter_vehicules(type_vehicule="Camion")
        nb_disponibles = self.compter_vehicules(disponible=True)
        nb_loues = self.compter_vehicules(disponible=False)
        
        info = f"Parc automobile: {self.get_nom()}\n"
        info += f"Nombre total de véhicules: {nb_total}\n"
        info += f"Voitures: {nb_voitures}, Camions: {nb_camions}\n"
        info += f"Véhicules disponibles: {nb_disponibles}, Véhicules loués: {nb_loues}\n\n"
        
        if nb_total > 0:
            info += "Liste des véhicules:\n"
            for i, vehicule in enumerate(self._vehicules, 1):
                info += f"{i}. {vehicule.afficher_info()}\n"
        
        return info