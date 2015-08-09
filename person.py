# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Sex(object):
    """Перечисление полов
    """
    MALE = 1
    FEMALE = 2

    values = {
        MALE: 'Он',
        FEMALE: 'Она',
    }


class Person(object):
    """Базовый класс человека
    """
    def __init__(self, name, dances, sex=None):
        self.__name = name
        self.__sex = sex
        self.__dances = dances

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @property
    def dances(self):
        return self.__dances

    def do(self, track):
        moves = []
        map(lambda x: moves.extend(x.moves),
            filter(lambda x: x in self.dances, track.dances))
        if not moves:
            print '{} идет в бар пить водку.'.format(self)
        else:
            print '{} начинает танцевать. {} выполняет движения: {}'.format(
                self,
                Sex.values[self.sex],
                ', '.join([move() for move in moves])
            )


class Male(Person):
    """Мужчина
    """
    def __init__(self, name, dances):
        super(Male, self).__init__(name, dances, sex=Sex.MALE)


class Female(Person):
    """Женщина
    """
    def __init__(self, name, dances):
        super(Female, self).__init__(name, dances, sex=Sex.FEMALE)
