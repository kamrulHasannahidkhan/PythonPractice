def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_str = str(n)[::-1]
    return sign * int(reversed_str)

print(reverse_integer(-1234))