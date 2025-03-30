def sumOfNaturalNumber(number:int) -> int:
    if number <= 1:
        return number
    return number + sumOfNaturalNumber(number-1)

print(sumOfNaturalNumber(54))
