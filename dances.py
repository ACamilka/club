# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Move(object):
    """Движение
    """
    def __init__(self, description):
        self.__description = description

    @property
    def description(self):
        return self.__description

    def __call__(self):
        return self.description


class BaseDance(object):
    """Базовый танец.
    """
    def __init__(self):
        self.__moves = []
        self.set_moves()

    @classmethod
    def get_name(cls):
        return cls.__name__

    @property
    def moves(self):
        return self.__moves

    def set_moves(self):
        raise NotImplementedError('Метод должен быть переопределен')

    def add_move(self, move):
        if move not in self.moves:
            self.moves.append(move)

    def delete_move(self, move):
        if move in self.moves:
            self.moves.remove(move)


class Rnb(BaseDance):
    def set_moves(self):
        self.add_move(Move('покачивание телом вперед и назад'))
        self.add_move(Move('ноги в полу-присяде'))
        self.add_move(Move('руки согнуты в локтя'))
        self.add_move(Move('головой вперед-назад'))


class Electro(BaseDance):
    def set_moves(self):
        self.add_move(Move('вращения руками'))
        self.add_move(Move('покачивание туловищем вперед и назад'))
        self.add_move(Move('ноги двигаются в ритме'))


class Pop(BaseDance):
    def set_moves(self):
        self.add_move(Move('плавные движения туловищем'))
        self.add_move(Move('плавные движения руками'))
        self.add_move(Move('плавные движения ногами'))
        self.add_move(Move('плавные движения головой'))


class House(BaseDance):
    def set_moves(self):
        self.add_move(Move('вращения руками'))
        self.add_move(Move('плавные движения руками'))
        self.add_move(Move('матание головой'))


class Rock(BaseDance):
    def set_moves(self):
        self.add_move(Move('прыжки вверх'))
        self.add_move(Move('матание головой'))

