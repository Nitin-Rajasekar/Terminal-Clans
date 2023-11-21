
from src.classes import place
from src.classes import render
from src.classes import revise
from src.classes import spell
from src.classes import end_check
from src.classes import stat_check



def render_game():
    place()
    render()
    revise()
    spell()
    end_check()
    stat_check()