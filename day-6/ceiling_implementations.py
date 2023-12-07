"""
This is a list of implementations of the ceiling function
using just algebra.  This means trying to avoid booleans (and
I guess mods are allowed), and it should work for ALL real numbers,
not just integers.
"""

def ceil_div_mod_bool(a: float, b: float) -> int:
    return a // b + (a % b > 0)

def ceil_div_only_floor(a: float, b: float) -> int:
    return a // b - (b * (a // b) - a) // b

def ceil_div_negate(a: float, b: float) -> int:
    return a // b - (-(a % b) // b)

if __name__ == "__main__":
    ceils = [
        ceil_div_mod_bool,
        ceil_div_only_floor,
        ceil_div_negate
    ]

    test_cases = [
        ((1, 2), 1),
        ((10, 3), 4),
        ((4, 2), 2),
        ((0, 3), 0),
        ((1.5, 1.2), 2),
        ((1.5, 0.75), 2),
        ((15.835, 3.38734), 5)
    ]

    for (a, b), ans in test_cases:
        for ceil in ceils:
            if ans != ceil(a, b):
                print(f"FAILURE: {a}/{b} on {ceil}")