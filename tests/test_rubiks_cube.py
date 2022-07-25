import pytest as pt

from utils import RubiksCube


def test_solved():
    cube = RubiksCube()
    assert cube.solved()
    not_solved_state = [[['o'] * 3] * 3] * 6
    cube.state = not_solved_state
    assert cube.solved() == False