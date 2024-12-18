# from project.player import Player
# from project.team import Team
#
#
# p = Player("Pall", 1, 3, 5, 7)
#
# print("Player name:", p.name)
# print("Points sprint:", p._Player__sprint)
# print("Points dribble:", p._Player__dribble)
# print("Points passing:", p._Player__passing)
# print("Points shooting:", p._Player__shooting)
#
# print("\ncalling the __str__ method")
# print(p)
#
# print("\nAbout the team")
# t = Team("Best", 10)
# print("Team name:", t._Team__name)
# print("Teams points:", t._Team__rating)
# print("Teams players:", len(t._Team__players))
# print(t.add_player(p))
# print(t.add_player(p))
# print("Teams players:", len(t._Team__players))
# print(t.remove_player("Pall"))
# print(t.remove_player("Pall"))
#
import unittest

from project.player import Player
from project.team import Team


class Tests(unittest.TestCase):
    def test_player_init(self):
        p = Player("Pall", 3, 3, 3, 3)
        self.assertEqual(p.name, "Pall")
        self.assertEqual(p._Player__sprint, 3)
        self.assertEqual(p._Player__passing, 3)
        self.assertEqual(p._Player__dribble, 3)
        self.assertEqual(p._Player__shooting, 3)

    def test_player_str(self):
        p = Player("Pall", 3, 3, 3, 3)
        result = str(p).strip()
        expected = "Player: Pall\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3"
        self.assertEqual(expected, result)

    def test_team_init(self):
        t = Team("Best", 10)
        self.assertEqual(t._Team__name, "Best")
        self.assertEqual(t._Team__rating, 10)
        self.assertEqual(len(t._Team__players), 0)

    def test_team_add_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)

        self.assertEqual(t.add_player(p), "Player Pall joined team Best")

    def test_team_add_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)

        t.add_player(p)
        self.assertEqual(t.add_player(p), "Player Pall has already joined")

    def test_team_remove_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)
        t.add_player(p)
        exp = t.remove_player("Pall")
        self.assertEqual(exp, p)

    def test_team_remove_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3)
        result = "Player Pall not found"
        exp = t.remove_player("Pall")
        self.assertEqual(exp, result)


if __name__ == "__main__":
    unittest.main()