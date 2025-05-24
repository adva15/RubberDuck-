# דוגמא לפתרון

class EvilSpaceShip:
    __armor = 50
    def __init__(self, life=100):
        self.life = life
    @staticmethod
    def blowup_animation(space_ship):
        print(f'EvilSpaceShip with life {space_ship.life} blow up')
    @classmethod
    def get_armor(cls):
        return cls.__armor
    @classmethod
    def upgrade_10perc(cls):
        cls.__armor *= 1.1
    @property
    def life(self):
        return self.__life
    @life.setter
    def life(self, value):
        if value < 0:
            self.__life = 0
        else:
            self.__life = value

evilship1 = EvilSpaceShip(90)
evilship1.life += 50
evilship2 = EvilSpaceShip(215)
evilship2.life -= 250

print(EvilSpaceShip.get_armor())
EvilSpaceShip.upgrade_10perc()
EvilSpaceShip.blowup_animation(evilship1)
EvilSpaceShip.blowup_animation(evilship2)