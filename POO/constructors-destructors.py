# (Get-Command python3).Path
class PartyAnimal:
    x = 0

    # Constructeur
    def __init__(self):
        print("Je suis construit !")

    def party(self):
        self.x = self.x + 1
        print("Pour l'instant je vaux : ", self.x)

    # Déstructeur
    def __del__(self):
        print("Je suis détruit !")


objet = PartyAnimal()
print(type(objet))
objet.party()
objet.party()
# Ici on affecte 42 à an, il n'est donc plus un objet et le deconstructor est appelé automatiquement !
objet = 42
print(type(objet))
print("objet contient la valeur : ", objet)
