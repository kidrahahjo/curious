# TODO: https://docs.python.org/3/howto/annotations.html

from __future__ import annotations

x = 1

class A:
    def __init__(self: int) -> None:
        print(__annotations__)
        super(A).__init__()

a = A()

print(a.__init__.__annotations__)

__all__ = ["A"]