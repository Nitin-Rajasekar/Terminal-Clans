class Person:
    health = 0
    beg_health = 0
    colour = 0

    def find_colour(self):
        if self.health >= float(self.beg_health/2):
            self.colour = 'G'
        elif self.health >= float(self.beg_health/5):
            self.colour = 'Y'
        elif self.health > 0:
            self.colour = 'R'
        else:
            self.alive=0
            self.colour = 'N'


class Building:
    health = None
    beg_health = None
    colour = None

    def find_colour(self):
        if self.health >= float(self.beg_health/2):
            self.colour = 'G'
        elif self.health >= float(self.beg_health/5):
            self.colour = 'Y'
        elif self.health > 0:
            self.colour = 'R'
        else:
            self.alive=0
            self.colour = 'N'