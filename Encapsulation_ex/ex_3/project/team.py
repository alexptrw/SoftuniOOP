from project.player import Player


class Team:
    def __init__(self, name: str, rating:int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player:Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str:
        a = next((p for p in self.__players if p.name == player_name), None)
        # print(a.name)
        if a:
            self.__players.remove(a)
            # return str(a)
            return a
        return f"Player {player_name} not found"
