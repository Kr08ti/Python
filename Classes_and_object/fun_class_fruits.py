class Fruits:
    def __init__(self):
        self.name1 = 'Grapes'
        self.name2 = 'Oranges'
        self.name3 = 'Apple'
        self.colours()
    def colours(self):
        colour1 = "Green"
        colour2 = "Orange"
        colour3 = "Red"
        print "The", self.name1, "are", colour1
        print "The", self.name2, "are", colour2
        print "The", self.name3, "are", colour3

F1 = Fruits()
