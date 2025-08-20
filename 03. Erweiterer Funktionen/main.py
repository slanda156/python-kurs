import random

import numpy as np

import src.structure
import src.structure as struc
from src import functions as func
from src.functions import dice


def main():
    func.hello()
    dice()
    seq = []
    func.fibonacci(10, seq)
    print(f"Fibonacci sequence up to 10: {seq}")


if __name__ == "__main__":
    main()
