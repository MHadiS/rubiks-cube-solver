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
    expected_state = {
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

    assert cube.up_down("up").state == expected_state
    cube.up(True)


def test_up_inverse(cube):
    expected_state = {
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
    
    assert cube.up_down("up", True).state == expected_state
    cube.up()


def test_down(cube):
    expected_state = {
        'w': [['w'] * 3,
              ['w'] * 3,
              ['b'] * 3],

        'o': [['o'] * 3] * 3,

        'g': [['g'] * 3,
              ['g'] * 3,
              ['w'] * 3],

        'y': [['y'] * 3,
              ['y'] * 3,
              ['g'] * 3],

        'r': [['r'] * 3] * 3,

        'b': [['b'] * 3,
              ['b'] * 3,
              ['y'] * 3],
    }

    assert cube.up_down("down").state == expected_state
    cube.up_down("down", True)
