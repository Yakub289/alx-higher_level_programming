#!/usr/bin/python3


"""Write a class MyInt that inherits from int:"""


class MyInt(int):
    """Representating the `int` class"""
    def __eq__(self, other):
        """define eqn and return value"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """define inequality and return value"""
        return (super().__eq__(other))
