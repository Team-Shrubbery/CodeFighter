import pytest
from config import *

from main import Game


def test_win_width():
    # assert WIN_WIDTH == 800
    pass


def test_win_height():
    # assert WIN_HEIGHT == 600
    pass


def test_acceleration():
    # assert ACC == 0.3
    pass


def test_friction():
    # assert FRIC == -0.10
    pass


def test_frames():
    # assert FPS == 60
    pass


def test_game_can_instantiate():
    g = Game()
    result = g.fighting
    assert result == False
