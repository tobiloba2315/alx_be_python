def get_positive_int(prompt="Enter the size of the pattern: "):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def draw_square(n):
    for _ in range(n):
        print("* " * n)

if __name__ == "__main__":
    size = get_positive_int()
    draw_square(size)
    
    