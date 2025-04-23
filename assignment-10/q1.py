import random

def is_valid(solution):
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(solution[i] - solution[j]):
                return False  
    return True

def generate_random_solution():
    while True:
        solution = list(range(8))
        random.shuffle(solution)
        if is_valid(solution):
            return solution

def print_board(solution):
    for row in range(8):
        line = ""
        for col in range(8):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

# Find and print a solution
solution = generate_random_solution()
print("A valid 8-Queens solution:")
print_board(solution)
