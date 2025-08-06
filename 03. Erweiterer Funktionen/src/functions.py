import random

def hello() -> None:
    a: int = 1
    b: list[float] = [1.0, 2.0, 3.0]
    c: dict[str, int] = {"one": 1, "two": 2}
    print("Hello, World!")


def add(a: int, b: int) -> int:
    return a + b


def fibonacci(n: int, seq: list[int]) -> None:
    """Generate Fibonacci sequence up to n and append to seq.

    Arguments:
        n -- The upper limit for the Fibonacci sequence.
        seq -- The list to append Fibonacci numbers to.
    """
    if len(seq) == 0:
        seq.append(0)
    elif len(seq) == 1:
        seq.append(1)
    else:
        seq.append(seq[-1] + seq[-2])
    if seq[-1] < n:
        fibonacci(n, seq)


def dice() -> None:
    result = random.randint(1, 6)
    print(f"Du hast eine {result} geworfen.")
