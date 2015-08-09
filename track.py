# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Track(object):
    """Музыкальная композиция
    """
    def __init__(self, dances):
        self.__dances = dances

    @property
    def dances(self):
        return self.__dances

    def do_play(self):
        print 'Начинает играть {}'.format(', '.join([
            dance.get_name() for dance in self.dances]))
