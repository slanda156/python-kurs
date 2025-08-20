# Typing
from typing import Any, Union, Optional, NewType

def testFunc(a: Union[int, float], b: Any, c: Optional[int]) -> int | float:
    if c is not None:
        return a + b + c
    else:
        return a + b

UserId = NewType("UserId", int)
id: UserId = 1

def userTest(id: int) -> UserId:
    return UserId(id)

id = userTest(1)

# Pathlib
from pathlib import Path

newPath = Path("folder")
if newPath.exists():
    print(f"Path {newPath} exists.")
else:
    newPath.mkdir(parents=True, exist_ok=True)
results = newPath.glob("*.jpg")
for result in results:
    print(result)
print(newPath.parts)

# Time
from time import time, time_ns

print(time())
print(time_ns())

# Datetime
from datetime import datetime

dt = datetime.now()
print(dt)

# Re (RegEx)
from  re import search, fullmatch

testStr1 = "test123@test.com"
testStr2 = "test123@test"
regEx = "[a-zA-Z0-9]+[@][a-zA-Z]+[.][a-zA-Z]+"
result = search(regEx, testStr1)
print(result)
result = fullmatch(regEx, testStr2)
print(result)

# Random
from random import random, randrange, choices

print(random())
print(randrange(0, 100))
nums = (1, 2, 3, 4, 5, 6)
weights = (0.1, 0.1, 0.1, 0.1, 0.1, 0.5)
print(choices(nums, weights))

# Logging
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
logger.critical("Critical message with exception", exc_info=True)
