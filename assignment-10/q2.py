import numpy as np

def odd_magic_square(n):
    magic = np.zeros((n, n), dtype=int)
    num = 1
    i, j = 0, n // 2
    while num <= n**2:
        magic[i, j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic[newi, newj]:
            i += 1
        else:
            i, j = newi, newj
    return magic

def doubly_even_magic_square(n):
    magic = np.arange(1, n*n+1).reshape(n, n)
    indices = [(i, j) for i in range(n) for j in range(n)
               if (i % 4 == j % 4) or ((i + j) % 4 == 3)]
    for i, j in indices:
        magic[i, j] = n*n + 1 - magic[i, j]
    return magic

def singly_even_magic_square(n):
    half = n // 2
    sub_square = odd_magic_square(half)
    magic = np.zeros((n, n), dtype=int)
    indices = [(r, c) for r in range(half) for c in range(half)]

    for r, c in indices:
        magic[r][c] = sub_square[r][c]
        magic[r + half][c + half] = sub_square[r][c] + half * half
        magic[r][c + half] = sub_square[r][c] + 2 * half * half
        magic[r + half][c] = sub_square[r][c] + 3 * half * half

    k = half // 2
    for r in range(n):
        for c in range(n):
            if (c < k or c >= n - k) and not (r >= half and c == k):
                if (r < half):
                    magic[r][c], magic[r + half][c] = magic[r + half][c], magic[r][c]
    return magic

def generate_magic_square(n):
    if n % 2 == 1:
        return odd_magic_square(n)
    elif n % 4 == 0:
        return doubly_even_magic_square(n)
    else:
        return singly_even_magic_square(n)

for N in range(4, 9):
    print(f"\nMagic Square for N = {N}:\n")
    print(generate_magic_square(N))
