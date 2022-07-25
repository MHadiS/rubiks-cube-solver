import pytest as pt

from utils import RubiksCube


@pt.fixture
def cube():
    return RubiksCube()


def test_solved(cube):
    assert cube.solved()
    not_solved_state = [[['o'] * 3] * 3] * 6
    cube.state = not_solved_state
    assert cube.solved() == False


def test_up(cube):
    expected_state1 = {
        'w': [['b'] * 3,
              ['w'] * 3,
              ['w'] * 3],

        'o': [['o'] * 3] * 3,

        'g': [['w'] * 3,
              ['g'] * 3,
              ['g'] * 3],

        'y': [['g'] * 3,
              ['y'] * 3,
              ['y'] * 3],

        'r': [['r'] * 3] * 3,

        'b': [['y'] * 3,
              ['b'] * 3,
              ['b'] * 3],
    }

    assert cube.up().state == expected_state1

    expected_state2 = {
        'w': [['g'] * 3,
              ['w'] * 3,
              ['w'] * 3],

        'o': [['o'] * 3] * 3,

        'g': [['y'] * 3,
              ['g'] * 3,
              ['g'] * 3],

        'y': [['b'] * 3,
              ['y'] * 3,
              ['y'] * 3],

        'r': [['r'] * 3] * 3,

        'b': [['w'] * 3,
              ['b'] * 3,
              ['b'] * 3],
    }
    
    assert cube.up(True).state == expected_state2