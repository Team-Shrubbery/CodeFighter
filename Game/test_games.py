import pytest
from config import *

def test_win_width():
    assert WIN_WIDTH == 800

def test_win_height():
    assert WIN_HEIGHT == 600

def test_acceleration():
    assert ACC == 0.3

def test_friction():
    assert FRIC == -.10

def test_frames():
    assert FPS == 60

