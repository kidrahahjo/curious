import itertools
from typing import Any


def circular_encode(data: bytes) -> itertools.cycle:
	bits = bin(int.from_bytes(data, 'big'))[2:]
	cycle = itertools.cycle((i, int(x)) if i == 0 else int(x) for i, x in enumerate(bits))
	return cycle


def get_bits(encoded_data: itertools.cycle) -> str:
    bits = []
    iterate = False
    for info in encoded_data:
        if iterate:
            if isinstance(info, tuple):
                    return "0b" + "".join(map(lambda x: str(x), bits))
            bits.append(info)
        else:
            if isinstance(info, tuple):
                iterate = True
                bits.append(info[1])


def decode(encoded_data: itertools.cycle) -> Any:
    bits = get_bits(encoded_data)    
    return eval(bits)


int_values = [i for i in range(100)] + [2 ** 100]
datum = [int_value.to_bytes(32, 'big') for int_value in int_values]

for i, data in enumerate(datum):
    cycle = circular_encode(data)
    assert int_values[i] == decode(cycle)


# Interesting to note that for an infinite stream of data
# itertools.islice(data, 0, 5) always starts iterating from the 
# place it ended last time. This is due to the data being circular in nature.
# TODO: Add support for multiple types
