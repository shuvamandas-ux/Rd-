def binary_xo(n):
    """
    Convert an integer to its binary representation using X for 1 and O for 0.
    """
    if n == 0:
        return 'O'
    binary = ''
    while n > 0:
        binary = ('X' if n % 2 == 1 else 'O') + binary
        n //= 2
    return binary

# Example usage
if __name__ == "__main__":
    for num in [0, 1, 2, 3, 4, 5, 10, 15]:
        print(f"{num}: {binary_xo(num)}")