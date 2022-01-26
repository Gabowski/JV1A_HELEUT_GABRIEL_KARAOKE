
# Je modélise la classe "Player"
class Player :
    def __init__(self, pseudo) :                            # Options de la classe "Player"
        self.__name = pseudo
    def getName(self) :                                     # Renvoie du nom du joueur
        return self.__name

# Je modélise la classe "Karaoke"
class Karaoke :
    def _init_(self, nommusic, lista) :                     # Options de la classe "Karaoke"
        self.__nom = nommusic
        self.__listepoints = lista
    def getNom(self) :                                      # Renvoie du nom de la musique
        return self.__nom
    def getListe(self) :
        return self.__listepoints                           # Renvoie de la liste de points des joueurs
    

# Je déclare les 4 joueurs, leur score est pour l'instant de 50
player1 = Player("Dylan", 50)
player2 = Player("Gabriel", 50)
player3 = Player("Aurélien", 50)
player4 = Player("Corentin", 50)

# Je déclare les 6 musiques que vont chanter les joueurs
music1 = Karaoke("Lost in the Dark")
music2 = Karaoke("In the End")
music3 = Karaoke("Afraid to die")
music4 = Karaoke("Run to the sky")
music5 = Karaoke("Fight like a knight")
music6 = Karaoke("Fire is power")