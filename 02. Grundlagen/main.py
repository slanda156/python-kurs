# Bool
varBool = True
varBool = bool()

# Integer
varInt = 42
varInt = int("42")
varHexInt = 0x2A
varBinInt = 0b101010
varIntHex = int("2A", 16)
varIntBin = int("101010", 2)

# Float
varFloat = 3.14
varFloat = float("3.14")

# String
varString = "Hello, World!"
varString = str(55)
fString = f"Das Ergebnis ist: {varInt:3.3f}"

varByteString = b"Hello, World!"
varByteString = varString.encode()
varStringBytes = varByteString.decode()

# Bytes / Bytearray
varBytes = bytes([72, 101, 108, 108, 111])  # b"Hello"
stringByte = varBytes.decode()
varByteArray = bytearray(varBytes)

# Datenstrukturen
varList = [1, 2, 3, 4, 5]
varList.sort()
varList.clear()
varList.append(6)
varList.extend([7, 8, 9])
varList.pop()
varList.reverse()
varList.insert(0, 0)
varList.insert(0, 0)

listLenght = len(varList)
sevenIndex = varList.index(7)
zeroCount = varList.count(0)

varTuple = (1, 2, 3, 4, 5)

varSet = {1, 2, 3, 4, 5}

varDict = {
    "key1": "value1",
    "key2": "value2"
}
varDict = {"key1": "value1", "key2": "value2"}
varDict["key3"] = "value3"
varDict.pop("key1")
varDict.clear()
varDict.update({"key2": "value2"})
value2 = varDict.get("key2")
value5 = varDict.get("key5", "default")
keys = varDict.keys()
values = varDict.values()
items = varDict.items()

# Kontrollstrukturen

if varBool:
    print("True")
elif not varBool:
    print("False")
else:
    print("not True nor False")

match varInt:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Something else")

if "test" in varString:
    print("Test gefunden")
elif "test" not in varString:
    print("Test nicht gefunden")

if varInt > 10 and varInt < 100 or not False:
    print("varInt ist zwischen 10 und 100")

if isinstance(varInt, int):
    print("varInt ist ein Integer")

# Schleifen

for i in range(5):
    print(i)

for i in varList:
    print(i)

for key, value in varDict.items():
    print(f"{key}: {value}")

while varFloat > 0:
    print(varFloat)
    varFloat -= 1.0

for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
