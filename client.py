class Client:
  
    def __init__(self, id_client, nom):
       
        self._id_client = id_client
        self._nom = nom     
    
    def get_id_client(self):
       
        return self._id_client
    
    def set_id_client(self, id_client):
       
        self._id_client = id_client
    
   
    def get_nom(self):
       
        return self._nom
    
    def set_nom(self, nom):
       
        self._nom = nom
    
   
    
   
        
    
    def infos(self):
       
        return (f"Client #{self.get_id_client()} - {self.get_nom()} \n"
        )