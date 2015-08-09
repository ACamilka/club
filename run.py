# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from club import Club
from track import Track
from person import Male, Female
from dances import Rnb, Electro, Pop, House, Rock


if __name__ == "__main__":
    rnd = Rnb()
    electro = Electro()
    house = House()
    rock = Rock()
    pop = Pop()

    club = Club()

    club.set_tracks([
        Track([rnd, rock]),
        Track([electro, house]),
        Track([pop]),
    ])

    club.add_dancer(Female('Анна', [rock, house]))
    club.add_dancer(Female('Катя', [rnd, house, electro]))
    club.add_dancer(Male('Антон', [pop]))
    club.add_dancer(Male('Саша', [rock, pop, rnd]))
    club.add_dancer(Female('Света', [pop, electro]))

    club.run()
