class Date:
    """Classe représentant une date"""
    
    def __init__(self, jour, mois, annee):
        """
        Initialise une date avec son jour, son mois et son année
        
        Args:
            jour (int): Le jour de la date (1-31)
            mois (int): Le mois de la date (1-12)
            annee (int): L'année de la date
        
        Raises:
            ValueError: Si la date est invalide
        """
        # Vérification de la validité de la date
        if not self._est_date_valide(jour, mois, annee):
            raise ValueError("Date invalide")
        
        self._jour = jour
        self._mois = mois
        self._annee = annee
    
    # Getters et setters pour jour
    def get_jour(self):
        """Retourne le jour de la date"""
        return self._jour
    
    def set_jour(self, jour):
        """
        Modifie le jour de la date si la nouvelle date est valide
        
        Args:
            jour (int): Le nouveau jour de la date
        
        Raises:
            ValueError: Si la nouvelle date est invalide
        """
        if not self._est_date_valide(jour, self._mois, self._annee):
            raise ValueError("Jour invalide")
        self._jour = jour
    
    # Getters et setters pour mois
    def get_mois(self):
        """Retourne le mois de la date"""
        return self._mois
    
    def set_mois(self, mois):
        """
        Modifie le mois de la date si la nouvelle date est valide
        
        Args:
            mois (int): Le nouveau mois de la date
        
        Raises:
            ValueError: Si la nouvelle date est invalide
        """
        if not self._est_date_valide(self._jour, mois, self._annee):
            raise ValueError("Mois invalide")
        self._mois = mois
    
    # Getters et setters pour annee
    def get_annee(self):
        """Retourne l'année de la date"""
        return self._annee
    
    def set_annee(self, annee):
        """
        Modifie l'année de la date si la nouvelle date est valide
        
        Args:
            annee (int): La nouvelle année de la date
        
        Raises:
            ValueError: Si la nouvelle date est invalide
        """
        if not self._est_date_valide(self._jour, self._mois, annee):
            raise ValueError("Année invalide")
        self._annee = annee
    
    def _est_date_valide(self, jour, mois, annee):
        """
        Vérifie si une date est valide
        
        Args:
            jour (int): Le jour à vérifier
            mois (int): Le mois à vérifier
            annee (int): L'année à vérifier
        
        Returns:
            bool: True si la date est valide, False sinon
        """
        if mois < 1 or mois > 12:
            return False
        
        # Déterminer le nombre de jours dans le mois
        jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Vérification année bissextile
        if mois == 2 and self._est_bissextile(annee):
            jours_dans_mois = 29
        else:
            jours_dans_mois = jours_par_mois[mois]
        
        return 1 <= jour <= jours_dans_mois
    
    def _est_bissextile(self, annee):
        """
        Vérifie si une année est bissextile
        
        Args:
            annee (int): L'année à vérifier
        
        Returns:
            bool: True si l'année est bissextile, False sinon
        """
        return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
    
    def to_string(self):
        """
        Convertit la date en chaîne de caractères
        
        Returns:
            str: La date au format JJ/MM/AAAA
        """
        return f"{self.get_jour():02d}/{self.get_mois():02d}/{self.get_annee():04d}"
    
    def difference(self, autre_date):
        """
        Calcule le nombre de jours entre cette date et une autre date
        Cette méthode est une approximation simple, elle ne prend pas en compte
        tous les détails comme les années bissextiles pour chaque jour.
        
        Args:
            autre_date (Date): La date avec laquelle calculer la différence
        
        Returns:
            int: Le nombre de jours entre les deux dates (valeur absolue)
        """
        # Cette implémentation est approximative
        # Une version plus précise nécessiterait l'utilisation de datetime
        jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Convertir les deux dates en nombre de jours depuis une date arbitraire
        def date_to_jours(date):
            jours = date.get_jour()
            
            # Ajouter les jours des mois précédents de cette année
            for m in range(1, date.get_mois()):
                if m == 2 and self._est_bissextile(date.get_annee()):
                    jours += 29
                else:
                    jours += jours_par_mois[m]
            
            # Ajouter les jours des années précédentes (approximation)
            jours += date.get_annee() * 365
            
            # Ajuster pour les années bissextiles (approximation)
            jours += date.get_annee() // 4 - date.get_annee() // 100 + date.get_annee() // 400
            
            return jours
        
        jours1 = date_to_jours(self)
        jours2 = date_to_jours(autre_date)
        
        return abs(jours1 - jours2)
    
    def __str__(self):
        """
        Représentation en chaîne de la date
        
        Returns:
            str: La date au format JJ/MM/AAAA
        """
        return self.to_string()