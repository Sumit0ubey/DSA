def decimalTObinary(decimal:int, result:str="") -> str:
    if decimal == 0:
        return result
    result = str(decimal % 2) + result
    return decimalTObinary(decimal//2, result)

print(decimalTObinary(56))