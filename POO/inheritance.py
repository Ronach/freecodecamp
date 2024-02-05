class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nem):
        self.name = nem
        print(self.name, " is constructed !")


    def party(self):
        self.x = self.x + 1
        print(self.name, " has a party count of ", self.x)


class FootballFan(PartyAnimal):
        points = 0
        def touchdown(self):
            self.points = self.points + 7
            # on peut appeler la méthode party() de la classe dont cet objet hérite
            self.party()
            print(self.name, "points", self.points)


sally = PartyAnimal("Sally")
sally.party()

jim = FootballFan("Jim")
jim.party()  # utilise la méthode party() de la classe PartyAnimal()
jim.touchdown()
