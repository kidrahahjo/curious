from __future__ import annotations

import sys


def size(data: object) -> int:
    return sys.getsizeof(data)


class A:
    pass


class B:
    def __init__(self: B, value: int) -> None:
        self.value = value


class C:
    def __init__(self: C) -> None:
        super(C).__init__()


a = A()
b = B(1)
c = C()


print(f"Size of None is {size(None)}")

print(f"Size of class A is {size(A)} bytes")
print(f"Size of instance of class A before variable assignment is {size(a)} bytes")
a.value = 1
print(f"Size of instance of class A after variable assignment is {size(a)} bytes")

print(f"Size of class B is {size(B)} bytes")
print(f"Size of instance of class B is {size(b)} bytes")


print(f"Size of class C is {size(C)} bytes")
print(f"Size of instance of class C is {size(c)} bytes")


# This is interesting to note that size of class is far more greater than the instance of the class
# TODO: Inverstigate why this happens
