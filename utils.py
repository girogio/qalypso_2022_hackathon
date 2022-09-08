def get_period(a: int, N: int) -> int:
    f_values = set()
    i = 0
    while True:
        value = (a**i) % N
        if value in f_values:
            return i
        f_values.add(value)
        i+=1


def is_good_root(a: int, N: int) -> bool:
    r = get_period(a, N)
    is_period_even = (r % 2) == 0 
    are_primes_sep = True
    if is_period_even:
        are_primes_sep = (pow(a, r/2) +1) % N != 0
    return r, (is_period_even and are_primes_sep)