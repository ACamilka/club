# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time


class Club(object):
    """Клуб.
    """
    REFRESH_TIMEOUT = 1

    def __init__(self):
        self.__tracks = []
        self.__dancers = []

    def set_tracks(self, tracks):
        self.__tracks = tracks

    def add_dancer(self, dancer):
        if dancer not in self.__dancers:
            self.__dancers.append(dancer)

    def delete_dancer(self, dancer):
        if dancer in self.__dancers:
            self.__dancers.remove(dancer)

    def run(self):
        for track in self.__tracks:
            track.do_play()
            for dancer in self.__dancers:
                time.sleep(self.REFRESH_TIMEOUT)
                dancer.do(track)
            time.sleep(self.REFRESH_TIMEOUT)
