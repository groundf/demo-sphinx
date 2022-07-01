# -*- coding: utf-8 -*-


"""
This is a :mod:`package.module1` documentation example.
"""

from typing import List, Tuple, Union, TypeVar


CustomTypeAlias = Union[List[str], Tuple[int, int]]
"""This is a type alias."""


CustomTypeVariable = TypeVar("T", bound=int)
"""This is a type variable."""


CONSTANT: str = "constant"


def function(argument1: int = 1, argument2: float = 1.0) -> None:
    """
    The function documentation example.

    $y = \sin(x)$

    :param arg: The rgumens
    :return: None
    :raise: SomeException
    """


class Error(Exception):
    """Custom exception. 
    """


class Example:
    """
    The class documentation example.
    """

    def example() -> None:
        """
        The method documentation example.
        """
