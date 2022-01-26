
# Je modélise la classe "Player"
class Player :
    def __init__(self,pseudo,score,wybormusic,listapunkt) :                     # Options de la classe
        self.__name = pseudo
        self.__score = score
        self.__wybor = wybormusic
        self.__lista = listapunkt
    def getName(self) :                                                         # Renvoie du nom du joueur
        return self.__name
    def getScore(self,bestscore) :                                              # Fonction permettant de dire au joueur s'il a battu son record en obtenant un meilleur score                         
        self._bestscore = bestscore
        if self._bestscore > self.__score :
            self.__score = self._bestscore
            print("Félicitations ! Vous avez battu votre record !")
        else :
            print("Dommage, vous n'avez pas battu votre record mais vous puvez retenter votre chance !")
        if self.__score < 50 :
            self.__score = 50
        return self.__score
    def getMusic(self) :                                                        # Liste des 5 chansons
        self.__wybor = [0, 1, 2, 3, 4]
        return self.__wybor
    def getList(self) :                                                         # Je renvoie la liste de points
        return self.__lista
    def GorszyScore(self) :                                                     # Fonction permettant d'afficher le pire score
        worstscore = self.__score [0]
        for i in range (1,5) :
            if self.__score [i-1] <= self.__score [i] :
                if self.__score [i-1] < worstscore :
                    worstscore = self.__score [i-1]
                print("Votre pire score est de", worstscore)
    def LepszyScore(self) :                                                    # Fonction permettant d'afficher le meilleur score
        bestscore = self.__score [0]
        for i in range (1,5) :
            if self.__score [i-1] >= self.__score [i] :
                if self.__score [i-1] > bestscore :
                    bestscore = self.__score [i-1]
                print("Votre meilleur score est de", bestscore)
    def BestScore(self) :                                                      # Affiche le meilleur score tout joueur confondue
        bestscore = self.__score [0]
        for i in range (self.__score) :
            bestscore += self.__score [i]
        print(bestscore)
                
# Je déclare les 4 joueurs, leur score est pour l'instant de 50
player1 = Player("Dylan", 50)
player2 = Player("Gabriel", 50)
player3 = Player("Aurélien", 50)
player4 = Player("Corentin", 50)

