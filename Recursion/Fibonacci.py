def fibonacci(number:int) -> int:
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(6))