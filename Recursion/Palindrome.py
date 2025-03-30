from helperFunction import substring

def isPalindrome(String:str) -> bool:
    if len(String) == 0 or len(String) == 1: return True
    if String[0] == String[len(String) - 1]:
        return isPalindrome(substring(String, startwith=1, endwith=len(String) - 1))
    return False

print(isPalindrome("racecar"))
print(isPalindrome(str(5005)))
print(isPalindrome("use"))
print(isPalindrome(str(5105)))
