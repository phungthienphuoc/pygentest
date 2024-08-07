import random
from collections.abc import Sequence

def randint(a, b):
    """Get a random integer in inclusive range [a,b].
        
    Args:
        `a`: Lowerbound of range.
        `b`: Upperbound of range.
    """
    return random.randint(a, b)


def randfloat(a, b):
    """Get a random number in the range [a, b) or [a, b] depending on rounding.

    Args:
        `a`: Lowerbound of range.
        `b`: Upperbound of range.
    """
    return random.uniform(a, b)

def randchar(chars):
    """Get a random character from the given list of character.
    
    Args:
        `chars`: List of character.
    """
    if not isinstance(chars, Sequence):
        raise TypeError(f"Argument must have a sequence type.")
    x = random.choice(chars)
    if not isinstance(x, str):
        raise TypeError(f"Argument must contain <str>, not <{type(x).__name__}>.")
    if len(x) != 1:
        raise ValueError("Length of character must be exactly 1.")
    return x