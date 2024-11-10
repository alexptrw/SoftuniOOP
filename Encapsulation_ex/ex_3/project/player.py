class Player:
    def __init__(self,name:str, sprint:int, dribble:int, passing:int, shooting:int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:

        return f'Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}'


# p = Player('Gosho', 4, 5, 6, 7)
# print(p.sprint)
