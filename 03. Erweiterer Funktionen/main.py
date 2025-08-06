import src.structure
import src.structure as struc
from src import functions
from src.functions import dice


def main():
    functions.hello()
    dice()
    seq = []
    functions.fibonacci(10, seq)
    print(f"Fibonacci sequence up to 10: {seq}")


if __name__ == "__main__":
    main()
